# **Final Projects – Embedded AI & Robotics (BDS)**

Each group will build **one end-to-end project** that connects:

* **Arduino / MCU at the edge** →  
* **Backend API deployed on Render** (Flask) →  
* **Streamlit app** (UI / dashboard / control panel)

You will choose **one** of these three project themes:

1. **Fall Detection Alert System**  
   * *Concept:* Use an accelerometer/gyroscope on the MCU to detect a sudden change in orientation (a "fall") and immediately trigger an alert message sent via the API.  
2. **Smart Classroom Entry/Exit Counter \+ Temperature Dashboard**  
   * *Concept:* Use a sensor (e.g., PIR, ultrasonic, or thermal camera) to count people entering and exiting a defined space. Periodically send the current count and ambient temperature data to the API.  
3. **4WD Robot Car Controlled Over the Internet**  
   * *Concept:* Use the Streamlit UI to send commands (Forward, Back, Turn) to the Flask API. The MCU receives these commands via the API and controls the 4WD motor drivers accordingly.

## **✅ Mandatory Requirements**

All three projects **must** adhere to the following technical requirements:

| Requirement | Details |
| :---- | :---- |
| **Real Hardware** | Must use a physical microcontroller (e.g., Arduino, ESP32, Uno WiFi, etc.). |
| **Data Communication** | Send and receive data via **HTTP** to a **backend on Render**. |
| **Frontend** | Must have a **Streamlit front-end** (local or Streamlit Cloud) talking to that backend. |
| **Documentation** | The GitHub repository must be fully documented, including: |
|  | \- Complete source code |
|  | \- Detailed wiring diagrams |
|  | \- Comprehensive README |
|  | \- Link to a short demonstration video |

## **⚙️ 1\. Common Architecture (for ALL Projects)**

No matter which project you pick, the high-level architecture is:  
Hardware (Arduino / ESP32 / Uno WiFi)  
     ↕ (Serial / Wi-Fi)  
Backend API (Flask) – deployed on Render  
     ↕ (HTTP \+ JSON)  
Streamlit App – UI / dashboard / control panel  
     ↕ (Browser)  
You / Users

### **Communication Flow Breakdown:**

1. **Hardware ↔ Backend:** The MCU connects to the local network (Wi-Fi) to send sensor data (e.g., fall status, temperature, count) or receive control commands via HTTP requests.  
2. **Backend ↔ Frontend:** The Flask API serves as the central data hub, handling data persistence (if required) and providing RESTful endpoints for the Streamlit application to fetch data (dashboard display) or post commands (control panel).  
3. **Frontend ↔ Users:** The Streamlit app provides the interactive, user-friendly interface for monitoring, visualization, and sending control inputs.

### **1.1 Minimum Tech Stack**

| Component | Stack | Details |
| :---- | :---- | :---- |
| **Hardware** | Arduino Uno / Uno WiFi / Nano / ESP32 | Use assigned hardware. Includes sensors & actuators depending on the project. |
| **Backend** | Python Flask app | Deployed as a **Web Service on Render.com**. |
| **Frontend** | Streamlit app | Can be local or Streamlit Cloud. Displays data and/or sends commands. |

**Backend API Minimum Endpoints:**

* GET /ping – health check  
* POST /data or POST /event – to receive data from the Arduino  
* *Optional:* POST /command – to receive commands from Streamlit for the Arduino (e.g., for the car project)

## **2\. Render Backend – What It Should Do**

Each group’s Flask backend (deployed on Render) should:

1. **Expose clear REST endpoints** (See project-specific examples below):  
   * Example: POST /data/fall, POST /data/classroom, POST /command/move  
2. **Store recent data** in **memory** (Python list/dict) or in a simple database (optional).  
3. **Provide GET endpoints** for the Streamlit app to retrieve data:  
   * e.g. GET /data/latest or GET /data/history  
* *Optional but nice:* Basic error handling and API key/token checks from devices.  
* *Note:* You do not have to build a huge database – the focus is on the **end-to-end pipeline**.

## **3\. Project Option 1 – Fall Detection Alert System**

### **3.1 Story**

You are building a **wearable fall detection device** (e.g. for elderly people). When a strong fall-like motion is detected, the Arduino flags a “fall event” and sends it via Wi-Fi / serial → backend → Streamlit. Streamlit shows an **alert** and logs the event.

### **3.2 Suggested Hardware**

* 1 × Arduino (Uno WiFi or ESP32 preferred)  
* 1 × Accelerometer module (e.g. MPU6050 / MPU-6050 / similar)  
* 1 × LED or buzzer for local feedback (optional)  
* USB cable, jumper wires

### **3.3 Responsibilities**

#### **Arduino side (edge device):**

* Read acceleration data from the **accelerometer**.  
* Implement **very simple rule-based fall detection**, for example:  
  * Compute magnitude of acceleration vector.  
  * If acceleration spike \> threshold (e.g. \> 2.5–3 *g*) AND maybe a following near-zero movement period → classify as “fall”.  
* When a fall is detected:  
  * Blink LED / buzzer locally (optional).  
  * Send an HTTP request (if Wi-Fi board) **OR** send a serial message to a small companion script that forwards to backend.

#### **Backend (Flask on Render):**

* **Endpoint:** POST /data/fall  
* **JSON body like:**  
  {  
    "device\_id": "belt-1",  
    "timestamp": "...",  
    "is\_fall": true,  
    "ax": 1.2, "ay": \-9.8, "az": 0.5  
  }

* Save this event to an in-memory list.  
* **Endpoint:** GET /data/fall/latest (Returns the latest event.)  
* **Endpoint:** GET /data/fall/history (Returns recent events, e.g. last 50.)

#### **Streamlit (UI):**

* Polls backend (e.g. every few seconds) to show:  
  * Latest status: **“OK”** or **“FALL DETECTED”**  
  * History table of last events.  
* **Visuals:**  
  * Big red card if the latest event is a fall.  
  * Chart of recent acceleration or a bar of fall counts per day.

### **3.4 High-Level “How To” with Arduino**

1. Wire accelerometer to Arduino (e.g. I²C: SDA/SCL \+ 5V/GND).  
2. Use a known library (e.g. MPU6050 or Wire) to read acceleration.  
3. Compute a\_mag \= sqrt(ax\*ax \+ ay\*ay \+ az\*az).  
4. If a\_mag exceeds threshold → mark as fallDetected \= true.  
5. **Send Data:**  
   * Use Arduino’s Wi-Fi library to POST to backend, **OR**  
   * Send text over Serial (e.g. "FALL\\n" and maybe the values) to a **Python script** on a laptop that then POSTs to Render.

## **4\. Project Option 2 – Smart Classroom Entry/Exit Counter \+ Temperature**

### **4.1 Story**

You are building a **smart classroom monitor** that: counts how many students enter and exit the room, tracks current occupancy, measures temperature/humidity, and displays everything on a **Streamlit dashboard** (charts, stats).

### **4.2 Suggested Hardware**

* 1 × Arduino (Uno / Uno WiFi / ESP32)  
* 2 × distance sensors (ultrasonic or IR break-beam) placed at the door  
* 1 × temperature/humidity sensor (e.g. DHT11 / DHT22)  
* *Optional:* LEDs to show room “too hot” or “crowded”

### **4.3 Responsibilities**

#### **Arduino (door \+ climate sensor):**

* Use two **entry/exit sensors** (S1, S2) at the door to determine direction:  
  * If S1 triggers then S2 → person enters (current\_count++).  
  * If S2 triggers then S1 → person exits (current\_count--, but not below zero).  
* Maintain current\_count, total\_entered, and total\_exited.  
* Read temperature (and optionally humidity) from sensor.  
* Periodically send a **data packet** (e.g. every 5–10 seconds) to the backend:  
  {  
    "room\_id": "lab-1",  
    "timestamp": "...",  
    "current\_count": 23,  
    "temp\_c": 24.5,  
    "humidity": 40.0  
  }

#### **Backend (Flask on Render):**

* **Endpoint:** POST /data/classroom (Receives data packets.)  
* Stores data in memory (list, or dict by room\_id).  
* **Endpoint:** GET /data/classroom/latest?room\_id=lab-1  
* **Endpoint:** GET /data/classroom/history?room\_id=lab-1 (Optional: allow query parameters like ?limit=50.)

#### **Streamlit Dashboard:**

* Shows:  
  * Current occupancy as big number.  
  * Graphs of occupancy over time.  
  * Temperature graph / gauge.  
* *Optional analytics:* Peak occupancy in last X minutes, "too crowded" or "too hot" warnings.

### **4.4 High-Level “How To” with Arduino**

1. Place sensors at the door (S1 at outer side, S2 at inner side).  
2. For each crossing, listen for the order in which S1 and S2 trigger to increment/decrement current\_count.  
3. Ensure basic debouncing / threshold so it doesn’t double count.  
4. Read temperature sensor (e.g. DHT library).  
5. Every X seconds: Construct a small JSON string and **send data via Wi-Fi to backend**, or over Serial to a **Python forwarder** script.

## **5\. Project Option 3 – 4-Motor Car Controlled Over Internet**

### **5.1 Story**

You are building a **4WD robot car** that can be driven from anywhere (within network constraints) using a web control panel (Streamlit), a backend (Flask on Render), and a 4-wheel car with motors driven by Arduino \+ L298N.

### **5.2 Suggested Hardware**

* 1 × 4WD robot chassis (4 DC gear motors)  
* 1 × L298N motor driver  
* 1 × Arduino (Uno / Uno WiFi / ESP32)  
* 1 × battery pack for motors  
* Jumper wires

### **5.3 Responsibilities**

#### **Arduino (motor controller):**

* Wire the 4 motors as **left side** and **right side** groups.  
* Use L298N with pins like: ENA (PWM), IN1, IN2 and ENB (PWM), IN3, IN4.  
* Implement Serial protocol to receive single-character commands:  
  * F → move forward  
  * B → move backward  
  * L → turn left  
  * R → turn right  
  * S → stop

#### **Backend (Flask on Render):**

* **Endpoint:** POST /command/move  
* **JSON input:**  
  { "direction": "forward", "speed": 180 }

* **Deployment Note (CRITICAL):** On Render, you **cannot** directly open a serial port to your Arduino.  
  * **Recommended for class:** Run Flask **locally** on one laptop for real motor control, and Streamlit talks to the **local Flask**. You still demonstrate the ability to deploy a placeholder Flask app on Render.  
  * **Hybrid architecture (optional / advanced):** Render backend stores commands, and a small **local agent script** on your laptop polls Render (GET /command/next) and sends the command via Serial to Arduino.

#### **Streamlit Control Panel:**

* Buttons: Forward, Back, Left, Right, Stop.  
* Speed slider (0–255).  
* On button click/slider change: Sends POST /command/move to backend (local or Render).  
* Shows: Status messages and optional log of last commands.

### **5.4 High-Level “How To” with Arduino**

1. Wire motors and L298N to Arduino as in lab.  
2. Write Arduino sketch to read Serial.read() (or use serialEvent()) and execute motor functions (forward(), backward(), etc.) based on F/B/L/R/S commands.  
3. On laptop: Run Flask locally with the /command/move endpoint, which then sends the received command (F/B/L/R/S) over Serial to the Arduino.  
4. Streamlit buttons call the local Flask endpoint (HTTP).

## **6\. Deliverables (For All Projects)**

Each group must submit:

1. **GitHub repo** containing organized folders:  
   * arduino/ folder with .ino files and wiring diagrams (.md \+ photos).  
   * backend/ folder with Flask app (app.py, requirements.txt).  
   * frontend/ folder with Streamlit app (app.py or main.py, requirements.txt).  
   * PROJECT.md (this file, plus your own notes and decisions).  
2. **README.md** at the root explaining:  
   * Which project you chose.  
   * How to run each part (hardware, backend, frontend).  
3. **Running demo (in class):**  
   * Hardware on the table.  
   * Streamlit open in browser.  
   * Backend running (locally or on Render).  
   * Show the data/control flow live.  
4. **Short video (2–3 minutes):**  
   * Walkthrough of: The problem you solved, the end-to-end pipeline, and a live demo (recording of it working).  
   * Link added to the README.  
5. **Reflection (per group)** – 1–2 pages:  
   * What worked, what was hard.  
   * What you would improve with more time.  
   * How this connects to “AI at the edge” and to data science.

## **7\. How to Choose Your Project**

Choose **Fall Detection** if:

* You like motion sensors and time-series classification.  
* You want to focus on **signal thresholds** and alerting.

Choose **Smart Classroom Counter** if:

* You like IoT dashboards and **analytics**.  
* You want to focus on **data collection, counting logic, charts.**

Choose **4WD Car** if:

* You like **control systems and robotics**.  
* You want to focus on **commands, motor drivers, and interactivity.**

Whatever you choose, the core learning outcome is the same:  
Designing and building an end-to-end embedded AI / IoT system that a data scientist can understand and extend.