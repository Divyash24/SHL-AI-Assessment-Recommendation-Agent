from app.rag.loader import load_catalog
from app.rag.preprocessor import preprocess_catalog

catalog = load_catalog()

documents = preprocess_catalog(catalog)

print(f"\nLoaded {len(documents)} documents\n")

print(documents[0])