from tkinter import *
from tkinter import ttk as ttk
from user import usuario

root = Tk()
passUsuario = StringVar()
nombreUsuario = StringVar()

def createGUI():
    #ventana principal
    root.title("LOGIN")

    #de toda mi ventana, creare una subventada que sera mi main frame
    mainFrame= Frame(root)
    mainFrame.pack()
    mainFrame.config(width=480,height=320)

    #titulos y textoss
    tittle = Label(mainFrame,text="Login usuarios",font="Arial")
    tittle.grid(column=0,padx=10,pady=10,row=0,columnspan=2)

    nombreLabel = Label(mainFrame,text="Usuario: ")
    nombreLabel.grid(column=0,row=1)
    passLabel = Label(mainFrame, text="Password: ")
    passLabel.grid(column=0,row=2)

    #entradas de texto
    
    nombreUsuario.set("")
    nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
    nombreEntry.grid(column=1,row=1)

    
    passUsuario.set("")
    passEntry = Entry(mainFrame,textvariable=passUsuario,show="*")
    passEntry.grid(column=1,row=2)

    #botones
    iniciarSesionButton = ttk.Button(mainFrame, text="Iniciar Sesion",command=iniciarSesion)
    iniciarSesionButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    registerButton = ttk.Button(mainFrame, text="Registrar",command=registrarUsuario)
    registerButton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    root.mainloop()

def iniciarSesion():
    global passUsuario
    user1.conectar(passUsuario.get())

def registrarUsuario():
    pass


if __name__=="__main__":
    user1 = usuario("carlos","1234")
    createGUI()