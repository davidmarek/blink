#include <DigiUSB.h>
#include <DigisparkRGB.h>

byte RED = 0;
byte GREEN = 1;
byte BLUE = 2;
byte colors[3] = {0,0,0};
int color = 0;

void setup() {
  DigiUSB.begin();
}

void get_input() {
  int lastRead;
  // when there are no characters to read, or the character isn't a newline
  while (true) { // loop forever    
    if (DigiUSB.available()) {
      // something to read
      lastRead = DigiUSB.read();
      
      DigiUSB.write(lastRead);
      
      colors[color++] = lastRead;
      
      if (color == 3) {
        analogWrite(RED, colors[RED]);
        analogWrite(GREEN, colors[GREEN]);
        analogWrite(BLUE, colors[BLUE]);
        color=0;
        break; // when we get a newline, break out of loop
      }      
    }
    
    // refresh the usb port for 10 milliseconds
    DigiUSB.delay(10);
  }
}

void loop() {
  // print output
  DigiUSB.println("Waiting for input...");
  // get input
  get_input();
}
