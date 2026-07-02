from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
from pathlib import Path

from app.config import (
    VECTOR_INDEX_PATH,
    METADATA_PATH,
)

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def build_vector_store(documents):

    texts = [doc["text"] for doc in documents]

    print("Generating embeddings...")

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True,
        normalize_embeddings=True,   # ⭐ Important
    )

    dimension = embeddings.shape[1]

    # ⭐ Cosine similarity using Inner Product
    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings.astype(np.float32))

    Path("vector_store").mkdir(exist_ok=True)

    faiss.write_index(index, VECTOR_INDEX_PATH)

    with open(METADATA_PATH, "wb") as f:
        pickle.dump(documents, f)

    print(f"\n✅ Indexed {len(documents)} assessments.")