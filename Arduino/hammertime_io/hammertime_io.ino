
 /*
  Hammertime io module implemented on Arduino uno.

  Serial port 115200 baud

  Serial commands and Status:
  'M' motor start
  'm' motor stop
  'A' run motor one revolution then stop (with m as status)
  'R' Red LED on
  'r' Red LED off
  'G' Green LED on
  'g' Green LED off
  'B' Blue LED on
  'b' Blue LED off
  'B' Blue LED on
  'b' Blue LED off
  'I' IR led on
  'i' IR led off

   - Øystein Buanes 
 */
 
#define DEBOUNCE_TIME_MS 100

const int DO_MOTOR = 7;
const int DO_RED_LED = 8;
const int DO_GREEN_LED = 9;
const int DO_BLUE_LED = 10;
const int DO_IR_LED = 11;
const int DI_FRAME_PULSE = 12;



// the setup routine runs once when you press reset:
void setup() {                
  // define DO
  pinMode(DO_RED_LED, OUTPUT);     
  pinMode(DO_GREEN_LED, OUTPUT);     
  pinMode(DO_BLUE_LED, OUTPUT);
  pinMode(DO_MOTOR, OUTPUT);
  pinMode(DI_FRAME_PULSE, INPUT);
  pinMode(DO_IR_LED, OUTPUT);
  Serial.begin(115200);
 
}


void StartMotor(){
     digitalWrite(DO_MOTOR, HIGH);
     Serial.write('M');

}
void StopMotor(){
    digitalWrite(DO_MOTOR, LOW);
    Serial.write('m');
}

int incomingByte;  
int framePulseOld = false;
int advanceOneFrame = false;

void loop() {
  
    if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
      incomingByte = Serial.read();

      switch (incomingByte)
      {
        case 'R':
          Serial.write('R');
          digitalWrite(DO_RED_LED, HIGH);
          break;
        case 'r':
          Serial.write('r');
          digitalWrite(DO_RED_LED, LOW);
          break;
        case 'G':
          Serial.write('G');
          digitalWrite(DO_GREEN_LED, HIGH);
          break;
        case 'g':
          Serial.write('g');
          digitalWrite(DO_GREEN_LED, LOW);
          break;
  
        case 'B':
          Serial.write('B');
          digitalWrite(DO_BLUE_LED, HIGH);
          break;
        case 'b':
          Serial.write('b');
          digitalWrite(DO_BLUE_LED, LOW);
          break;

        case 'M':
          Serial.write("M");
          StartMotor();
        break;
        
        case 'm':
          StopMotor();
        break;

        case 'A':  // advance one frame
          Serial.write('A');
          advanceOneFrame = true;
          StartMotor();
        break;

        case 'I':
          Serial.write('I');
          digitalWrite(DO_IR_LED, HIGH);
          break;
        case 'i':
          Serial.write('i');
          digitalWrite(DO_IR_LED, LOW);
          break;
      }
   }
   
  int framePulse = digitalRead(DI_FRAME_PULSE);
  int framePulseFallingEdge = ((framePulseOld == true) && (framePulse==false));
  framePulseOld=framePulse;

  if ((framePulseFallingEdge == true) && (advanceOneFrame == true )) {
    delay(DEBOUNCE_TIME_MS);  // lazy hack to do debouce
    StopMotor();
    advanceOneFrame = false;
  }

}