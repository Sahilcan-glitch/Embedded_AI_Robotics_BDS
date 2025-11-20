# Connecting & Testing a Servo Motor (Step-by-Step)

This guide will help you **connect a servo motor to your Arduino** and test it using the built-in **Servo → Sweep** example.

---

## 1. What You Need

- Arduino Uno (or compatible)  
- USB cable  
- 1 × small servo motor (e.g. SG90)  
- Breadboard (optional but helpful)  
- A few jumper wires (male–male or male–female depending on your servo)

Typical servo wire colours:

- **Red**   → +5V (power)  
- **Brown/Black** → GND (ground)  
- **Orange/Yellow/White** → Signal (control)

---

## 2. Identify Servo Wires

Look at your servo cable:

- Find the **Red** wire → this is **VCC (5V)**  
- Find the **Brown/Black** wire → this is **GND**  
- The remaining wire (often **Orange/Yellow/White**) → **Signal**

> ✅ If you’re not sure, you can later search the exact servo model – but for most SG90-style servos, this colour scheme is correct.

---

## 3. Wiring the Servo to Arduino

> ⚠️ For safety, do the wiring **before** plugging the Arduino into USB.

1. Place the servo near your Arduino (tape it to the table if it wiggles).
2. Connect the **Red (VCC)** wire:
   - Servo **Red** → Arduino **5V** pin
3. Connect the **Brown/Black (GND)** wire:
   - Servo **Brown/Black** → Arduino **GND** pin
4. Connect the **Signal** wire:
   - Servo **Orange/Yellow/White** → Arduino **Digital pin 3** (PWM-capable)

Your final wiring should be:

text
Servo Red    → 5V
Servo Brown  → GND
Servo Signal → D3



```
#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(3);  // attaches the servo on pin 3 to the servo object
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) {
    myservo.write(pos);
    delay(15);
  }
  for (pos = 180; pos >= 0; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
}
```
