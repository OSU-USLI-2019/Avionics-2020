void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    Serial.write("Starting Serial Writer");
}

void loop() {
  int alt = random(1,5000);
  float lat = random(1, 500) / 100.0;
  float lon = random(1, 500) / 100.0;

  

  
  //Serial.println("Altitude:" + randy);
  Serial.print("Altitude: " + (String)alt + ", Lat: " + (String)lat + ", Lon:" + (String)lon + "\n" );
  delay(random(1,2000));
}
