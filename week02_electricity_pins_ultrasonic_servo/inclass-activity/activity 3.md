# Reading an Ultrasonic Sensor on the Serial Monitor

This guide shows you how to **connect an HC-SR04 ultrasonic sensor** to your Arduino and  
**read the distance in centimeters** on the **Serial Monitor**.

---

## 1. What You Need

- Arduino Uno (or compatible)  
- USB cable  
- 1 × Ultrasonic sensor (HC-SR04 or similar)  
- Breadboard (optional, but useful)  
- Jumper wires

---

## 2. Pinout – HC-SR04 Ultrasonic Sensor

The HC-SR04 typically has **4 pins** labeled:

- **VCC** – Power (5V)  
- **Trig** – Trigger input (from Arduino)  
- **Echo** – Echo output (to Arduino)  
- **GND** – Ground

---

## 3. Wiring – Ultrasonic → Arduino

Connect the sensor to the Arduino as follows:

- **VCC** → `5V`  
- **GND** → `GND`  
- **TRIG** → digital pin `9`  
- **ECHO** → digital pin `10`

Text diagram:

text
HC-SR04       Arduino
----------------------
VCC      →   5V
GND      →   GND
TRIG     →   D9
ECHO     →   D10


Example Code – Ultrasonic Distance Reader
Create a new sketch and save it as:

```
// Simple Ultrasonic Distance Reader (prints to Serial Monitor)

// Pin definitions
const int TRIG_PIN = 9;
const int ECHO_PIN = 10;

void setup() {
  Serial.begin(9600);        // Open serial at 9600 baud
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

long readDistanceCM() {
  // Make sure trigger is LOW
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  // Send 10µs HIGH pulse on TRIG
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Measure the length of the echo pulse
  long duration = pulseIn(ECHO_PIN, HIGH);  // in microseconds

  // Convert time to distance (speed of sound ~343 m/s)
  long distanceCm = duration * 0.0343 / 2;

  return distanceCm;
}

void loop() {
  long distance = readDistanceCM();

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(200); // read ~5 times per second
}
```

5. Running the Demo
Wire the sensor as in Section 3.
Connect the Arduino to your laptop with the USB cable.
Open Arduino IDE.
Select your board and port:
Tools → Board → Arduino Uno (or your board)
Tools → Port → port that shows your Arduino (if available)
Paste the code from Section 4 into the editor.
Click ✔ (Verify), then → (Upload).
Open the Serial Monitor:
Tools → Serial Monitor
Set baud rate to 9600 (bottom-right corner)
