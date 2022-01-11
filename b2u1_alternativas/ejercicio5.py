import PySimpleGUI as sg
sg.theme('DarkPurple1')
# Primero creamos una funcion para validar el inicio de sesion.
def iniciar_sesion(usuario, nip):
    if(usuario == "" or nip == ""):
        # si faltan datos notificamos al usuario.
        sg.popup_error('Debes rellenar los campos')
    else:
        if (usuario == "pepe" and nip == "asdasd"):
             # Si las credenciales son correctas lanzamos una notifiacion.  
             sg.popup_ok("Usuario y NIP correctos")
        else:
            # si las credenc les son incorrectas lanzamos otra ificacion.
             sg.popup_error("Usuario o NIP incorrectos")

layout = [
    [sg. Image(filename='logo.png', pad=((95, 0), (18, 10)))],
    [sg. Text('Usuario:', size=(100, 1), justification='center')],
    [sg.InputText('', pad=((0,0), (0, 10)), key='user')],
    [sg. Text('NIP:', size=(100, 1), justification='center')],
    [sg.InputText('', password_char="*", key='nip')],
    [sg.Button ('Iniciar Sesion', key='login'), sg.Button('Cancelar', key='close')]
]

window = sg.Window('Login',layout,size=(250,250))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'close':
        break
    elif (event == 'login'):
        iniciar_sesion(values["user"],values["nip"])