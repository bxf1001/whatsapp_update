import pyautogui
import time

while True:
    try:
        button_location = pyautogui.locateOnScreen('ringing.png')
        button_center = pyautogui.press("f12")
        break
    except:
        time.sleep(1)
        continue
