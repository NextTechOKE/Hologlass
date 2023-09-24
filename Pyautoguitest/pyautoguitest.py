import pyautogui
import time

# Set the position where you want to start typing
start_x, start_y = 1127, 726

# Define the sentence you want to type
sentence = "The Cygnus NG-19 cargo ship, S.S. Laurel Clark, was launched from Wallops Island on Aug 2.The ISS SSRMS grappled it at 0852 UTC Aug 4 and berthed it at the Unity nadir location at 1228 UTC.On Aug 9 astronauts Prokop'ev and Petelin made spacewalk VKD-60. They attached debris shields"


# Split the sentence into words
words = sentence.split()

# Move the mouse to the starting position
pyautogui.moveTo(start_x, start_y)

time.sleep (5)
# Loop through each word
for word in words:
    # Type the word
    pyautogui.typewrite(word, interval=0.01)  # Adjust interval as needed

    # Press Enter
    pyautogui.press("enter")


    # Wait for a short while (you can adjust the duration)
    time.sleep(0.1)

# Move the mouse away at the end (optional)
pyautogui.moveTo(0, 0)
