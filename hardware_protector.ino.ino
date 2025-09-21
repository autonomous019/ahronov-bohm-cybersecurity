// === Combo Optical + Magnetic Randomizer (ESP32) ===
// LED: GPIO2 (onboard) or change to your IR LED pin
// DRV8871: IN1=GPIO16 (PWM), IN2=GPIO17 (direction)
// Power coils from 5–9V; aim ~20–50 mA to start.

#include <driver/ledc.h>

const int LED_PIN = 2;      // onboard LED (change if needed)
const int IN1_PWM = 16;     // DRV8871 IN1 (PWM)
const int IN2_DIR = 17;     // DRV8871 IN2 (direction)

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(IN2_DIR, OUTPUT);
  digitalWrite(IN2_DIR, LOW);

  // LEDC channel setup for coil PWM on IN1
  // We'll change frequency often; duty ~30–70% randomized
  ledcSetup(0, 1000, 10);           // channel 0, 1 kHz start, 10-bit resolution
  ledcAttachPin(IN1_PWM, 0);

  // Seed RNG
  uint32_t seed = esp_random();
  randomSeed(seed);

  Serial.begin(115200);
  Serial.println("ESP32 LED + Coil Randomizer ready.");
}

static void coilBurst(uint16_t ms_min, uint16_t ms_max) {
  // Randomized burst of PWM with chirp steps
  uint32_t burst_ms = random(ms_min, ms_max + 1);
  uint32_t t0 = millis();

  // Flip direction sometimes to avoid DC bias
  digitalWrite(IN2_DIR, (random(0, 2) == 0) ? LOW : HIGH);

  while (millis() - t0 < burst_ms) {
    // Randomize frequency in 50–5000 Hz, and duty 30–70%
    uint32_t f = random(50, 5001);
    uint32_t duty = random(300, 721); // 10-bit scale (0..1023)
    ledcWriteTone(0, f);
    ledcWrite(0, duty);

    // Short segment 2–12 ms
    delay(random(2, 13));
  }
  // Stop PWM
  ledcWrite(0, 0);
}

static void ledPulse(uint16_t on_ms, uint16_t off_ms) {
  digitalWrite(LED_PIN, HIGH);
  delay(on_ms);
  digitalWrite(LED_PIN, LOW);
  delay(off_ms);
}

void loop() {
  // --- LED randomized pattern (e.g., 3 ms bursts + descending offs) ---
  for (int off = 24; off >= 6; off -= 2) {
    ledPulse(3, off);
  }
  delay(random(100, 501)); // 100–500 ms rest

  // --- Random coil bursts (optical + magnetic not phase-locked) ---
  // Four quick random bursts 8–40 ms each
  for (int i = 0; i < 4; i++) coilBurst(8, 40);

  // One longer chirp burst 80–200 ms
  coilBurst(80, 200);

  // Short idle gap
  delay(random(30, 120));
}
