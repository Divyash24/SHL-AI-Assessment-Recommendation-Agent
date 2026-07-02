import re

from app.rag.retriever import retrieve
from app.services.gemini_services import generate_response


ROLE_KEYWORDS = [
    "developer",
    "engineer",
    "manager",
    "analyst",
    "sales",
    "marketing",
    "java",
    "python",
    "backend",
    "frontend",
    "full stack",
    "qa",
    "tester",
    "intern",
    "graduate",
    "executive",
    "leader",
    "hr",
    "recruiter",
]

EXPERIENCE_PATTERN = r"(\d+\+?\s*(year|years|yr|yrs))"


def has_role(text):

    text = text.lower()

    return any(keyword in text for keyword in ROLE_KEYWORDS)


EXPERIENCE_KEYWORDS = [
    "junior",
    "mid",
    "mid-level",
    "mid level",
    "senior",
    "lead",
    "entry",
    "entry-level",
    "entry level",
    "graduate",
    "experienced",
    "manager",
    "director",
]


def has_experience(text):

    text = text.lower()

    if re.search(EXPERIENCE_PATTERN, text):
        return True

    for keyword in EXPERIENCE_KEYWORDS:
        if keyword in text:
            return True

    return False


def chat(messages):

    conversation = []

    user_text = ""

    for msg in messages:

        conversation.append(
            f"{msg.role.upper()}: {msg.content}"
        )

        if msg.role == "user":
            user_text += " " + msg.content

    user_text = user_text.strip()

    # --------------------------
    # Missing Role
    # --------------------------

    if not has_role(user_text):

        return {

            "reply":
            "Sure! Which role are you hiring for?",

            "recommendations": [],

            "end_of_conversation": False

        }

    # --------------------------
    # Missing Experience
    # --------------------------

    if not has_experience(user_text):

        return {

            "reply":
            "Got it. What experience level are you hiring for?",

            "recommendations": [],

            "end_of_conversation": False

        }

    # --------------------------
    # Enough Information
    # --------------------------

    docs = retrieve(user_text)

    answer = generate_response(
        "\n".join(conversation),
        docs
    )

    recommendations = []

    for doc in docs:

        recommendations.append({

            "name": doc["metadata"]["name"],

            "url": doc["metadata"]["url"],

            "test_type": "Assessment"

        })

    return {

        "reply": answer,

        "recommendations": recommendations,

        "end_of_conversation": True

    }