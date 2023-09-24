import pyautogui
import time

# Set the position where you want to start typing
start_x, start_y = 1127, 726

# Define the sentence you want to type
sentence = "In ancient times, the Capital was visited by an incredible, technologically advanced people. The people of the Capitol were amazed and begged them to stay, They called them Haptix "


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
