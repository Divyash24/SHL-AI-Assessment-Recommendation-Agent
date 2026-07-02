import pickle
import faiss
from sentence_transformers import SentenceTransformer

from app.config import (
    VECTOR_INDEX_PATH,
    METADATA_PATH,
    TOP_K_RESULTS,
)

MODEL_NAME = "all-MiniLM-L6-v2"

model = None
index = None
documents = None


def load_resources():
    global model, index, documents

    if model is None:
        print("Loading embedding model...")
        model = SentenceTransformer(MODEL_NAME)

    if index is None:
        print("Loading FAISS index...")
        index = faiss.read_index(VECTOR_INDEX_PATH)

    if documents is None:
        print("Loading metadata...")
        with open(METADATA_PATH, "rb") as f:
            documents = pickle.load(f)


def retrieve(query, top_k=TOP_K_RESULTS):

    load_resources()

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        query_embedding.astype("float32"),
        top_k,
    )

    results = []

    for idx, distance in zip(indices[0], distances[0]):

        doc = documents[idx].copy()
        doc["score"] = float(distance)
        results.append(doc)

    return results