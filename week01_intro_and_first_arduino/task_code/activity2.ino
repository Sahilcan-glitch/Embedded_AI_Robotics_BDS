// Activity 2 – One Button, One LED
// Button pressed  -> LED ON
// Button released -> LED OFF
//
// Wiring:
//   LED on pin 8 (with resistor) to GND
//   Button between pin 2 and GND
//   Using INPUT_PULLUP: NOT pressed = HIGH, pressed = LOW

const int LED_PIN    = 8;
const int BUTTON_PIN = 2;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);  // internal pull-up enabled
  digitalWrite(LED_PIN, LOW);         // start with LED OFF
}

void loop() {
  // Read button state
  bool buttonPressed = (digitalRead(BUTTON_PIN) == LOW);  // pressed = LOW

  if (buttonPressed) {
    digitalWrite(LED_PIN, HIGH);  // LED ON
  } else {
    digitalWrite(LED_PIN, LOW);   // LED OFF
  }

  delay(10);  // small delay to reduce noise
}
