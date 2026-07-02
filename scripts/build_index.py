from app.rag.loader import load_catalog
from app.rag.preprocessor import preprocess_catalog
from app.rag.embeddings import build_vector_store

catalog = load_catalog()

documents = preprocess_catalog(catalog)

build_vector_store(documents)