"""
Assignment 24 - Ollama Chatbot (Streamlit version)
- Chat UI built with Streamlit
- Uses LangChain's Ollama LLM wrapper (model: gemma3:1b)
- Every message is traced in LangSmith (keys come from the .env file)

Run with:  streamlit run streamlit_app.py
"""

import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

# Load LangSmith keys from .env (tracing turns on automatically)
load_dotenv()

# ---------- Page setup ----------
st.set_page_config(page_title="Ollama Chatbot", page_icon="🤖")
st.title("🤖 Ollama Chatbot")
st.caption("Local LLM with Ollama + LangChain, tracked in LangSmith")

# ---------- Sidebar ----------
with st.sidebar:
    st.header("Settings")
    model_name = st.text_input("Ollama model", value="gemma3:1b")
    st.caption("Examples: gemma3:1b, llama3, mistral")
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

# ---------- Chat history ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- Handle new message ----------
user_input = st.chat_input("Type your message...")

if user_input:
    # Show and save the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Build a simple prompt that includes the earlier conversation
    history = ""
    for m in st.session_state.messages:
        speaker = "User" if m["role"] == "user" else "Assistant"
        history += f"{speaker}: {m['content']}\n"
    history += "Assistant:"

    # Get the reply from Ollama (streamed word by word)
    with st.chat_message("assistant"):
        try:
            llm = OllamaLLM(model=model_name)
            reply = st.write_stream(llm.stream(history))
        except Exception as e:
            reply = (
                "Could not reach Ollama. Make sure it is running "
                f"(`ollama serve`) and the model is pulled.\n\nError: {e}"
            )
            st.error(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})