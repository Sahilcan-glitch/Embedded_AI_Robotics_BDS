# Cloud Flask Class Server – Step-by-Step Guide 🧠🌐

This repository contains a **single Flask backend** that all student groups can use **at the same time** for different projects:

- Fall detection alerts  
- Student counter + humidity  
- Balancing robot status  

The goal is to **feel like a real internet backend** but still stay simple enough for beginners.

---

## 1. Big Picture – What Are We Doing & Why?

### 🧩 What is this?

- A **small Python web server** (Flask) deployed to the **cloud** (e.g. Render).
- It exposes simple **HTTP endpoints**:
  - `POST /log` → send (log) data
  - `GET /log` → read all data
  - `GET /log/<group_id>` → read data for one group

### 🎯 Why are we doing this?

1. To show how **IoT / robotics** projects send data over the **internet** (not just serial).
2. To give students a **shared backend** they can log to from:
   - Arduino / ESP32
   - Python scripts
   - Google Colab
   - Streamlit dashboards
3. To teach the idea of:
   > “Many clients, one server, shared API, data separated by IDs/project names.”

### 🏫 How does one server handle 3 projects?

- Every log entry includes:
  - `group_id` → which team
  - `project` → what project (e.g. `"fall_detection"`, `"student_counter"`, `"balancing_robot"`)
  - `value` → the key reading
  - `note` → human-readable comment
- The server doesn’t care *which* project → it just stores JSON.
- Later we **filter** by `group_id` or `project`.

Think of it as **one big whiteboard** in the cloud.  
All groups write on it, but we label every line with group and project.

---

## 2. Prerequisites

You (the instructor) need:

1. **GitHub account**  
   - Sign up at: https://github.com

2. **Render account** (for hosting)  
   - Sign up at: https://render.com  
   - Log in with GitHub (easiest).

3. **Python installed (optional, for local testing)**  
   - Python 3.x on your laptop (Mac/Windows/Linux).

Students need:

- Ability to run **Python** (VS Code / terminal / Colab) or **ESP32 / Arduino** code that can send HTTP requests.

---



## 3. Step-by-Step: Deploy to Render

Why Render?

It gives you a public HTTPS URL so students anywhere (home, lab, Colab, IoT devices) can send data.

Go to: https://render.com

Log in with GitHub.

Click New → Web Service.

Choose the cloud_flask_class_server repository.

Set the service settings:

Build Command:

pip install -r requirements.txt

Tells Render how to install dependencies.

Start Command:

gunicorn app:app

gunicorn is a production WSGI server that runs your Flask app.

Environment: Python 3

Instance Type: Free

Click Create Web Service and wait for the deployment to finish.

Render will give you a URL like:


https://cloud-flask-class-server.onrender.com
This is your BASE_URL.
