from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as Messagebox
from user import usuario
from Reproductor import Reproductor
root = Tk()

passUsuario = StringVar()
nombreUsuario = StringVar()
usuarios=[]

'''
def createGUI():
    root.title("MUSIQUE")
    
    root.geometry("1000x600")
    title=Label(root,text="Musique", font=("calibri",20,"bold"),bg="grey",fg="white")  
    title.pack(side="top",fill="x") 

    mainFrame= Frame(root)
    mainFrame.pack(side='bottom')
    mainFrame.config(bg="black")

    #imagen1 = PhotoImage(file ='carpeta.jpg')
    imagen2 = PhotoImage(file ='play.png')
    imagen3 = PhotoImage(file ='pausa.png')
    #imagen4 = PhotoImage(file ='repetir.png')
    #imagen5 = PhotoImage(file ='stop.png')
    imagen6 = PhotoImage(file ='atras.png')
    #imagen7 = PhotoImage(file ='adelante.png')

    #boton1 = Button(mainFrame, image= imagen1)
    #boton1.grid(column=0, row=2, pady=10)
    boton2 = Button(mainFrame, image= imagen2,command=Reproductor.play)
    boton2.grid(column=1, row=2, pady=10)
    boton3 = Button(mainFrame,image= imagen3,command=Reproductor.stop)
    boton3.grid(column=2, row=2, pady=10)
    #boton4 = Button(mainFrame,image= imagen4)
    #boton4.grid(column=3, row=2, pady=10)
    #boton5 = Button(mainFrame, image= imagen5)
    #boton5.grid(column=4, row=2, pady=10)
    atras = Button(mainFrame, image= imagen6,command=Reproductor.back)
    atras.grid(column=5, row=2, pady=10)
    #adelante = Button(mainFrame, image= imagen7)
    #adelante.grid(column=6, row=2, pady=10)






    root.mainloop()
'''




def login_interfaz():
    #ventana principal
    musique = Tk()
    musique.title("Musique")
    musique.iconbitmap('icono_musique.ico')

    #de toda mi ventana, creare una subventada que sera mi main frame
    mainFrame= Frame(musique)
    mainFrame.pack()
    mainFrame.config(width=480,height=320,bg="#FFDFD3")

    #titulos y textoss
    tittle = Label(mainFrame,text="Login usuarios",font="Arial")
    tittle.grid(column=0,padx=10,pady=10,row=0,columnspan=5)

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
    iniciarSesionButton.grid(column=2,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    registerButton = ttk.Button(mainFrame, text="Registrar",command=registrarUsuario)
    registerButton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)

    #salir de login
    exit = ttk.Button(mainFrame, text="Salir", command=musique.destroy)
    exit.grid(column=1,row=4,ipadx=5,ipady=5,padx=10,pady=10)
    musique.mainloop()

def iniciarSesion():
    for user in usuarios:
        if user.nombre==nombreUsuario.get():
            test = user.conectar(passUsuario.get())
            if test:
                Messagebox.showinfo("Conectado",f"Se inicio sesion en [{user.nombre}] exitosamente!")
                nombreUsuario.get()
                passUsuario.get()
            else:
                Messagebox.showerror("Error","password incorrecta")
            break
    else:
        Messagebox.showerror("Error","No existen usuarios con ese nombre")

def registrarUsuario():
    name = nombreUsuario.get()
    password = passUsuario.get()
    newUser = usuario(name,password)
    usuarios.append(newUser)
    Messagebox.showinfo("Registro Exitoso",f"Se registro el usuario [{name}] correctamente!!!")
    nombreUsuario.get()
    passUsuario.get()


if __name__=="__main__":
    user1 = usuario("carlos","1234")
    usuarios.append(user1)
    createGUI()
    #login_interfaz()