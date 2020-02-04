#include <LiquidCrystal.h>
#include <Firmata.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void stringDataCallback(char *stringData){
   lcd.setCursor(0,1);
   lcd.print(stringData);
}

void setup() {
  lcd.begin(16,2);
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
  Firmata.attach( STRING_DATA, stringDataCallback);
  Firmata.begin();
}

void loop() {
  while ( Firmata.available() ) {
    Firmata.processInput();
  }
}
