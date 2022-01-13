import PySimpleGUI as sg
sg.popup('Welcome to the Chromindows Air by Apposoft. Please sign in to your Apposoft ID.')
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
                if values['-email-'] != values['-remail-']:
                    sg.popup_error("Error", font=16)
                    continue
                elif values['-email-'] == values['-remail-']:
                    progress_bar()
                    break
create_account()


def login():
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
                if values['-usrnm-'] == values['-username-'] and values['-pwd-'] == values['-password-']:
                    sg.popup("Welcome Back! ")
                    break
                elif values['-usrnm-'] != values['-usrnm-'] and values['-pwd-'] != values['-password-']:
                    sg.popup("Invalid login. Try again")

login()
sg.popup("Loading Apposoft Credentials and logging you in.")
layout = [[sg.Text('Logging you in.....')],
    	  [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
    	  [sg.Cancel()]]
sg.Image('Mac.png', size=(300,300))
sg.popup("Dowload Apposoft 95 and you will get some pre -  installed apps. Goto ")