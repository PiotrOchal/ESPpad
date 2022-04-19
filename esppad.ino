//created by Piotr Ochal

//button ABXY
const int bA = 32;
const int bB = 5;
const int bX = 35;
const int bY = 17;
//triggers use potentiometers
const int Tr = 12;
const int Tl = 14;
//joystic  use potentiometers
const int Jlx = 27;


const int Jly = 33;
const int Jrx = 25;
const int Jry = 36;
 

//variables
int vA;
int vB;
int vX;
int vY;
int vTr;
int vTl;
int vJlx;

int vJly;
int vJrx;
int vJry;
 
void setup() {
  pinMode (bA, INPUT);
  pinMode (bB, INPUT);
  pinMode (bX, INPUT);
  pinMode (bY, INPUT);
  Serial.begin (9600);
}

void loop() {
  //read variables
  
  vA = digitalRead(bA);
  vX = digitalRead(bX);
  vB = digitalRead(bB);
  vY = digitalRead(bY);
  vTr=analogRead(Tr);
  vTl=analogRead(Tl);
  vJlx=analogRead(Jlx);
  
  vJly=analogRead(Jly);
  vJrx=analogRead(Jrx);
  vJry=analogRead(Jry);
  
  //write to serial port
  Serial.print("a");
  Serial.print(vA);
  Serial.print("b");
  Serial.print(vB);
  Serial.print("x");
  Serial.print(vX);
  Serial.print("y");
  Serial.print(vY);
  Serial.print("Jlx");
  Serial.print(vJlx+1000);//add 1000 becuese constant length is easier to read
  Serial.print("Jly");
  Serial.print(vJly+1000);
  Serial.print("Jrx");
  Serial.print(vJrx+1000);
  Serial.print("Jry");
  Serial.print(vJry+1000);
  
  
  Serial.print("Tl");
  Serial.print(vTl+1000);
  Serial.print("Tr");
  Serial.println(vTr+1000);
    
  
}
