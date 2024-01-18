import Whatsappcall
import time
import PySimpleGUI

print("             WELCOME TO PUZHAL PHONE PORTAL              ")
enter_calls = input("ENTER NO OF CALLS (1/2):: ")
enter_calls=int(enter_calls)


while True:
    if enter_calls==1:
        add_time=input('ADD_TIME:: ')
        add_time=int(add_time)
        add_num=input('ADD_NUMBER:: ')
        Whatsappcall.phone_number(add_num)
        Whatsappcall.timer(add_time)
        time.sleep(1)
        sg.theme('NeutralBlue')
        layout=[sg.popup('TIME OUT',font='stencil 50')]

    else:
        print("Invalid Selection")
    if enter_calls==2:
        add_time1=input('ADD_TIME:: ')
        add_time1=int(add_time1)
        add_num1=input('ADD_NUMBER 1:: ')
        add_time2=input('ADD_TIME:: ')
        add_time2=int(add_time2)
        add_num2=input('ADD_NUMBER 2:: ')
        Whatsappcall.phone_number(add_num1)
        Whatsappcall.timer(add_time1)
        Whatsappcall.phone_number(add_num2)
        Whatsappcall.timer(add_time2)
        time.sleep(1)
        sg.theme('NeutralBlue')
        layout=[sg.popup('TIME OUT',font='stencil 50')]

    else:
        print("Invalid option")