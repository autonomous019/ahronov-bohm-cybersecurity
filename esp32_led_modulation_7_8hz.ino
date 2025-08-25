
/**
 * LED Modulation Pattern at 7–8 Hz
 * Each cycle (ON + OFF) ~125–143 ms
 * For calming entrainment in sensory experiments
 */

const int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Loop through randomized 7–8 Hz modulated pulses
  for (int i = 0; i < 10; i++) {
    phase_former(random(120, 140), 3);  // Delay + 3ms ON = ~125–143ms
  }

  delay(random(100, 501)); // brief rest period (optional)
}

// LED pulse: ON then OFF with precise delay
void phase_former(int delay_time, int point_duration) {
  digitalWrite(ledPin, HIGH);
  delay(point_duration);
  digitalWrite(ledPin, LOW);
  delay(delay_time);
}
