import pyautogui
import time

while True:
    if pyautogui.locateOnScreen('calling.png')!=None:
        continue
    else:
        pyautogui.locateOnScreen('ringing.png')
        time.sleep(5)
        pyautogui.press('f12')
        break
    