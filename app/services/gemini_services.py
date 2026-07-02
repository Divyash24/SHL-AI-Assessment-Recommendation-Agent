import google.generativeai as genai

from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(user_query, retrieved_docs):

    context = ""

    for i, doc in enumerate(retrieved_docs, start=1):

        context += f"""
Assessment {i}

{doc["text"]}

-------------------------

"""

    prompt = f"""
You are an AI-powered SHL Assessment Recommendation Assistant.

You MUST answer ONLY using the assessment information provided below.

Rules:

1. Never invent or hallucinate assessments.
2. If information is unavailable in the provided context, clearly say:
   "I couldn't find this information in the SHL assessment catalog."
3. Recommend the most suitable assessment(s).
4. Explain WHY each assessment is recommended.
5. Mention duration, job level, remote testing and adaptive testing if available.
6. If the user asks to compare assessments, compare only those found in the context.
7. If the user's request is vague, ask one concise clarifying question instead of guessing.
8. Keep answers professional and concise.
9. Always mention the assessment name exactly as provided.

Context:

{context}

User Question:

{user_query}
"""


    response = model.generate_content(prompt)

    return response.text