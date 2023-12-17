void setup() {
  Serial.begin(9600);
    // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}
void loop() {
  if (Serial.available() > 0) {
    int data = Serial.parseInt();
    //Serial.println(data);
    //Serial.print("*");
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000*data/9);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(1000*(1-data)/9);
    //Serial.print(".");
  }

 else{
// Default Mode
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(100);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(100);

  }
    
    //Serial.print("You sent me: ");
    //Serial.println(data);
  
}
