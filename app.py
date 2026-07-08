import streamlit as st
from dataclasses import dataclass

from app.services.chat_service import chat


@dataclass
class Message:
    role: str
    content: str

st.set_page_config(
    page_title="SHL AI Assessment Recommendation Agent",
    page_icon="🧠",
    layout="centered",
)

st.title("🧠 SHL AI Assessment Recommendation Agent")
st.caption(
    "Describe the role you're hiring for and I'll recommend the most suitable SHL assessments."
)

# ── Session state ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []          # list of {"role": str, "content": str}
if "conversation_ended" not in st.session_state:
    st.session_state.conversation_ended = False

# ── Render chat history ────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Chat input ─────────────────────────────────────────────────────────────────
if st.session_state.conversation_ended:
    st.info("Conversation complete. Refresh the page to start a new session.")
else:
    user_input = st.chat_input("e.g. I'm hiring a senior Python backend engineer…")

    if user_input:
        # Store and display the user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Build the Message objects expected by chat_service
        history = [
            Message(role=m["role"], content=m["content"])
            for m in st.session_state.messages
        ]

        with st.spinner("Thinking…"):
            result = chat(history)

        reply = result.get("reply", "")
        recommendations = result.get("recommendations", [])
        end_of_conversation = result.get("end_of_conversation", False)

        # Build the assistant reply text
        assistant_text = reply

        if recommendations:
            assistant_text += "\n\n**Recommended Assessments:**\n"
            for rec in recommendations:
                name = rec.get("name", "Unknown")
                url = rec.get("url", "")
                test_type = rec.get("test_type", "Assessment")
                if url:
                    assistant_text += f"- [{name}]({url}) — {test_type}\n"
                else:
                    assistant_text += f"- {name} — {test_type}\n"

        # Store and display the assistant message
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_text}
        )
        with st.chat_message("assistant"):
            st.markdown(assistant_text)

        if end_of_conversation:
            st.session_state.conversation_ended = True
            st.success("✅ Recommendations complete! Refresh the page to start over.")
