import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from app.config import (
    VECTOR_INDEX_PATH,
    METADATA_PATH,
    TOP_K_RESULTS,
)

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

# Load FAISS index
index = faiss.read_index(VECTOR_INDEX_PATH)

# Load metadata
with open(METADATA_PATH, "rb") as f:
    documents = pickle.load(f)


def retrieve(query, top_k=TOP_K_RESULTS):
    """
    Retrieve top-k relevant assessments using cosine similarity.
    """

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
    )

    scores, indices = index.search(
        query_embedding.astype(np.float32),
        top_k,
    )

    results = []

    for idx, score in zip(indices[0], scores[0]):

        doc = documents[idx].copy()

        doc["score"] = round(float(score), 4)

        results.append(doc)

    return results