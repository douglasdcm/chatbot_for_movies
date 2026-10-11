import faiss
import re

from tensorflow.keras.models import load_model

from pipeline import EMBEDER,  MODEL_PATH
from setup_dabatabase import Conversation, Session
from src.backend.dataset import Dataset



# ----------------------------
# LOAD MODELS
# ----------------------------
classifier = load_model(MODEL_PATH)

ds = Dataset()
tokenizer = ds.load_tokenizer()

FAISS_INDEX_PATH = "faiss.index"
def load_index():
    return faiss.read_index(FAISS_INDEX_PATH)

# ----------------------------
# CLASSIFIER
# ----------------------------
def classify_text(text: str) -> int:
    vec = tokenizer.texts_to_matrix([text], mode='binary')  # adjust if needed
    pred = classifier.predict(vec, verbose=0)[0][0]
    return int(pred > 0.5)


# ----------------------------
# RESPONSE REPHRASER
# ----------------------------
def rephrase_response(response: str) -> str:
    r = response.strip()

    if re.match(r"^(yes|yeah|yep)\b", r.lower()):
        return "Yes."
    if re.match(r"^(no|nope)\b", r.lower()):
        return "No."

    if r.endswith("?"):
        return "Could you clarify your question?"

    if len(r.split()) > 12:
        return "I'm not sure I can answer that clearly."

    return r


# ----------------------------
# RAG CHAT (DB-BASED)
# ----------------------------
def rag_chat(user_input: str, top_k: int = 3):
    session = Session()

    # classify input
    user_type = classify_text(user_input)

    # embed query
    query_vec = EMBEDER.encode([user_input], convert_to_numpy=True)
    faiss.normalize_L2(query_vec)

    # search FAISS
    D, I = load_index().search(query_vec, top_k)
    try:
        I[0]
    except Exception:
        return "I don't know how to answer that. Talk more about it"

    ids = [int(i) for i in I[0] if i != -1]

    if not ids:
        return "Explain it better"

    # fetch from DB
    results = (
        session.query(Conversation)
        .filter(Conversation.id.in_(ids))
        .all()
    )

    # filter by TAG
    filtered = [r for r in results if r.target == user_type]
    session.close()
    if filtered:
        return filtered[0].msg_2
    if results:
        return results[0].msg

    return "I don't know how to answer that. Give me examples"






# ----------------------------
# CLI
# ----------------------------
if __name__ == "__main__":
    print("Chatbot ready (type 'exit')\n")
    context = []

    while True:
        user_input = input("You: ")
        context.append(user_input)

        if user_input.lower() == "exit":
            break

        print(" ".join(context[-2:]))
        response = rag_chat(" ".join(context[-2:]))
        print(f"Bot: {response}\n")
