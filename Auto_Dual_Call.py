import pyautogui
import subprocess
import PySimpleGUI as sg
import time

timer1=input('ADD TIMER::')
timer1=int(timer1)
add_number1=input('ADD NUMBER HERE::') 
timer2=input('ADD TIMER::') 
timer2=int(timer2)
add_number2=input('ADD NUMBER HERE::') 
pyautogui.FailSafeException = False

def phone_number_1(number_1):
    url = f"whatsapp://send?phone=+91{number_1}"
    subprocess.Popen(["cmd", "/C", f"start {url}"], shell=True)


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

#This is timer
    time.sleep(timer1*60)
    subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)

    time.sleep(2)
#Unlock 
    pyautogui.hotkey('ctrl', 'alt', 'z')

#Cut call
#time.sleep(1)
#button_location1 = pyautogui.locateCenterOnScreen('end_button.png')

# Click the button
#time.sleep(1)
#pyautogui.click(button_location1)

#stop Recording
    time.sleep(2)
    pyautogui.press('f12')

    time.sleep(2)
def phone_number_2(number_2):
    url = f"whatsapp://send?phone=+91{number_2}"
    subprocess.Popen(["cmd", "/C", f"start {url}"], shell=True)


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

#This is timer
    time.sleep(timer2*60)
    subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)


#Cut call
#time.sleep(1)
#button_location1 = pyautogui.locateCenterOnScreen('end_button.png')

# Click the button
#time.sleep(1)
#pyautogui.click(button_location1)


    if timer2<9:
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
