---
### `tasks.md`

```markdown
# Week 3 – Tasks (Submit by: TBA)

All work is **group-based**.

> You can reuse and adapt the code from `code_examples/`,  
> but your final submissions should show **your own changes** (e.g. prompts, UI text, comments).

---

## Task 1 – Streamlit Chatbot 

Build a **simple conversational chatbot** using:

- **Streamlit** (frontend)
- **OpenAI API** (backend)

### Requirements

- App written in Python using **Streamlit**.
- Uses the **OpenAI Chat API** to generate responses.
- Has:
  - A title (e.g. “health Chatbot”).
  - A text input or chat input for the **user message**.
  - Displays both **user messages** and **assistant replies**.
- Uses a **system prompt** that makes the bot act like a helpful for:
  -  basics
  -  knowlegde
  - Simple  questions (high-level, friendly).

### File naming (suggested)

- Code file: `week03_task1_streamlit_chatbot.py`  
  (or use `app.py` inside a folder `week03_task1_chatbot/`)

### What to submit

- The `.py` file (or folder) in your group repo.
- 1–2 **screenshots** of the chatbot running in your browser.
- A short **reflection (3–5 sentences)** in a `REFLECTION.md` or at the bottom of your task file:
  - What was easy / hard about using Streamlit + OpenAI?
  - One thing you would improve if you had more time.

---

## Task 2 – Flask Server + Streamlit Vehicle Control Panel

Set up a working **client–server prototype** for a future remote vehicle.

- **Flask** = backend API (receives commands).
- **Streamlit** = frontend control panel (sends commands).

### Part A – Flask Server

- Create a Flask app with at least:
  - `POST /move` endpoint:
    - Accepts JSON: `{"direction": "...", "speed": 0–10}`
    - Prints the command on the server console.
    - Returns JSON `{"status": "ok", ...}`.
  - `GET /ping` endpoint (optional but recommended):
    - Returns something like `{"status": "alive"}`.

### Part B – Streamlit Control Panel

- Create a Streamlit app with:
  - A **slider** for speed (0–255).
  - Buttons for:
    - Forward
    - Backward
    - Left
    - Right
    - Stop
  - When a button is pressed:
    - The app sends a POST request to `/move` on your Flask server.
    - Shows success/error messages in the UI.

> For now, the Flask server is allowed to just `print()` the command.  
> In future weeks we will connect this to Arduino Uno WiFi.

### File naming (suggested)

- Flask app: `week03_task2_flask_server.py`  
- Streamlit app: `week03_task2_streamlit_control.py`

### What to submit

- The `.py` files for both:
  - Flask server
  - Streamlit control panel
- 1–2 screenshots:
  - Streamlit control panel in the browser.
  - Flask terminal showing commands received (forward/back/etc.).
- A short **reflection (5–7 sentences)**:
  - Describe the architecture in your own words:
    - Who is the client? Who is the server?
    - Where would the Arduino vehicle fit in?
  - Describe one bug you hit and how you fixed it.

---

## Optional Bonus – Small Integration Step (Not Required but Cool 😎)

If your group is fast and adventurous, you can attempt:

- From the Flask server, send simple text commands over **Serial** to an Arduino (e.g. `"F\n"`, `"B\n"`, `"L\n"`, `"R\n"`, `"S\n"`).
- On the Arduino side, read these commands and just blink an LED differently.

This is **not graded** for Week 3, but you can show it in class if it works.
