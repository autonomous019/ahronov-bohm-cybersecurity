
/* this accelerate is not the same for entanglement
 *  it has random calls so the frequency is always 
 *  different and theoretically unguessable, but
 *  has a 4 sections of 3 accelerating angular momentum
 *  
 *  Part of the Cybersecurity Tests
 */

int ledPin = 9;
int sensorValue;     // variable to stores data
const int adc = 0 ;   //naming pin 0 of analog input side as ‘adc’

void setup() {
  
  pinMode(9, OUTPUT);
  Serial.begin(9600);  //init serial comm
  
}


void loop() {
//make point_duration a constant in the header
//for ascending field set delay_time to a sequence of descending numbers, point duration should be either 1 or 3 (milliseconds)

  sensorValue = analogRead(ledPin);
  Serial.println(sensorValue);         // send data to serial
  
  int adc  = analogRead(0) ;    //reading analog voltage and storing it in an integer 
  adc = map(adc, 0, 1023, 0, 255);
  Serial.println(adc);    
/*
----------map funtion------------the above funtion scales the output of adc, which is 10 bit and gives values btw 0 to 1023, in values btw 0 to 255 form analogWrite funtion which only receives  values btw this range
*/


//add as many 'pins' or 'counters' to add random config to em waves for security, prevents others from hijacking your shield
int random_key_1 = random_delay_time(6,30);
int random_key_2 = random_delay_time(6,30);
int random_key_3 = random_delay_time(6,30);
int random_key_4 = random_delay_time(6,30);


//set either an ascending or descending rhythm (phase) here

int phaser_a = phase_former(24,3);
int phaser_b = phase_former(22,3);
int phaser_c = phase_former(20,3);
int phaser_d = phase_former(18,3);
int phaser_e = phase_former(16,3);
int phaser_f = phase_former(14,3);
int phaser_g = phase_former(12,3);
int phaser_h = phase_former(10,3);
int phaser_i = phase_former(8,3);
int phaser_k = phase_former(6,3);


}// ends loop()


int phase_former(int delay_time, int point_duration) {
  int v = 0;
  digitalWrite(9,HIGH);
  delay(point_duration);
  digitalWrite(9,LOW);
  delay(delay_time);
  return v; 
}

//i am a random delay function put me in to keep others guessing the em pattern
int random_delay_time(int min_delay, int max_delay){
  digitalWrite(9,HIGH);
  delay(random(min_delay,max_delay));
  digitalWrite(9,LOW);
  delay(3);      
}
