# Week 1 – Intro + Your First Arduino

## 1. Goals

By the end of this week, you will:

- Understand what this course is about and how it runs.
- Know the basic idea of a microcontroller vs PC vs cloud.
- Install the Arduino IDE and connect to an Arduino board.
- Upload and modify the classic **Blink** example.
- Build a simple **button + LED** circuit and control it in code.

---

## 2. Before You Start

You will need:

- A laptop (Windows, macOS, or Linux)
- Arduino Uno (or Nano) + USB cable
- 1 × LED
- 1 × 220Ω resistor
- 1 × push button
- Breadboard + jumper wires

### Step 2.1 – Install Arduino IDE

1. Go to the official Arduino IDE download page.
2. Download and install the latest Arduino IDE for your OS.
3. Open the Arduino IDE.

---

## 3. Connect Your Arduino

1. Plug in your Arduino via USB.
2. In the Arduino IDE, go to:
   - **Tools → Board → Arduino AVR Boards → Arduino Uno** (or your board type)
   - **Tools → Port** → select the port that mentions `Arduino` (if available).
3. If you see no port:
   - Try a different USB cable/USB port.
   - Unplug and plug back in.

---

## 4. Your First Program: Blink

1. In Arduino IDE, open:
   - **File → Examples → 01.Basics → Blink**
2. Read the code and try to spot:
   - `setup()` – runs once at the beginning
   - `loop()` – runs again and again forever
3. Click the **Upload** (arrow) button.
   - Wait for “Done uploading”.
4. You should see the built-in LED (usually on pin 13) blinking.

### 4.1 – Experiment with Blink

- Change `delay(1000)` to `delay(200)` – what happens?
- Try a pattern:
  - Short blink, long pause
  - 3 fast blinks, then 1 second off

---

## 5. Button + LED Circuit

Now we build a simple input + output circuit.

### 5.1 – Wiring

On a breadboard:

- Connect LED **anode** (long leg) to a digital pin (e.g. pin 8) through a **220Ω resistor**.
- Connect LED **cathode** (short leg) to **GND**.
- Connect one side of the push button to **5V**.
- Connect the other side of the button to a digital pin (e.g. pin 2).
- Add a **10kΩ resistor** (if available) from pin 2 to GND as a pull-down resistor.

> If you don’t have a resistor handy, you can temporarily use `pinMode(2, INPUT_PULLUP);` and wire the button to GND instead – we’ll explain this later.

### 5.2 – Example Code

An example sketch is in `code_examples/button_led/button_led.ino`.

Behaviour:

- When the button is pressed → LED turns ON.
- When the button is released → LED turns OFF.

---

## 6. Troubleshooting

- **Board not found / no port:**
  - Try another cable or USB port.
  - Close and reopen Arduino IDE.
- **Upload error:**
  - Make sure correct board & port are selected.
  - Press the reset button on the board once and retry.
- **LED not lighting:**
  - Check polarity (long leg to pin through resistor, short leg to GND).
  - Check that you are using the right pin number in code.

---

## 7. This Week’s Tasks

After you complete the guided steps above, open [`tasks.md`](./tasks.md) and do the three tasks:

1. Custom Blink pattern  
2. Two buttons, two LEDs  
3. Short reflection on microcontrollers and ground

These will be your Week 1 submission.
