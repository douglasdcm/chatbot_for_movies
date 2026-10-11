import os
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# ----------------------------
# CONFIG
# ----------------------------
MODEL_PATH = "/home/douglas/repo/chatbot_for_movies/src/chatdata/model.h5"
FAISS_INDEX_PATH = "faiss.index"


EMBEDER = SentenceTransformer("all-MiniLM-L6-v2")

Base = declarative_base()

# ---------- DATABASE SETUP ----------
DATABASE_URL = "sqlite:///chatbot.db"
engine = create_engine(DATABASE_URL, echo=False)
def create_database():
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    msg = Column(Text, nullable=False)
    msg_2 = Column(Text, nullable=False)
    target = Column(Integer, nullable=False)

def load_index():
    return faiss.read_index(FAISS_INDEX_PATH)

# ----------------------------
# BUILD / LOAD FAISS (WITH IDS)
# ----------------------------
def build_and_save_index():
    session = Session()
    rows = session.query(Conversation.id, Conversation.msg).all()

    ids = []
    texts = []

    for r in rows:
        ids.append(r.id)
        texts.append(r.msg)

    embeddings = EMBEDER.encode(texts, convert_to_numpy=True)
    faiss.normalize_L2(embeddings)

    dim = embeddings.shape[1]

    base_index = faiss.IndexFlatIP(dim)
    index = faiss.IndexIDMap(base_index)

    ids_np = np.array(ids, dtype=np.int64)
    index.add_with_ids(embeddings, ids_np)

    faiss.write_index(index, FAISS_INDEX_PATH)

    session.close()
    return index


if os.path.exists(FAISS_INDEX_PATH):
    print("Loading FAISS index...")
    INDEX = load_index()
else:
    print("Building FAISS index...")
    INDEX = build_and_save_index()

INDEX
# ----------------------------
# OPTIONAL: ADD NEW DATA TO INDEX
# ----------------------------
def add_to_index(new_rows):
    texts = [r.msg for r in new_rows]
    ids = [r.id for r in new_rows]

    embeddings = EMBEDER.encode(texts, convert_to_numpy=True)
    faiss.normalize_L2(embeddings)

    INDEX.add_with_ids(embeddings, np.array(ids, dtype=np.int64))

    faiss.write_index(INDEX, FAISS_INDEX_PATH)