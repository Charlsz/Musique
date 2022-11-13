from tkinter import *
from tkinter import ttk as ttk


#ventana principal
root = Tk()
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
nombreUsuario = StringVar()
nombreUsuario.set("Carlos")
nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
nombreEntry.grid(column=1,row=1)

passUsuario = StringVar()
passUsuario.set("1234")
passEntry = Entry(mainFrame,textvariable=passUsuario,show="*")
passEntry.grid(column=1,row=2)

#botones
iniciarSesionButton = ttk.Button(mainFrame, text="Iniciar Sesion")
iniciarSesionButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

registerButton = ttk.Button(mainFrame, text="Registrar")
registerButton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)




root.mainloop()