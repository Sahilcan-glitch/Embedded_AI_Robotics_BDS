// Activity 3 – Two Buttons, Two LEDs + Combo Blink
//
// Behaviour:
//   - Button 1 controls LED 1 (ON while pressed)
//   - Button 2 controls LED 2 (ON while pressed)
//   - If BOTH buttons are pressed:
//       -> both LEDs blink together 3 times fast
//
// Wiring:
//   LED1: pin 8 -> LED (through resistor) -> GND
//   LED2: pin 9 -> LED (through resistor) -> GND
//   Button 1: pin 2 <-> button <-> GND
//   Button 2: pin 3 <-> button <-> GND
//   Buttons use INPUT_PULLUP: NOT pressed = HIGH, pressed = LOW

const int LED1_PIN    = 8;
const int LED2_PIN    = 9;
const int BUTTON1_PIN = 2;
const int BUTTON2_PIN = 3;

void setup() {
  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);

  pinMode(BUTTON1_PIN, INPUT_PULLUP); // internal pull-up
  pinMode(BUTTON2_PIN, INPUT_PULLUP); // internal pull-up

  digitalWrite(LED1_PIN, LOW);
  digitalWrite(LED2_PIN, LOW);
}

void loop() {
  bool button1Pressed = (digitalRead(BUTTON1_PIN) == LOW); // pressed = LOW
  bool button2Pressed = (digitalRead(BUTTON2_PIN) == LOW);

  // Check for combo first
  if (button1Pressed && button2Pressed) {
    // Both pressed: special pattern
    for (int i = 0; i < 3; i++) {
      digitalWrite(LED1_PIN, HIGH);
      digitalWrite(LED2_PIN, HIGH);
      delay(150);  // ON
      digitalWrite(LED1_PIN, LOW);
      digitalWrite(LED2_PIN, LOW);
      delay(150);  // OFF
    }
  } else {
    // Normal independent behaviour
    digitalWrite(LED1_PIN, button1Pressed ? HIGH : LOW);
    digitalWrite(LED2_PIN, button2Pressed ? HIGH : LOW);

    delay(10); // small debounce / noise reduction
  }
}
