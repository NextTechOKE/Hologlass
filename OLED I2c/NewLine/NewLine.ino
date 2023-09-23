#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128  // OLED display width
#define SCREEN_HEIGHT 64  // OLED display height
#define OLED_RESET    -1  // Reset pin (or -1 if sharing the Arduino reset pin)
#define SCREEN_ADDRESS 0xBC  // 8-bit I2C address for your specific screen

// Initialize display object
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

String inputString = ""; // A string to hold incoming Serial data
int currentLine = 0;  // Current line on the screen

void setup() {
  // Initialize Serial for debugging (optional)
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
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      // Update the OLED display when a newline character is received
      display.setTextSize(1);  // Normal 1:1 pixel scale
      display.setTextColor(SSD1306_WHITE);  // Draw white text
      display.setCursor(0, currentLine);  // Start at the appropriate line
      
      display.print(inputString);  // Print the received string to the OLED
      
      display.display();  // Update the display
      
      inputString = "";  // Clear the input string for new data
      
      currentLine += 10;  // Move to the next line by 10 pixels
      
      // Check for screen limit
      if(currentLine > (SCREEN_HEIGHT - 10)) {
        currentLine = 0;
        display.clearDisplay();  // Clear screen when it's full
      }
    } else {
      inputString += inChar;  // Add received char to string
    }
  }
}
