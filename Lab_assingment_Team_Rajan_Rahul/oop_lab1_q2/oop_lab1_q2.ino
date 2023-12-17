class Homeautomation {
  public:
  
  // Declaring the variables 
  // 0 == OFF & 1 == ON state
  // we will be assining these variable using a random function 
    int linghtIntensity = 0;

    int temp = 0;

    int lightStatus = 0;

    int fanStatus = 0;

    int acStatus = 0;

    int isPersonAvailable = 0;
    // Methods
    void sensorData();
    void PrintStatus();
    void LightControl();
    void TempControl();
    
};
// We will first acquire the data from the sensor using random 
void Homeautomation::sensorData(){
linghtIntensity = random(0, 100 + 1);
temp = random(1, 100 + 1);
acStatus = random(0, 1 + 1);
fanStatus = random(0, 1 + 1);
acStatus = random(0, 1 + 1);
isPersonAvailable = random(0, 1 + 1);
}
// This method helps the user to see the changes in the status of applience during the process
void Homeautomation::PrintStatus(){
Serial.println("is person available ?:   ");
Serial.println(isPersonAvailable);  
Serial.println("The light Intentsity is:   ");
Serial.println(linghtIntensity);
Serial.println("The current Tempratue: ");
Serial.println(temp);
Serial.println("The Current state of Fan is:  ");
Serial.println(fanStatus);
Serial.println("The Current state of AC is:  ");
Serial.println(acStatus);
Serial.println("The Current state of Light Bulb is:  ");
Serial.println(lightStatus);
 }
// we will first check if the person is available in the room then
// check for the temprature data from the sensor i.e generated with the random function
// Let assume that sensor data below 50 mean that we need to turn on the light bulb and else we off the bulb
void Homeautomation::LightControl() {
if (isPersonAvailable == 1) {
if (linghtIntensity <= 50) {
lightStatus = 1;
} else {
  lightStatus = 0;
 }}}
 // Now for temprature control we will be using fan and AC appropriately
 // Let's say that below 20 degree we don't need AC and fan
 // Between 20 to 40 we need Fan but not AC
 // and Beyond 40 we Need AC only.
 
void Homeautomation::TempControl() {
if (temp <= 20) {
acStatus = 0;
fanStatus = 0;
} 
else {


if (temp > 20 && temp <= 40) {
acStatus = 0;
fanStatus = 1;
} 

if (temp >40) {
        acStatus = 1;
        fanStatus = 0;
      }
      }
    }
Homeautomation room1;
void setup() {
  Serial.begin(9600);
  
  }
void loop() {
  // First Step 
    // Check the Status of devices and read the sensor data
  room1.sensorData();
  Serial.println("Before Automation");
   // Prompt the current status before automation
  room1.PrintStatus();
  delay(10000);
  // Step2 
   // Take appropiate action on the basis of above data acquired
  room1.LightControl();
  room1.TempControl();
  
  Serial.println("After automation");
  room1.PrintStatus();
  delay(10000);
  // Continue this cycle after some period of time say after every hour
  Serial.println("A Few Moment Later.....................");
  }

  
