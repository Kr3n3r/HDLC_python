from tkinter import *
#defino la función de login
def login():
    #recojo los valores de usuario y contraseña
    uname=username.get()
    pwd=password.get()
    #valido los datos
    if uname=='' or pwd=='':
        message.set("Rellena los campos vacíos!!!")
    else:
      if uname=="pepe" and pwd=="asdasd":
       message.set("Has entrado al sistema!")
      else:
       message.set("Contraseña o usuario incorrecto!!!")

#defino la función que crea el formulario de forma gráfica
def Loginform():
    global login_screen
    login_screen = Tk()
    #título de la pantalla
    login_screen.title("Formulario de login")
    #tamaño de la pantalla
    login_screen.geometry("300x250")
    login_screen.configure(background="#5CDB95")
    #declarando las variables que se van a usar para recoger los datos
    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Diseñando el layout del formulario
    Label(login_screen,width="300", text="Introduce tus datos", bg="#05386B",fg="#EDF5E1").pack()
    #Label e input del usuario
    Label(login_screen, text="  Usuario", background="#5CDB95").place(x=20,y=40)
    Entry(login_screen, textvariable=username, bg="#EDF5E1").place(x=90,y=42)
    #Label e input de la contraseña
    Label(login_screen, text="Password", background="#5CDB95").place(x=20,y=80)
    Entry(login_screen, textvariable=password ,show="*", bg="#EDF5E1").place(x=90,y=82)
    #Label para los mensajes de [correcto/incorrecto/void]
    Label(login_screen, text="",textvariable=message, background="#5CDB95", fg="#EDF5E1").place(x=75,y=170)
    #Botón de Login("Enter") donde valida con la función programada anteriormente V
    Button(login_screen, text="Enter", width=10, height=1, command=login, background="#05386B", fg="#EDF5E1").place(x=105,y=130)
    login_screen.mainloop()
# #calling function Loginform
# Loginform()