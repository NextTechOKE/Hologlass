#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <SoftwareSerial.h>

#define SCREEN_WIDTH 128  // OLED display width
#define SCREEN_HEIGHT 64  // OLED display height
#define OLED_RESET -1     // Reset pin (or -1 if sharing the Arduino reset pin)
#define SCREEN_ADDRESS 0xBC  // 8-bit I2C address for your specific screen

// Initialize display object
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Initialize SoftwareSerial
SoftwareSerial BTSerial(10, 11); // RX, TX

String inputString = ""; // A string to hold incoming data
int currentLine = 0;  // Current position on the screen (horizontal)

void setup() {
  // Initialize Serial for Bluetooth module
  BTSerial.begin(38400);  // Adjust the baud rate according to your module
  
  // Initialize standard Serial for debugging
  Serial.begin(9600);
  
  // Initialize the OLED display
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);  // Don't proceed, loop forever
  }

  // Clear the display
  display.clearDisplay();
}

void loop() {
  while (BTSerial.available()) {
    char inChar = (char)BTSerial.read();
    
    // Debugging: Echo received character to Arduino IDE Serial Monitor
    Serial.print("Received: ");
    Serial.println(inChar, HEX);  // Print in hexadecimal
    
    if (inChar == '\n') {
      // Update the OLED display when a newline character is received
      display.setTextSize(1);
      display.setTextColor(SSD1306_WHITE);
      display.setCursor(currentLine, 0);  // Horizontal position, vertical line
      
      display.print(inputString);
      display.display();
      
      // Move cursor to the end of the current line
      currentLine += 6 * inputString.length();  // Assuming text size 1, each character is 6 pixels wide
      
      // Check for screen width limit and wrap text
      if(currentLine > (SCREEN_WIDTH - 6)) {
        currentLine = 0;
        display.clearDisplay();
      }
      
      // Reset the input string
      inputString = "";
    } else {
      inputString += inChar;
    }
  }
}
