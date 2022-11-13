class usuario():

    numUsuarios = 0
    
    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contra = contra

        self.conectado = False
        self.intentos = 3

        usuario.numUsuarios=+1

    def conectar(self,password=None):
        if password==None:
            myContra = input("ingresa tu password: ")
        else:
            myContra = password
        if myContra==self.contra:
            print("se ha conectado")
            self.conectado = True
            return True
        else:
            self.intentos-=1
            if self.intentos > 0:
                print("password incorrecta, intentelo otra vez: ")
                if password!=None:
                    return False
                print("intentos restantes: ", self.intentos)
                self.conectar()
            else:
                print("No se pudo iniciar sesion, hasta luego")
    
    def desconectar(self):
        if self.conectado:
            print("se ha cerrado sesion")
            self.conectado = False
        else:
            print("No ha iniciado sesion")
    
    def __str__(self):
        if self.conectado:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"mi nombre de usuario es {self.nombre} y estoy {conect}"

"""
user1 = usuario(input("escribe tu usuario: "),input("escribe tu password: "))
print(user1)

user1.conectar()
print(user1)

user1.desconectar()
print(user1)
"""
