import pyautogui
import time

text = input("Enter the text you want to send")

i=0
while True:
  time.sleep(2)
  pyautogui.typewrite(text)
  time.sleep(1)
  pyautogui.press('enter')