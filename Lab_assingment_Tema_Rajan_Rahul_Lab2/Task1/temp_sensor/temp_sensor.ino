int i = 0;
void setup() {
  Serial.begin(9600);
}
void loop() {
  i = random(0,10);
  Serial.println(i);
  delay(1000);
}
