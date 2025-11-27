# Week 3 – Streamlit Chatbot & Web-Controlled Robot (Concept Stage)

This week we shift from **microcontrollers only** to **microcontrollers + web apps**.

You will:

- Learn the basics of **Streamlit** (quick Python web apps).
- Use the **OpenAI API** to build a **simple chatbot UI**.
- Learn what a **Flask server** is and why we need a “backend”.
- Set up a **small Flask API** that can receive **movement commands** for a future Arduino-powered vehicle.
- Start thinking about the architecture for a **remote-controlled motor vehicle** using Arduino Uno WiFi + Streamlit.

> ⚠️ In Week 3 we focus on the **software side** (Streamlit + Flask + APIs).  
> Actual **Arduino motor driving** will be wired in this class.

---

## 1. Big Picture – Architecture

We are now moving from:

> Laptop ↔ Arduino (USB)

to:

> Browser (students) → **Streamlit app** → **Flask server** → Arduino Uno WiFi (future integration)

Three key pieces:

1. **Streamlit (frontend)**  
   - Python library to build web UIs with very little code.  
   - Runs on your laptop, you open it in your browser.

2. **Flask (backend API)**  
   - Python micro web framework.  
   - Exposes HTTP routes like `/move` where we can POST JSON commands.

3. **Arduino Uno WiFi (robot side – later)**  
   - Receives commands (e.g. over Serial or WiFi) and drives motors.  
   - For now, we just **print** commands on the server to prove it works.

---

## 2. Before You Start

### 2.1 Software Requirements

- Python 3.10+  
- Arduino IDE (from previous weeks)  
- A code editor (VS Code / PyCharm / etc.)

### 2.2 Recommended Python Setup (per group)

In a terminal:

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate    # Windows PowerShell

# Install required Python packages
pip install streamlit flask openai requests
