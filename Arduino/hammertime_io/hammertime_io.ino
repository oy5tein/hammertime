
 /*
 
IO


 */
 

const int DO_MOTOR = 7;
const int DO_RED_LED = 8;
const int DO_GREEN_LED = 9;
const int DO_BLUE_LED = 10;
const int DO_IR_LED = 11;
const int DI_FRAME_PULSE = 12;
const int LED = 13;
const int DO_FAN = 6;



// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(DO_RED_LED, OUTPUT);     
  pinMode(DO_GREEN_LED, OUTPUT);     
  pinMode(DO_BLUE_LED, OUTPUT);
  pinMode(DO_MOTOR, OUTPUT);
  pinMode(DI_FRAME_PULSE, INPUT);
  pinMode(LED, OUTPUT);  
  pinMode(DO_FAN, OUTPUT);  
  pinMode(DO_IR_LED, OUTPUT);
  Serial.begin(115200);
   
}

int incomingByte;  
char r=0;
char g=0;
char b=0;
char m=0;
char ir=0;

int framePulseOld = false;

char rotationStarted=false;


void StartMotor(){
     digitalWrite(DO_MOTOR, HIGH);
     Serial.write('M');
     rotationStarted=true;
}
void StopMotor(){
    digitalWrite(DO_MOTOR, LOW);
    rotationStarted=false;
    Serial.write('m');
}
void loop() {
  
    if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
      incomingByte = Serial.read();
      // if it's a capital H (ASCII 72), turn on the LED:

      switch (incomingByte)
      {
        case 'R':
          r=255;
          Serial.write('R');
          digitalWrite(DO_RED_LED, HIGH);
          break;
        case'r':
          r=0;
          Serial.write('r');
          digitalWrite(DO_RED_LED, LOW);
          break;
        case 'G':
          g=255;
          Serial.write('G');
          digitalWrite(DO_GREEN_LED, HIGH);
          break;
        case'g':
          g=0;
          Serial.write('g');
          digitalWrite(DO_GREEN_LED, LOW);
          break;
  
        case 'B':
          b=255;
          Serial.write('B');
          digitalWrite(DO_BLUE_LED, HIGH);
          break;
        case'b':
          b=0;
          Serial.write('b');
          digitalWrite(DO_BLUE_LED, LOW);
          break;
        case 'M':
            Serial.write("M");
            StartMotor();
            delay(100);
        break;
        
        case 'm':
            StopMotor();
        break;

        case 'F':
          Serial.println("$DO_FAN,1");
          digitalWrite(DO_FAN, HIGH);
          break;
        case'f':
          Serial.println("$DO_FAN,0");          
          digitalWrite(DO_FAN, LOW);
          break;


        case 'I':
          Serial.println("$DO_IR_LED,1");
          digitalWrite(DO_IR_LED, HIGH);
          break;
        case'i':
          Serial.println("$DO_IR_LED,0");
          digitalWrite(DO_IR_LED, LOW);
          break;


      }
   }
   
  
  int framePulse = digitalRead(DI_FRAME_PULSE);
  int framePulseFallingEdge = ((framePulseOld == true) && (framePulse==false));
  framePulseOld=framePulse;

  if (framePulseFallingEdge == true)
  {
    StopMotor();
  }



}