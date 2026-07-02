import json
import re
from pathlib import Path

from app.config import DATA_PATH


def load_catalog():
    """
    Load and sanitize SHL Product Catalog JSON.
    """

    file_path = Path(DATA_PATH)

    if not file_path.exists():
        raise FileNotFoundError(f"Catalog not found: {DATA_PATH}")

    # Read raw file
    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read()

    # Remove illegal control characters
    raw = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F]", "", raw)

    catalog = json.loads(raw)

    print(f"\n✅ Loaded {len(catalog)} assessments successfully.\n")

    return catalog