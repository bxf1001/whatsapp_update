
import pyautogui
import time

while True:
    try:
        button_location = pyautogui.locateOnScreen('calling.png')
        continue
    except:
        if pyautogui.locateOnScreen('ringing.png')!=None:
            time.sleep(5)
            pyautogui.press('f12')
            break
