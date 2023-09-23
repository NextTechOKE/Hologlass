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
      display.clearDisplay();  // Clear previous content
      
      display.setTextSize(1);  // Normal 1:1 pixel scale
      display.setTextColor(SSD1306_WHITE);  // Draw white text
      display.setCursor(0, 0);  // Start at the top-left corner
      
      display.print(inputString);  // Print the received string to the OLED
      
      display.display();  // Update the display
      
      inputString = "";  // Clear the input string for new data
    } else {
      inputString += inChar;  // Add received char to string
    }
  }
}
