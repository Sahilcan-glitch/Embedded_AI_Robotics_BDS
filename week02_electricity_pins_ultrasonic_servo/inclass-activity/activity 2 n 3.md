# Ultrasonic Motion Demos – Activity 2 & 3

This folder contains two **hands-on demo activities** that extend your basic Arduino skills:

- **Activity 2:** Ultrasonic sensor + **servo motor** (distance → angle)  
- **Activity 3:** Ultrasonic sensor + **DC motor with transistor** (distance → speed)

Both activities show a complete **Sense → Think → Act** loop:

- **Sense** – Ultrasonic sensor measures distance  
- **Think** – Arduino code decides how to respond  
- **Act** – Servo or DC motor moves/changes speed  

These instructions are written so you can follow them step-by-step in lab or at home.

---

## 0. Prerequisites

Before starting:

- You have installed **Arduino IDE** and can upload sketches.
- You have successfully run the **Blink** example on your Arduino.
- You know how to:
  - Open the **Serial Monitor**
  - Select the correct **Board** and **Port**

If not, go back to **Week 1 – Intro + Your First Arduino** and finish that first.

---

## 1. Parts List

For **Activity 2 (Ultrasonic + Servo)**:

- 1 × Arduino Uno (or compatible)
- 1 × USB cable
- 1 × Ultrasonic sensor (HC-SR04 or similar)
- 1 × Small servo motor (e.g. SG90)
- Breadboard + jumper wires

For **Activity 3 (Ultrasonic + DC Motor + Transistor)**:

- Everything from Activity 2, plus:
- 1 × Small DC motor (5V hobby motor / fan)
- 1 × NPN transistor (e.g. 2N2222, BC547, etc.)
- 1 × Diode (e.g. 1N4007) – flyback protection
- 1 × Resistor for transistor base (e.g. 1 kΩ)
- Optional: separate 5–9V supply for the motor (if bigger)

> ⚠️ **Important:** If you use a separate supply for the motor,  
> you **must** connect the supply GND to Arduino GND.

Suggested pin plan:

- Ultrasonic:
  - TRIG → pin **9**
  - ECHO → pin **10**
- Servo:
  - Signal → pin **3**
- DC motor driver:
  - Transistor control → pin **5** (PWM pin)

---

## 2. Activity 2 – Ultrasonic Sensor + Servo (Distance → Angle)

In this activity, you will:

- Read distance from an **ultrasonic sensor**
- Map that distance to a **servo angle**
- Watch the servo move as your hand moves

### 2.1 Wiring – Ultrasonic Sensor

Connect the **HC-SR04** ultrasonic sensor to the Arduino:

- **VCC** → `5V`
- **GND** → `GND`
- **TRIG** → `D9`
- **ECHO** → `D10`

Double-check:

- VCC really goes to **5V** (not 3.3V)
- GND is connected to **Arduino GND**

### 2.2 Wiring – Servo Motor

Connect the servo (typical colour scheme):

- Servo **Red** → `5V`
- Servo **Brown/Black** → `GND`
- Servo **Orange/Yellow (signal)** → `D3`

> ✅ Make sure **GND** of the servo **and** sensor are connected to **Arduino GND**.  
> All grounds must be common, or the signal will behave strangely.

### 2.3 Code – Ultrasonic + Servo Demo

Create a new sketch and save it as:

> `activity02_ultrasonic_servo.ino`

Paste this code:

```cpp
#include <Servo.h>

// Pins
const int TRIG_PIN  = 9;
const int ECHO_PIN  = 10;
const int SERVO_PIN = 3;

Servo myServo;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  myServo.attach(SERVO_PIN);
  myServo.write(90); // start in the middle
}

// Read distance in cm from ultrasonic sensor
long readDistanceCM() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH); // microseconds
  long distanceCm = duration * 0.0343 / 2; // sound speed conversion
  return distanceCm;
}

void loop() {
  long distance = readDistanceCM();

  // Clamp distance to a useful range (e.g. 5–50 cm)
  if (distance < 5)  distance = 5;
  if (distance > 50) distance = 50;

  // Map distance (5–50 cm) to servo angle (0–180°)
  int angle = map(distance, 5, 50, 0, 180);
  myServo.write(angle);

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm | Servo angle: ");
  Serial.println(angle);

  delay(100);
}
