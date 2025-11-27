# How to Deploy a Streamlit Chatbot (GitHub + Streamlit Cloud Only)

This guide shows you how to go from **nothing** to a **deployed Streamlit chatbot**  
using only:

- GitHub (in the browser – no local Git)
- Streamlit Community Cloud
- OpenAI API key (for the chatbot)

No terminal, no venv, no pushing from your laptop.

---

## 1. Prerequisites

You need:

1. **GitHub account**
   - Sign up at: https://github.com

2. **Streamlit Community Cloud account**
   - Go to: https://streamlit.io/cloud
   - Sign in with GitHub.

3. **OpenAI API key**
   - Go to: https://platform.openai.com
   - Create an account / log in.
   - Go to **API Keys**, create a key, and copy it.
   - Keep it safe. We will paste it into Streamlit **Secrets**, not into code.

---

## 2. Create a New GitHub Repo (in the Browser)

1. Go to https://github.com
2. Click **“+” → New repository** (top-right).
3. Repo name (example): `week03_streamlit_chatbot`
4. Visibility: **Public** or **Private** (both work with Streamlit Cloud).
5. DO NOT tick “Add README” (optional – doesn’t matter much).
6. Click **“Create repository”**.

You now have an empty repo page.

---

## 3. Add `app.py` (Chatbot Code) via GitHub Web Editor

1. In the new repo page, click **“Add file” → “Create new file”**.
2. File name: `app.py`
3. Paste this code:

   ```python
   import streamlit as st
   from openai import OpenAI

   st.set_page_config(page_title="Embedded AI TA Chatbot", page_icon="🤖")

   st.title("Embedded AI & Robotics TA Chatbot 🤖")
   st.write("Ask anything about Arduino, sensors, motors, or tiny AI models!")

   # Get API key from Streamlit secrets (we will set this on Streamlit Cloud)
   api_key = st.secrets.get("OPENAI_API_KEY", None)
   if api_key is None:
       st.error("OPENAI_API_KEY is not set. Please add it in Streamlit Cloud → Settings → Secrets.")
       st.stop()

   client = OpenAI(api_key=api_key)

   # Initialise chat history
   if "messages" not in st.session_state:
       st.session_state["messages"] = [
           {
               "role": "system",
               "content": (
                   "You are a friendly teaching assistant for an Embedded AI & Robotics lab. "
                   "Explain things simply for first-year data science students."
               ),
           }
       ]

   # Display previous messages
   for msg in st.session_state["messages"]:
       if msg["role"] == "user":
           with st.chat_message("user"):
               st.markdown(msg["content"])
       elif msg["role"] == "assistant":
           with st.chat_message("assistant"):
               st.markdown(msg["content"])

   # Chat input
   user_input = st.chat_input("Type your question here…")

   if user_input:
       # Add user message
       st.session_state["messages"].append({"role": "user", "content": user_input})

       # Show user message
       with st.chat_message("user"):
           st.markdown(user_input)

       # Call OpenAI
       with st.chat_message("assistant"):
           with st.spinner("Thinking…"):
               response = client.chat.completions.create(
                   model="gpt-4.1-mini",
                   messages=st.session_state["messages"],
               )
               reply = response.choices[0].message.content
               st.markdown(reply)

       # Save assistant reply
       st.session_state["messages"].append({"role": "assistant", "content": reply})```

##Scroll down and click “Commit new file”.

##4. Add requirements.txt via GitHub Web Editor
Back on the repo page, click “Add file” → “Create new file”.
File name: requirements.txt
Paste:
streamlit
openai
##Click “Commit new file”.
Your repo now has at least:
app.py
requirements.txt
##5. Deploy on Streamlit Community Cloud
Go to: https://streamlit.io/cloud
Log in with GitHub.
Click “New app”.
Under “Select a repo”, choose your repo:
Repo: your-username/week03_streamlit_chatbot
Branch: main (or master, whatever GitHub shows)
Main file: app.py
Click “Deploy”.
Streamlit Cloud will:
Install packages from requirements.txt
Run app.py
Open a URL like: https://week03_streamlit_chatbot-yourname.streamlit.app
You will see an error about OPENAI_API_KEY (expected). Now we fix it.
##6. Add the OpenAI API Key in Streamlit Settings → Secrets
In your deployed Streamlit app, click the “⋮” (three dots) in the top-right.
Click “Settings” → then “Secrets”
(or from the app dashboard: “Manage app” → “Secrets”).
In the Secrets editor, add this line:
OPENAI_API_KEY = "sk-...your-real-key-here..."
Click “Save”.
The app will automatically restart.
Now:
st.secrets["OPENAI_API_KEY"] is available inside app.py.
Your chatbot should start responding.
