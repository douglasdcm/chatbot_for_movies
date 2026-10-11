from pathlib import Path
import csv
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from tqdm import tqdm

# ----------------------------
# DB SETUP
# ----------------------------
Base = declarative_base()

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    msg = Column(Text, nullable=False)
    msg_2 = Column(Text, nullable=False)
    target = Column(Integer, nullable=False)

DATABASE_URL = "sqlite:///chatbot.db"
engine = create_engine(DATABASE_URL, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# ----------------------------
# CONFIG
# ----------------------------
FAISS_INDEX_PATH = "faiss.index"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
DB_BATCH_SIZE = 1000
EMBED_BATCH_SIZE = 64
STREAM_BATCH_SIZE = 256
EMBEDDING_DIM = 384

# ----------------------------
# EMBEDDER
# ----------------------------
embedder = SentenceTransformer(EMBEDDING_MODEL, device="cpu")

# ----------------------------
# FAISS HELPERS
# ----------------------------
def create_index():
    return faiss.IndexIDMap(faiss.IndexFlatIP(EMBEDDING_DIM))

def save_index(index):
    faiss.write_index(index, FAISS_INDEX_PATH)

# ----------------------------
# STREAM INSERT + INDEX (MAIN)
# ----------------------------
def load_tsv_stream_and_build_index(file_path: str):
    session = Session()
    index = create_index()

    file_path = Path(file_path).expanduser()

    db_batch = []
    texts_batch = []
    ids_batch = []

    total = 0

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")

        for i, row in tqdm(enumerate(reader)):
            try:
                msg = row[3]
                msg_2 = row[4]
                target = int(row[6])

                if not msg:
                    continue

                conv = Conversation(msg=msg, msg_2=msg_2, target=target)
                db_batch.append(conv)

                # When DB batch is full → flush to get IDs
                if len(db_batch) >= DB_BATCH_SIZE:
                    session.add_all(db_batch)
                    session.flush()  # get IDs without commit

                    for r in tqdm(db_batch):
                        if r.id and r.msg:
                            ids_batch.append(r.id)
                            texts_batch.append(r.msg)

                    # Embed in chunks (avoid memory spikes)
                    for j in tqdm(range(0, len(texts_batch), STREAM_BATCH_SIZE)):
                        sub_texts = texts_batch[j:j+STREAM_BATCH_SIZE]
                        sub_ids = ids_batch[j:j+STREAM_BATCH_SIZE]

                        embeddings = embedder.encode(
                            sub_texts,
                            convert_to_numpy=True,
                            show_progress_bar=False,
                            batch_size=EMBED_BATCH_SIZE
                        )

                        faiss.normalize_L2(embeddings)

                        index.add_with_ids(
                            embeddings,
                            np.array(sub_ids, dtype=np.int64)
                        )

                    total += len(db_batch)
                    print(f"Processed {total}")

                    # Clear batches
                    db_batch.clear()
                    texts_batch.clear()
                    ids_batch.clear()

                    session.commit()

            except Exception as e:
                print(f"Skipping row {i}: {e}")

        # Handle remaining
        if db_batch:
            session.add_all(db_batch)
            session.flush()

            for r in tqdm(db_batch):
                if r.id and r.msg:
                    ids_batch.append(r.id)
                    texts_batch.append(r.msg)

            for j in tqdm(range(0, len(texts_batch), STREAM_BATCH_SIZE)):
                sub_texts = texts_batch[j:j+STREAM_BATCH_SIZE]
                sub_ids = ids_batch[j:j+STREAM_BATCH_SIZE]

                embeddings = embedder.encode(
                    sub_texts,
                    convert_to_numpy=True,
                    show_progress_bar=False,
                    batch_size=EMBED_BATCH_SIZE
                )

                faiss.normalize_L2(embeddings)

                index.add_with_ids(
                    embeddings,
                    np.array(sub_ids, dtype=np.int64)
                )

            total += len(db_batch)
            print(f"Processed {total} (final)")

            session.commit()

    save_index(index)
    session.close()

    print("Index build completed.")

# ----------------------------
# RUN
# ----------------------------
if __name__ == "__main__":
    load_tsv_stream_and_build_index(
        "/home/douglas/repo/chatbot_for_movies/src/chatdata/orig/movie_lines_pre_processed.tsv"
    )