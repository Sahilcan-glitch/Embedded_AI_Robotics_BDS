
---

## 2) `how_to_flask.md` – Simple Flask API reachable on the network

```markdown
# How to Flask – Simple API for Robot Commands (Network-Ready)

This guide shows you how to create a **small Flask API** that:

- Runs on your laptop,
- Listens on the **network** (not just `localhost`),
- Accepts movement commands like `"forward"` / `"left"` / `"stop"`.

Later, your **Streamlit app** or other devices can send HTTP requests to this server.

---

## 1. Requirements

On the laptop running the server:

- Python 3.10+ installed  
- Internet / Wi-Fi connection  
- Ability to install Python packages

In your group, designate **one laptop** as the “Flask server machine”.

---

## 2. Install Flask

Open a terminal / command prompt on the server machine:

```bash
pip install flask
