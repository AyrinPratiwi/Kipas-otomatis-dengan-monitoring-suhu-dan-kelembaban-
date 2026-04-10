#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22
#define LEDPIN 9

LiquidCrystal_I2C lcd(0x27, 16, 2);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  lcd.init();
  lcd.backlight();
  dht.begin();
  pinMode(LEDPIN, OUTPUT);
}

void loop() {
  float suhu = dht.readTemperature();
  float kelembaban = dht.readHumidity(); 

  lcd.clear();

  // cek error
  if (isnan(suhu) || isnan(kelembaban)) {
    lcd.setCursor(0,0);
    lcd.print("Sensor Error");
    return;
  }

  // tampilkan suhu
  lcd.setCursor(0,0);
  lcd.print("T:");
  lcd.print(suhu);
  lcd.print("C ");

  // tampilkan kelembaban
  lcd.print("H:");
  lcd.print(kelembaban);
  lcd.print("%");

  // logika LED (kipas)
  if (suhu > 30) {
    digitalWrite(LEDPIN, HIGH);
    lcd.setCursor(0,1);
    lcd.print("PANAS (Kipas ON)");
  } else {
    digitalWrite(LEDPIN, LOW);
    lcd.setCursor(0,1);
    lcd.print("NORMAL (OFF)");
  }

  delay(2000);
}