import pyautogui
import subprocess
import PySimpleGUI as sg
import time


timer=input('ADD TIMER:: ')     #Add Time Here
add_number=input('ADD NUMBER HERE:: ')     #Add Number & Press F5
timer=int(timer)

pyautogui.FailSafeException = False


def phone_number(number):
    url = f"whatsapp://send?phone=+91{number}"
    subprocess.Popen(["cmd", "/C", f"start {url}"], shell=True)

phone_number(add_number)
time.sleep(0.25)
phone_number(add_number)


time.sleep(1)
while True:
    try:
        button_location = pyautogui.locateOnScreen('call_button.png')
        button_center = pyautogui.center(button_location)
        pyautogui.click(button_center.x, button_center.y)
        break
    except:
        time.sleep(1)
        continue

time.sleep(2)
pyautogui.hotkey('win', 'up')
#Start recording

time.sleep(30)
pyautogui.press('f12')


#Puts First LK
time.sleep(5)
pyautogui.hotkey('ctrl', 'alt', 'z')

#button_location1 = pyautogui.locateCenterOnScreen('end_button.png')

# Click the button
#time.sleep(0.5)
#pyautogui.click(button_location1)


#This is timer
time.sleep(timer*60)
subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)

if timer<9:
#Unlock 
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'alt', 'z')

#stop Recording
    time.sleep(2)
    pyautogui.press('f12')
#Final Lock
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'alt', 'z')


time.sleep(1)
sg.theme('NeutralBlue')
layout=[sg.popup('TIME OUT',font='stencil 50')]


