#include <SPI.h>
#include <RH_RF69.h>

// ---------- Pins ----------
const int IR_LED_PIN   = 25;  // MOSFET gate for IR LED array
const int ONBOARD_LED  = 2;   // your board's LED (active-HIGH on your unit)

// RFM69 pins (ESP32)
#define RFM69_CS   5
#define RFM69_INT  4     // DIO0
#define RFM69_RST  14
#define RF_FREQUENCY 433.0  // MHz

RH_RF69 rf69(RFM69_CS, RFM69_INT);
bool rf_ok = false;

// ---------- LED helpers ----------
inline void onboardOn()  { digitalWrite(ONBOARD_LED, HIGH); }
inline void onboardOff() { digitalWrite(ONBOARD_LED, LOW);  }
inline void irOn()       { digitalWrite(IR_LED_PIN, HIGH);  }
inline void irOff()      { digitalWrite(IR_LED_PIN, LOW);   }

// ---------- Rhythm primitives ----------
int phase_former(int off_delay_ms, int on_ms) {
  irOn();  onboardOn();
  delay(on_ms);
  irOff(); onboardOff();
  delay(off_delay_ms);

  if (rf_ok) {
    const char *msg = "pulse";
    rf69.send((uint8_t*)msg, strlen(msg));
    rf69.waitPacketSent();
  }
  Serial.print("PULSE:"); Serial.print(on_ms);
  Serial.print("ms, OFF:"); Serial.print(off_delay_ms); Serial.println("ms");
  return 0;
}

int random_delay_time(int min_ms, int max_ms){
  int on_ms = random(min_ms, max_ms);   // upper bound exclusive
  irOn();  onboardOn();
  delay(on_ms);
  irOff(); onboardOff();
  delay(3);

  if (rf_ok) {
    const char *msg = "rand";
    rf69.send((uint8_t*)msg, strlen(msg));
    rf69.waitPacketSent();
  }
  Serial.print("RAND:"); Serial.print(on_ms); Serial.println("ms");
  return 0;
}

// ---------- Setup ----------
void setup() {
  pinMode(IR_LED_PIN, OUTPUT);
  pinMode(ONBOARD_LED, OUTPUT);
  irOff(); onboardOff();

  Serial.begin(115200);
  delay(50);
  randomSeed((uint32_t)esp_random());

  // RFM69 reset sequence
  pinMode(RFM69_RST, OUTPUT);
  digitalWrite(RFM69_RST, HIGH); delay(10);
  digitalWrite(RFM69_RST, LOW);  delay(10);

  rf_ok = rf69.init();
  if (rf_ok) {
    rf69.setFrequency(RF_FREQUENCY);
    rf69.setTxPower(14, true); // 14 dBm, PA boost enabled
    // Optional encryption (must match on receiver):
    // uint8_t key[16] = "1234567890ABCDEF";
    // rf69.setEncryptionKey(key);
    Serial.println("✅ RFM69 ready @ 433 MHz");
  } else {
    Serial.println("⚠️ RFM69 init failed — continuing LED + IR only");
  }

  Serial.println("== ESP32 Rhythm + IR + RF (guarded) ==");
}

// ---------- Main loop ----------
void loop() {
  // Four randomized pulses (6–30 ms ON, 3 ms OFF each)
  random_delay_time(6, 30);
  random_delay_time(6, 30);
  random_delay_time(6, 30);
  random_delay_time(6, 30);

  // Descending phase sequence (3 ms ON, decreasing OFF)
  phase_former(24, 3);
  phase_former(22, 3);
  phase_former(20, 3);
  phase_former(18, 3);
  phase_former(16, 3);
  phase_former(14, 3);
  phase_former(12, 3);
  phase_former(10, 3);
  phase_former(8,  3);
  phase_former(6,  3);

  int rest = random(10, 50);  // 100..500 ms
  delay(rest);
  Serial.print("REST:"); Serial.print(rest); Serial.println("ms");
}
