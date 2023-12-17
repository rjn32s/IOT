
int N =10; // Initialize the nuber of iteration

int x = 0; // Will be used to store the random number
long blinkPeriod = 5000;// Delay value specified
int counter; // counter for runnig for loop
//int fraction = 9;
int onPeriod;
int offPeriod;
void setup()
{
  Serial.begin(9600); // Initialize the bitrate to 9600 

  pinMode(LED_BUILTIN, OUTPUT); // Make builtin LED as output
  Serial.println("Enter a value");
}

void loop()
{
   x = random(0, 9);// Initialize a random number between 0 to 9
   onPeriod =blinkPeriod * ( x)/9;
   offPeriod = blinkPeriod - onPeriod;
   
   if (Serial.available()>0){
   
   
   N = Serial.parseInt();
   Serial.println("# of Iteration: ");
   Serial.println(N);
   Serial.print("The Random Number for this round");
   Serial.println(x);
    // Take user input
  for (counter = 0; counter < N; ++counter) {
    Serial.println(counter);
    Serial.print(".");
    digitalWrite(LED_BUILTIN, HIGH); // On LED
    delay(onPeriod);  // Manipulate the delay amount using the random number x
    digitalWrite(LED_BUILTIN, LOW); // Off LED
    delay(offPeriod); // Manipulate the delay amount using the random number x
  }
 Serial.println("This Round is Done");
 Serial.println("Enter a vlaue and again");
   }
}
