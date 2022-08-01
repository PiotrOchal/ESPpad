//created by Piotr Ochal

//button ABXY
const int bA = 19;
const int bB = 23;
const int bX = 21;
const int bY = 22;
//triggers use potentiometers
//const int Tr = 12;
//const int Tl = 14;
//joystic  use potentiometers
const int Jlx = 15;
const int jbl=0;
const int jbr=12;

const int Jly = 2;
const int Jrx = 14;
const int Jry = 27;

const int bu = 17;
const int bd = 18;
const int bl =  5;
const int br = 16; 

//variables
int vA;
int vB;
int vX;
int vY;

int vu;
int vd;
int vl;
int vr;
//int vTr;
//int vTl;
int vJlx;

int vJly;
int vJrx;
int vJry;
int jl;
int jr;
void setup() {
  pinMode (bA, INPUT);
  pinMode (bB, INPUT);
  pinMode (bX, INPUT);
  pinMode (bY, INPUT);
  Serial.begin (512000);
  pinMode (bu, INPUT);
  pinMode (bd, INPUT);
  pinMode (bl, INPUT);
  pinMode (br, INPUT);
  pinMode(jbr, INPUT_PULLUP);
  pinMode(jbl, INPUT_PULLUP);
}

void loop() {
  //read variables
  
  vA = digitalRead(bA);
  vX = digitalRead(bX);
  vB = digitalRead(bB);
  vY = digitalRead(bY);
  vu = digitalRead(bu);
  vd = digitalRead(bd);
  vl = digitalRead(bl);
  vr = digitalRead(br);
//  vTr=analogRead(Tr);
//  vTl=analogRead(Tl);
  vJlx=analogRead(Jlx);
  jl=digitalRead(jbl);
  jr=digitalRead(jbr);
  //reduce error use parabolic function
  vJlx=1.2224546194*vJlx-0.0000543235*vJlx*vJlx;
  vJly=analogRead(Jly);
  //error
  vJly=(vJly*vJly*(-0.000256)+2.047132*vJly);
  vJrx=analogRead(Jrx);
  //error
  vJrx=1.1761864381*vJrx-0.0000430248*vJrx*vJrx;
  vJry=analogRead(Jry);
//error
  vJry=(vJry*vJry*(-0.0000391277)+1.1602278046*vJry);
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
  Serial.print(4095-vJlx+1000);//add 1000 becuese constant length is easier to read
  Serial.print("Jly");
  Serial.print(vJly+1000);
  Serial.print("Jrx");
  Serial.print(vJrx+1000);
  Serial.print("Jry");
  Serial.print(4095-vJry+1000);
  Serial.print("^");
  Serial.print(vu);
  Serial.print("v");
  Serial.print(vd);
  Serial.print("<");
  Serial.print(vl);
  Serial.print(">");
  Serial.print(vr);
  Serial.print("R");
  Serial.print(1-jr);
  Serial.print("L");
  Serial.print(1-jl);
//  Serial.print("Tl");
//  Serial.print(vTl+1000);
//  Serial.print("Tr");
//  Serial.println(vTr+1000);
//    
  
}
