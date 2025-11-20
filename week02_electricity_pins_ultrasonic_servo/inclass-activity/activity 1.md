# 💡 Week 2 – In-Class Activities

This file is for **live, in-class demos**.
Each section is a separate mini-activity – you don’t need all of them wired at once.

---

## 1. LED Controlled by PWM (Fade Demo)

This activity demonstrates **Pulse Width Modulation (PWM)** using `analogWrite()` to smoothly fade an LED on and off.

### 1.1 Components

* 1 × **Arduino Uno** (or compatible)
* 1 × **LED** (any color)
* 1 × **220Ω resistor**
* **Breadboard**
* **Jumper wires**

### 1.2 Wiring (LED + Resistor on PWM Pin)



Follow these connections carefully:

* Arduino **pin 9** (a PWM pin) $\rightarrow$ **220$\Omega$ resistor** $\rightarrow$ LED **long leg** (**anode**)
* LED **short leg** (**cathode**) $\rightarrow$ **GND**

**⚡ Check:**
* There is **exactly one resistor in series** with the LED to limit current.
* The LED's ground connection returns to an Arduino **GND** pin.

---

### 1.3 Code – LED Fade with `analogWrite()`

```cpp
/*
 * LED Fade Demo using analogWrite()
 *
 * This code sweeps a PWM value from 0 (off) to 255 (full brightness)
 * and back, creating a smooth fading effect. Pin 9 is used as it
 * supports hardware PWM on the Arduino Uno.
 */

const int LED_PIN = 9; // Define the pin connected to the LED/Resistor

void setup() {
  // Set the LED pin as an OUTPUT
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // 1. Fade UP: from 0 (off) to 255 (full on)
  for (int value = 0; value <= 255; value++) {
    analogWrite(LED_PIN, value); // Output the PWM value
    delay(10);                   // Pause for 10ms to control the speed of the fade
  }

  // 2. Fade DOWN: from 255 (full on) to 0 (off)
  for (int value = 255; value >= 0; value--) {
    analogWrite(LED_PIN, value); // Output the PWM value
    delay(10);                   // Pause for 10ms
  }
}
