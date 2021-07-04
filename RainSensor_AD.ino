const int RainSensor_D = 4;
const int RainSensor_A = 0;

int RainSensorRead;

void setup(){
    pinMode(RainSensor_D, INPUT);
    pinMode(RainSensor_A, INPUT);
    Serial.begin(9600);
}

void loop(){
    if(digitalRead(RainSensor_D) == LOW) {
        Serial.println("Digital value : wet"); 
        delay(10); 
    }
    else{
        Serial.println("Digital value : dry");
        delay(10); 
    }
    
    RainSensorRead  = analogRead(RainSensor_A);
    
    Serial.print("Analog value : ");
    Serial.println(RainSensorRead ); 
    Serial.println("");
    
    delay(1000);
}
