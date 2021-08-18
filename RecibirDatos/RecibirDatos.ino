int led = 13;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(led,OUTPUT);
}

void loop() {
if(Serial.available()>0)
{
  char opcion = Serial.read();
  if(opcion == 's')
  {
    digitalWrite(led,HIGH);
    }
  else
  {
    digitalWrite(led,LOW);
    }
  }
}
