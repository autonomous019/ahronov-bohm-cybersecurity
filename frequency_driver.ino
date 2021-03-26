int buzzerPin = 9;
int cnt = 1;


/* setup() is where you assign ports to the uno or other circuit board
 *  
    for instance put your out wire to pin 9 now it will be energized when
    connecting to breadboard. 
 */
void setup() {
  
   pinMode(9, OUTPUT);
  
}

/* 
 *  
   loop iterates until powered off, main frequencies are set here
you could change the delay(3) to delay(1) to fire up some electrons,
3 fires up protons.  The descending/ascending delays could be set to
any random variables for Cybersecurity purposes, not used for
entanglement.  Different protocols for different applications of
changing velocity magnetic fields. 

TODO: 
   add way to diplay and keep track of frequency in Hz
   should be around 2Hz for TMS. Adjust number of power cycles
   based on last cycle time length, so it adjust to 2Hz give or take .2



int ReadSens_and_Condition(){
  int i;
  int sval = 0;

  for (i = 0; i < 5; i++){
    sval = sval + analogRead(0);    // sensor on analog pin 0
  }

  sval = sval / 5;    // average
  sval = sval / 4;    // scale to 8 bits (0 - 255)
  sval = 255 - sval;  // invert output
  return sval;
}

int sens;
sens = ReadSens_and_Condition();


 for (int i = 0; i <= 255; i++) {
    analogWrite(PWMpin, i);
    delay(10);
  }


*/

void loop() {
    /*
    for security all we need is a changing rhythm, not timed as a primer field as in entanglement
    see entanglement_driver.ino for entanglement version, this version is only for 'encrypting' a brain rhythm
    or whatever is encompassed or enveloped by the field in the middle of the toroid.  

    Note: this is only valid for discrete energy levels of low values such as potential energies 
    */
   
   delay(random(1,10));  //a very quick and dirty way to achieve cybersecurity, random will keep someone from guessing your rhythm. 
 
   //ascending by 2, with proton rhythm, 3 ms point durations
   //these four lines need functionalized.
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   digitalWrite(9,HIGH);
   delay(random(1,30));
   digitalWrite(9,LOW);
   delay(random(1,30));
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   digitalWrite(9,HIGH);
   delay(3);
   digitalWrite(9,LOW);
   delay(random(1,30));
   digitalWrite(9,HIGH);
   delay(3);






  
}//end of loop()
