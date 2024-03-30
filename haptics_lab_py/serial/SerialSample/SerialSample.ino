#include <M5Stack.h>

int cnt = 0;

void setup() {
  M5.begin();
  M5.Lcd.setTextSize(2);
  M5.Lcd.println("Waiting for serial data...");

  Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        /// Read data from serial
        String data = Serial.readStringUntil('\n');

        int commaIndex = data.indexOf(',');
        int data_1 = data.substring(0, commaIndex).toInt();
        float data_2 = data.substring(commaIndex + 1).toFloat();

        M5.Lcd.fillScreen(BLACK);
        M5.Lcd.setCursor(0, 0);
        M5.Lcd.print("data_1: ");
        M5.Lcd.println(data_1);
        M5.Lcd.print("data_2: ");
        M5.Lcd.println(data_2);

        /// Send data to serial
        if (data_1 % 5 == 0) {
          cnt += 1;
          M5.Lcd.fillScreen(BLUE);
          Serial.print(cnt);
          Serial.print(",");
          Serial.println(cnt*0.1);
        }
    }
}
