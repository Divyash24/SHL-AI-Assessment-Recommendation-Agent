import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Project Paths
DATA_PATH = "data/shl_product_catalog_clean.json"

VECTOR_INDEX_PATH = "vector_store/faiss.index"

METADATA_PATH = "vector_store/metadata.pkl"

# Retrieval Settings
TOP_K_RESULTS = 5