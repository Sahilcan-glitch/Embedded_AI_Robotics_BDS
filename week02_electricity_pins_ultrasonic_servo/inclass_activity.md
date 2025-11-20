# Week 2 – In-Class Activities

This file is just for **in-class demos**.  
Each section is a separate mini-activity – you don’t need all of them wired at once.

---

## 1. LED Controlled by PWM (Fade Demo)

### 1.1 Wiring (LED + Resistor on PWM Pin)

Components:

- 1 × LED
- 1 × 220Ω resistor
- Jumper wires
- Breadboard

Connections:

- Arduino **pin 9** → **220Ω resistor** → LED **long leg** (anode)
- LED **short leg** (cathode) → **GND**

Check:

- There is **exactly one** resistor in series with the LED.
- GND from the LED goes to Arduino GND.

### 1.2 Code – LED Fade with `analogWrite()`

```cpp
const int LED_PIN = 9;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // fade up from 0 to 255
  for (int value = 0; value <= 255; value++) {
    analogWrite(LED_PIN, value);  // PWM: 0 = off, 255 = full on
    delay(10);                    // adjust speed of fade
  }

  // fade down from 255 to 0
  for (int value = 255; value >= 0; value--) {
    analogWrite(LED_PIN, value);
    delay(10);
  }
}
