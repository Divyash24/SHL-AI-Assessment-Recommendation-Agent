from app.rag.retriever import retrieve
from app.services.gemini_services import generate_response

query = "Recommend an assessment for hiring backend software engineers."

docs = retrieve(query)

answer = generate_response(query, docs)

print(answer)