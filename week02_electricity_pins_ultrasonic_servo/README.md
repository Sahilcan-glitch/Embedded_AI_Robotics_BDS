# Week 2 – Electricity Basics, Arduino Pins & Distance → Movement

## 1. Goals

By the end of this week, you will:

- Understand basic **electricity concepts**: voltage, current, resistance, and GND.
- Know **where and why** to use a resistor with an LED.
- Understand the main **Arduino pin types** (digital, PWM, analog, RX/TX, SDA/SCL).
- Read distance using an **ultrasonic sensor**.
- Use that distance to control a **servo motor**.
- See the full **Sense → Think → Act** loop in a simple embedded system.

---

## 2. Before You Start

You will need:

- A laptop (Windows, macOS, or Linux)
- Arduino Uno (or compatible) + USB cable
- 1 × LED
- 1 × 220Ω resistor (for LED)
- 1 × Ultrasonic sensor (HC-SR04 or similar)
- 1 × Small servo motor (e.g. SG90)
- Breadboard + jumper wires

You should already have from Week 1:

- Arduino IDE installed
- Your board working with the **Blink** example

---

## 3. Quick Recap (From Week 1)

Last week you:

- Installed the Arduino IDE
- Selected the correct **Board** and **Port**
- Uploaded and modified **Blink**
- Built a simple **button + LED** circuit

Key ideas from Week 1:

- `setup()` runs once, `loop()` runs forever.
- We used a **digital pin** to control an LED instead of connecting it directly to 5V.

---

## 4. Electricity Basics (Very Simple)

### 4.1 Voltage, Current, Resistance

Think of electricity like water in pipes:

- **Voltage (V)** – the **push** (pressure)
- **Current (A)** – the **flow** (how much is moving)
- **Resistance (Ω)** – how much the path **resists** the flow

In this course:

- Arduino gives us **5V** and **3.3V** (safe, low voltages).
- We use **resistors** to limit current so LEDs and pins don’t burn out.

### 4.2 What Is a Circuit?

A circuit is a **closed loop**:

```text
5V → resistor → LED → GND
