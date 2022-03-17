import PySimpleGUI as sg
from tkinter import simpledialog
import pyttsx3
import os
import webbrowser as wb
import time
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

username = ''
password = ''
#PROGRESS BAR
def progress_bar():
    sg.theme('LightBlue2')
    layout = [[sg.Text('Creating your account...')],
            [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
            [sg.Cancel()]]

    window = sg.Window('Working...', layout)
    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()


def create_account():
    global username, password
    sg.theme('LightBlue2')
    layout = [[sg.Text("Sign Up", size =(15, 1), font=40, justification='c')],
             [sg.Text("E-mail", size =(15, 1),font=16), sg.InputText(key='-email-', font=16)],
             [sg.Text("Re-enter E-mail", size =(15, 1), font=16), sg.InputText(key='-remail-', font=16)],
             [sg.Text("Create Username", size =(15, 1), font=16), sg.InputText(key='-username-', font=16)],
             [sg.Text("Create Password", size =(15, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
             [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Sign Up", layout)

    while True:
        event,values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                password = values['-password-']
                username = values['-username-']
                if values['-email-'] != values['-remail-']:
                    sg.popup_error("Error", font=16)
                    continue
                elif values['-email-'] == values['-remail-']:
                    progress_bar()
                    break
    window.close()
create_account()


def login():
    global username,password
    sg.theme("LightBlue2")
    layout = [[sg.Text("Log In", size =(15, 1), font=40)],
            [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-usrnm-', font=16)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-pwd-', password_char='*', font=16)],
            [sg.Button('Ok'),sg.Button('Cancel')]]

    window = sg.Window("Log In", layout)

    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Ok":
                if values['-usrnm-'] == username and values['-pwd-'] == password:
                    sg.popup("Welcome Back !")
                    break
                elif values['-usrnm-'] != username or values['-pwd-'] != password:
                    sg.popup("Invalid login. Try again")

    window.close()
login()
# root.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Chromindows Air UserName for AIsisstaint",
                                  prompt="What do you want AIsisstaint to call you ? :")

# check it out
sg.popup("Hello", USER_INP)
sg.popup("Starting AIsisstaint....")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
text = ("Welcome to AAI Sistaitant.")
text1 = ("Welcome back " , USER_INP)
engine.say(text)
engine.runAndWait()
engine.say(text1)
engine.runAndWait()
# root.withdraw()
# the input dialog
gUSER_ASKED = simpledialog.askstring(title="AAI Sistaitant",
                                  prompt="What Google App do you want to open?:")
if gUSER_ASKED == ("Gmail"):
    wb.open_new_tab('https://mail.google.com/mail/u/0/#inbox')
if gUSER_ASKED == ("Google"):
    wb.open_new_tab('https://www.google.com/')
if gUSER_ASKED == ("Google Docs"):
    wb.open_new_tab('https://docs.google.com/document/u/0/')
if gUSER_ASKED == ("Google Sheets"):
    wb.open_new_tab('https://docs.google.com/spreadsheets/u/0/')
if gUSER_ASKED == ("Google Slides"):
    wb.open_new_tab('https://docs.google.com/presentation/u/0/')
if gUSER_ASKED == ("Google Maps"):
    wb.open_new_tab('https://www.google.com/maps/@-37.8922746,145.060364,15z')
if gUSER_ASKED == ("Google Forms"):
    wb.open_new_tab('https://translate.google.com/')
if gUSER_ASKED == ("Google Earth"):
    wb.open_new_tab('https://earth.google.com/web/@0,0,0a,22251752.77375655d,35y,0h,0t,0r')
if gUSER_ASKED == ("Google Hangouts"):
    wb.open_new_tab('https://hangouts.google.com/')
if gUSER_ASKED == ("Google Chat"):
    wb.open_new_tab('https://mail.google.com/chat/u/0/#chat/welcome')
if gUSER_ASKED == ("Google Meet"):
    wb.open_new_tab('https://meet.google.com/?pli=1')
if gUSER_ASKED == ("Google Colab"):
    wb.open_new_tab('https://colab.research.google.com/notebooks/intro.ipynb')
if gUSER_ASKED == ("Youtube"):
    wb.open_new_tab('https://www.youtube.com/')
mUSER_ASKED = simpledialog.askstring(title="AAI Sistaitant",
                                  prompt="What Microsoft App do you want to open?:")
if mUSER_ASKED == ("Microsoft Word"):
    wb.open_new_tab('https://www.office.com/launch/word?ui=en-US&rs=GB&auth=1')
if mUSER_ASKED == ("Microsoft Powerpoint"):
    wb.open_new_tab('https://www.office.com/launch/powerpoint?ui=en-US&rs=GB&auth=1')
if mUSER_ASKED == ("Microsoft Excel"):
    wb.open_new_tab('https://www.office.com/launch/excel?ui=en-US&rs=GB&auth=1')
if mUSER_ASKED == ("Microsoft Outlook"):
    wb.open_new_tab('https://outlook.live.com/mail/0/')
if mUSER_ASKED == ("Microsoft Onedrive"):
    wb.open_new_tab('https://onedrive.live.com/')
if mUSER_ASKED == ("Microsoft Teams"):
    wb.open_new_tab('https://teams.live.com/_?utm_source=OfficeWeb')
if mUSER_ASKED == ("Microsoft Onenote"):
    wb.open_new_tab('https://www.onenote.com/notebooks?session=9cb942b9-8507-4a3a-80c3-ab943a4af33d&auth=1&fromAR=1')
if mUSER_ASKED == ("Microsoft To Do"):
    wb.open_new_tab('https://to-do.live.com/tasks/')
if mUSER_ASKED == ("Skype"):
    wb.open_new_tab('https://web.skype.com/')
aUSER_ASKED = simpledialog.askstring(title="AAI Sistaitant",
                                  prompt="What Apple App do you want to open?:")
if aUSER_ASKED == ("Apple Pages"):
    wb.open_new_tab('https://www.icloud.com/pages/')
if aUSER_ASKED == ("Apple Numbers"):
    wb.open_new_tab('https://www.icloud.com/numbers/')
if aUSER_ASKED == ("Apple Keynote"):
    wb.open_new_tab('https://www.icloud.com/keynote/')
if aUSER_ASKED == ("Apple iCloud Drive"):
    wb.open_new_tab('https://www.icloud.com/iclouddrive/')
if aUSER_ASKED == ("Apple Find My"):
    wb.open_new_tab('https://www.icloud.com/find/')
if aUSER_ASKED == ("Apple Reminders"):
    wb.open_new_tab('https://www.icloud.com/reminders/')
if aUSER_ASKED == ("Apple Notes"):
    wb.open_new_tab('https://www.icloud.com/notes/')
if aUSER_ASKED == ("Apple Photos"):
    wb.open_new_tab('https://www.icloud.com/photos/')
if aUSER_ASKED == ("Apple Calender"):
    wb.open_new_tab('https://www.icloud.com/calendar/')
if aUSER_ASKED == ("Apple Contacts"):
    wb.open_new_tab('https://www.icloud.com/contacts/')

root= tk.Tk()
canvas = tk.Canvas(root , width =600 , height = 300)
# canvas.grid(columnspan = 3)
#logo

logo = Image.open('images.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.Image = logo
logo_label.grid(column=1 , row=0)
#text
instructions = tk.Label(root, text=USER_INP ,font='Terminal')
instructions.grid(columnspan=3, column=0 ,row=1)

entry1 = tk.Entry (root) 
canvas.create_window(200, 140, window=entry1)
entry1.grid(columnspan=3, column=0 ,row=2)

root.mainloop()