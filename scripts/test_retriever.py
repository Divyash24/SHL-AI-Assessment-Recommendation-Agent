from app.rag.retriever import retrieve

query = "I need a personality assessment for software developers"

results = retrieve(query)

for i, item in enumerate(results, start=1):

    print("=" * 80)

    print(f"Result {i}")

    print(item["metadata"]["name"])

    print(item["metadata"]["url"])