# Week 2 – Tasks (Submit by: 27/Nov)


## Task 1 – LED + Resistor + PWM Fade

- Build a circuit with:
  - 1 × LED
  - 1 × 220Ω resistor
- Wiring:
  - Pin 9 → 220Ω resistor → LED anode (long leg)
  - LED cathode (short leg) → GND
- Write a sketch that:
  - Fades the LED from OFF to full brightness
  - Then fades it back down to OFF
  - Repeats in a smooth loop
- Save as `week02_task1_led_fade_pwm.ino`.

**What to submit:**
- `week02_task1_led_fade_pwm.ino`
- A photo of your LED circuit (clearly showing resistor placement).

---

## Task 2 – Ultrasonic Distance Reader

- Build a circuit with:
  - 1 × Ultrasonic sensor (HC-SR04)
- Wiring:
  - VCC → 5V  
  - GND → GND  
  - TRIG → digital pin 9  
  - ECHO → digital pin 10
- Write a sketch that:
  - Measures distance in centimeters using the ultrasonic sensor
  - Prints `Distance: XX cm` to the Serial Monitor
  - Adds a simple rule:
    - If `distance < 20` cm → print `"TOO CLOSE"`
    - Else → print `"OK"`
- Save as `week02_task2_ultrasonic_reader.ino`.

**What to submit:**
- `week02_task2_ultrasonic_reader.ino`
- A photo of your ultrasonic setup.
- 2–3 sentences reflecting on:
  - What you learned about how the sensor works
  - One issue you faced and how you fixed it.

---

## Task 3 – Ultrasonic + Servo (Distance → Movement)

- Build a circuit with:
  - 1 × Ultrasonic sensor (as in Task 2)
  - 1 × Servo motor
- Wiring (in addition to Task 2):
  - Servo Red → 5V  
  - Servo Brown/Black → GND  
  - Servo Orange/Yellow (signal) → digital pin 3
- Write a sketch that:
  - Reads the distance from the ultrasonic sensor
  - Clamps distance to a useful range (e.g. 5–50 cm)
  - Uses `map()` to convert distance to an angle (0–180°)
  - Moves the servo to that angle
  - Prints both distance and angle to the Serial Monitor
- Save as `week02_task3_ultrasonic_servo.ino`.

**What to submit:**
- `week02_task3_ultrasonic_servo.ino`
- A photo of your full ultrasonic + servo setup  
  (optional: a short video link of it working).
- 3–4 sentences reflecting on:
  - How you chose the distance → angle mapping
  - What was hardest (wiring, code, debugging)
  - How this demonstrates the **Sense → Think → Act** loop.
