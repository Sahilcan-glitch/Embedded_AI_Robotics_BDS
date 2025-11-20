# Week 2 – Electricity Basics, Arduino Pins & Distance → Movement

Welcome to Week 2 of **Embedded AI & Robotics for Data Scientists**.

In Week 1, you:

- Installed Arduino IDE
- Connected the board
- Blinked an LED
- Used a button as input and an LED as output

You saw your **code** controlling the **real world**.

This week, we will:

1. Fix the **electrical confusion** (voltage, current, resistance, GND)
2. Understand **Arduino pin types** (digital, PWM, analog, RX/TX, SDA/SCL)
3. Build three activities:
   - Activity 1 (with Sahil): LED + resistor + PWM fade
   - Activity 2 (your group): Ultrasonic distance reader
   - Activity 3 (your group): Ultrasonic + servo (distance → movement)

---

## 1. Concepts You Must Know

### 1.1 Voltage, Current, Resistance

We use a **water analogy**:

- **Voltage (V)** – the **push** behind the electrons  
  → like water pressure in a pipe

- **Current (A)** – the **flow** of electrons  
  → like how much water is moving

- **Resistance (Ω)** – how much the path **resists** the flow  
  → like a narrow or wide pipe

In our Arduino world:

- The **5V pin** gives a safe, low voltage
- Components (LEDs, sensors, motors) need the **right current**
- **Resistors** are used to limit current and protect parts

---

### 1.2 What Is a Circuit?

A **circuit** is a **closed loop** that current can flow through:

```text
5V → resistor → LED → GND
