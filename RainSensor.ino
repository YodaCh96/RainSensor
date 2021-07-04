int RainSensor = 0; // Analog Input A0

void setup(){
    Serial.begin(9600);
    pinMode(RainSensor, INPUT);
}

void loop(){
    int RainSensorRead = analogRead(RainSensor);
    Serial.println(RainSensorRead);
    delay(1000);
}
