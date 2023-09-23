#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128  // OLED display width
#define SCREEN_HEIGHT 64  // OLED display height
#define OLED_RESET    -1  // Reset pin (or -1 if sharing the Arduino reset pin)
#define SCREEN_ADDRESS 0xBC  // 8-bit I2C address for your specific screen

// Initialize display object
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  // Initialize Serial for debugging (optional)
  Serial.begin(9600);
  
  // Initialize the OLED display
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);  // Don't proceed, loop forever
  }
  
  // Show the Adafruit splash screen (optional)
  display.display();
  delay(2000);

  // Clear the display
  display.clearDisplay();

  // Text display
  display.setTextSize(1);  // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE);  // Draw white text
  display.setCursor(0, 0);  // Start at the top-left corner
  display.print(F("Testing text change"));
  
  // Update the display with the above settings
  display.display();
}

void loop() {
  // Nothing to do in loop since this is just a text display example.
}
