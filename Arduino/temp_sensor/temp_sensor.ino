/*
 * temp_sensor.ino
 * 
 * 2016 Developed by Keith Choison
 * 
 * Uses the following components:
 * - KY013    analog temperature sensor
 * - LCD1602  display (a compatible Hitachi HD44780 chipset)
 * 
 * Configured for:
 * Arduino 2560 Mega
 * 
 * Code referenced from:
 * http://www.sunfounder.com/learn/Super-Kit-V2-0-for-Arduino/lesson-8-lcd1602-super-kit.html
 * https://www.arduino.cc/en/Reference/LiquidCrystal
 * https://tkkrlab.nl/wiki/Arduino_KY-013_Temperature_sensor_module
 * 
 */

#include <LiquidCrystal.h>

#define sensorPin A0 // pin for the sensor data input

char line1[] = "Temperature:";
int timer = 500; // delay time for display
LiquidCrystal lcd (44, 46, 50, 51, 52, 53); // initialize display library (rs, enable, d4, d5, d6, d7)

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600); // initialize serial communications
  lcd.begin (16, 2); // define 16 columns, 2 rows for display
  lcd.print (line1);
}

void loop() {
  // put your main code here, to run repeatedly:
  int analogVal = analogRead (sensorPin);
  double temp = readThermometer (analogVal);

  /* Serial.print ("temp: ");
  Serial.print (temp);
  Serial.println (" F");
  delay (1000); */

  Serial.println (temp);

  lcd.setCursor (0, 1); // write to second line (note: 0 is the first line)
  lcd.print (temp);
  lcd.write (' ');
  lcd.write ((char) 223); // degree symbol
  lcd.write ('F');
  lcd.write (' ');
  lcd.write (' ');

  delay (timer);
}

double readThermometer (int val){
  double temp;

  temp = log (10000.0 * ((1024.0 / val - 1)));
  temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * temp * temp)) * temp);
  temp = temp - 273.15; // convert from K to deg C
  temp = (temp * 9.0) / 5.0 + 32.0; // convert from deg C to deg F

  return temp;
}
