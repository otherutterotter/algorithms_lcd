#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 4, 4, 3, 2);

void setup()
{
  lcd.begin(16,2);
  lcd.print("hello, world!");
}

void loop() {}

/////*
////SOURCES
////- https://gist.github.com/varlen/91170e7cdd61032107e833fce6b7106a
////- http://www.arduino.cc/en/Tutorial/LiquidCrystal
//// */
//
//#include <LiquidCrystal.h>
////#include <Firmata.h>
//
//// initialize the library with the numbers of the interface pins
////LiquidCrystal lcd(12, 11, 4, 5, 6, 7);
//LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
////int lastLine = 1;
////
////void stringDataCallback(char *stringData){
////   if ( lastLine ) {
////     lastLine = 0;
////     lcd.clear();
////   } else {
////     lastLine = 1;
////     lcd.setCursor(0,1);
////   }
////   lcd.print(stringData);
////}
//
//void setup() {
//  lcd.begin(16,2);
//  lcd.print("hello, world!");
////  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
////  Firmata.attach( STRING_DATA, stringDataCallback);
////  Firmata.begin();
//}
//
//void loop() {
//  // set the cursor to column 0, line 1
//  // (note: line 1 is the second row, since counting begins with 0):
//  lcd.setCursor(0, 1);
//  lcd.print(millis() / 1000);
////  while ( Firmata.available() ) {
////    // lcd.print(millis() / 1000);
////    Firmata.processInput();
////  }
//}
//
