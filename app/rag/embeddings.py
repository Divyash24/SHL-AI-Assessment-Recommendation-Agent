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

model = None


def get_model():
    global model

    if model is None:
        print("Loading embedding model...")
        model = SentenceTransformer(MODEL_NAME)

    return model


def build_vector_store(documents):

    texts = [doc["text"] for doc in documents]

    print("Generating embeddings...")

    model = get_model()

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True,
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings.astype("float32"))

    Path("vector_store").mkdir(exist_ok=True)

    faiss.write_index(index, VECTOR_INDEX_PATH)

    with open(METADATA_PATH, "wb") as f:
        pickle.dump(documents, f)

    print(f"\n✅ Indexed {len(documents)} assessments.")