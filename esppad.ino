const int bA = 32;
const int bB = 5;
const int bX = 35;
const int bY = 17;
const int gas = 12;
const int ham = 14;
const int kier = 27;
int vA;
int vB;
int vX;
int vY;
int vgas;
int vham;
int vkier;
void setup() {

  pinMode (bA, INPUT);
  pinMode (bB, INPUT);
  pinMode (bX, INPUT);
  pinMode (bY, INPUT);


    
  
  Serial.begin (9600);
}

void loop() {
  vkier=analogRead(kier);
  vA = digitalRead(bA);
  vX = digitalRead(bX);
  vB = digitalRead(bB);
  vY = digitalRead(bY);
  vgas =analogRead(gas);
  vham=analogRead(ham);
 
    
    Serial.print("a");
    Serial.print(vA);
    Serial.print("b");
    Serial.print(vB);
    Serial.print("x");
    Serial.print(vX);
    Serial.print("y");
    Serial.print(vY);
    Serial.print("Jlx");
    Serial.print(vkier+1000);
    Serial.print("Tl");
    Serial.print(vham+1000);
    Serial.print("Tr");
    Serial.println(vgas+1000);
    
  
}
