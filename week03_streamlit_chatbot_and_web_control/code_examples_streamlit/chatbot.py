import streamlit as st
from openai import OpenAI

# Get API key from Streamlit secrets or environment
api_key = st.secrets.get("OPENAI_API_KEY", None)

if api_key is None:
    st.error("OPENAI_API_KEY is not set in .streamlit/secrets.toml")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("Week 3 – Simple Chatbot 💬")
st.write("This is a minimal chatbot using the OpenAI API and Streamlit.")

# Keep chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a friendly TA for Embedded AI & Robotics students."}
    ]

# Show previous messages (user + assistant)
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask something about Arduino, sensors, or AI:")

if user_input:
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call OpenAI API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=st.session_state["messages"],
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    # Add assistant message to history
    st.session_state["messages"].append({"role": "assistant", "content": reply})
