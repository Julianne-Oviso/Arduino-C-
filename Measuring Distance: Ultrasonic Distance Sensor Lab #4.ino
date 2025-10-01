//my code
const int buttonPin = 2;
int pressCount = 0;

//track button state
bool buttonPressed = false;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int reading = HIGH;
  reading = digitalRead(buttonPin);
  
  //----- Wait for "make" (button pres: HIGH -> LOW) 
  while(digitalRead(buttonPin)== HIGH) {
    // While button isn't pressed
     Serial.println("Waiting to Detect an Object");
  }
  
  // Button pressed!
  pressCount++; 
  Serial.println("Object Detected & Present");
  Serial.println(pressCount);
  
  // Wait for "break" (button release: LOW -> HIGH) 
  while(digitalRead(buttonPin)== LOW) {
    //do nothing until button is pressed 
  }
  
  //Button released 
  Serial.println("Detected Object Is Gone");
}
