# Week 2 – Electricity, Pins, Ultrasonic & Servo

## 1. Goals

By the end of this week, you will:

- Recap Week 1: Blink, button as input, LED as output.
- Understand voltage, current, resistance at a very simple level.
- Understand what a circuit (loop) is and why GND is critical.
- Know why we use resistors with LEDs and where they go.
- Know why we don’t just power everything directly from 5V.
- Recognise the main Arduino pin types (digital, PWM, analog, RX/TX, SDA/SCL).
- Wire and read an ultrasonic distance sensor.
- Use a servo motor and control its angle from a distance reading.

---

## 2. Quick Recap from Week 1

Last week you:

- Plugged in the Arduino.
- Installed the Arduino IDE.
- Uploaded the **Blink** example.
- Used:
  - **Button** as input
  - **LED** as output
- Saw the full chain: **code → board → real world**.

If any of this still feels fuzzy, skim the Week 1 README again before starting.

---

## 3. Before You Start

You will need:

- A laptop (Windows, macOS, or Linux)
- Arduino Uno (or compatible) + USB cable
- Breadboard + jumper wires
- 1 × LED
- 1 × 220Ω resistor
- 1 × ultrasonic distance sensor (HC-SR04 style)
- 1 × small servo motor (e.g. SG90)
- (Optional but helpful) Extra LEDs and resistors

We will follow the path:

> **Electricity basics → Arduino pins → Sensor (ultrasonic) → Actuator (servo)**

---

## 4. Very Simple Electricity

### 4.1 Voltage, Current, Resistance

Think of electricity like water in pipes:

- **Voltage (V)** = *push*  
  Like water pressure in a pipe.

- **Current (A)** = *flow*  
  How much water is actually moving.

- **Resistance (Ω)** = *restriction*  
  A narrow pipe that slows the flow.

In our labs:

- Arduino gives us **5V** and **3.3V**.
- We use **resistors** to limit current.
- LEDs, sensors, and motors all need the **right amount of flow**.
- Too much current → things get hot, burn out, or die.

---

### 4.2 What Is a Circuit (Loop)?

A **circuit** is a closed loop:

- From **+ (5V)**  
- Through components (resistor, LED, sensor, servo…)  
- Back to **GND**

Rules of thumb:

- If the loop is **broken** → no current → nothing happens.
- If the loop is **wrong** → too much current → things can break.

Simplest LED loop:

> **5V → resistor → LED → GND**

Always ask yourself:

> “Where is +5V? Where is GND? How does the loop go around?”

---

### 4.3 Ground (GND) – The Reference

**GND** is our **0 volts reference**.

- All voltages are measured **relative to GND**.
- Every sensor, servo, and module must share **GND** with the Arduino.

If GND is missing:

- Signals **float**
- Things behave **randomly**
- Readings are **wrong**

One of the **top reasons** circuits don’t work is: **no common ground**.

---

### 4.4 LEDs & Resistors – Where and Why?

An LED is **not** a resistor:

- It drops about ~2V and then lets current rush through.
- If you connect: `5V → LED → GND`  
  → too much current, LED can burn, Arduino pin can be stressed.

**Solution: add a resistor in series:**

> 5V or digital pin → resistor → LED → GND

In a **series loop**, the same current flows through all parts, so the resistor can be:

- Before the LED  
  `5V → resistor → LED → GND`
- Or after the LED  
  `5V → LED → resistor → GND`

Both are fine, as long as there is **one resistor in series** with the LED.

---

### 4.5 Why Not Just Use the 5V Pin?

**5V pin:**

- Always ON when the board has power.
- You can’t turn it off in code.

**Digital pins:**

- Controlled by your program.
- Can be **HIGH** (~5V) or **LOW** (0V).
- Can blink, fade (PWM), and react to sensors.

So:

- **5V pin** = dumb, always-on power.
- **Digital pin** = smart, code-controlled power.

We use digital pins when we want **our code** to decide when something turns ON or OFF.

---

## 5. Arduino Pin Overview

### 5.1 Main Pin Types (Arduino Uno)

- **Digital pins (0–13)**  
  - `pinMode(pin, INPUT/OUTPUT)`  
  - `digitalRead(pin)`, `digitalWrite(pin, HIGH/LOW)`

- **PWM pins (~3, ~5, ~6, ~9, ~10, ~11)**  
  - Special digital pins that can do **PWM**  
  - `analogWrite(pin, value)` for brightness/speed (0–255)

- **Analog input pins (A0–A5)**  
  - `analogRead(pin)`  
  - Give values from **0–1023** (voltage level between 0 and 5V)

- **Power pins**  
  - **5V**, **3.3V**, **GND**

---

### 5.2 Special Communication Pins

- **RX (0)** – Receive serial data  
- **TX (1)** – Transmit serial data  

Used for the **Serial Monitor** over USB.  
For basic labs:

- Avoid using **pins 0 and 1** for LEDs/buttons so we don’t break Serial.

**I²C pins:**

- **SDA (data)** → A4  
- **SCL (clock)** → A5  

Used later to talk to **smart sensors/displays** with just 2 wires.

---

## 6. Activity 1 – LED Fade with PWM

We’ll rebuild the LED circuit and use a **PWM pin** to fade it.

### 6.1 Wiring

On your breadboard:

- Pin **9** (PWM) → **220Ω resistor** → LED **long leg** (anode)
- LED **short leg** (cathode) → **GND**

Check:

- There is **exactly one resistor** in series with the LED.
- GND from LED goes back to Arduino GND.

---

### 6.2 Code – LED Fade

```cpp
const int LED_PIN = 9;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // fade up
  for (int v = 0; v <= 255; v++) {
    analogWrite(LED_PIN, v);
    delay(10);
  }

  // fade down
  for (int v = 255; v >= 0; v--) {
    analogWrite(LED_PIN, v);
    delay(10);
  }
}
