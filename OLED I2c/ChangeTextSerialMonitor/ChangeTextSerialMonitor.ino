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
int currentX = 0;  // Current horizontal position
int currentLine = 0;  // Current line on the screen

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
      int textWidth = 6 * inputString.length();  // Calculate text width
      
      // Check for screen width limit and wrap text to the next line
      if(currentX + textWidth > SCREEN_WIDTH) {
        currentX = 0;
        currentLine += 10;  // Move down by 10 pixels
        
        // Check if we've reached the display height, then clear the display
        if(currentLine > (SCREEN_HEIGHT - 10)) {
          currentLine = 0;
          display.clearDisplay();
        }
      }
      
      // Update the OLED display
      display.setTextSize(1);
      display.setTextColor(SSD1306_WHITE);
      display.setCursor(currentX, currentLine);
      
      display.print(inputString);
      display.display();
      
      // Update current position
      currentX += textWidth;
      
      // Reset the input string
      inputString = "";
    } else {
      inputString += inChar;
    }
  }
}
