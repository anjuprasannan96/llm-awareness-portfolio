# app.py
import streamlit as st
import requests

st.set_page_config(page_title="Local Chat App", layout="wide")
st.title("🤖 Chat with Local LLM (via Ollama)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Your Message", key="user_input")

if st.button("Send"):
    if user_input:
        # Show user message
        st.session_state.chat_history.append(("You", user_input))

        # Send prompt to FastAPI server
        try:
            res = requests.post("http://localhost:8000/chat", json={"prompt": user_input})
            answer = res.json().get("response", "No response")
        except Exception as e:
            answer = f"Error connecting to backend: {e}"

        # Show bot response
        st.session_state.chat_history.append(("Bot", answer))

# Display conversation
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
