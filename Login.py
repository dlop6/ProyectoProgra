from tkinter import *
import json
from Menu import Menu

class Login:
    def __init__(self, ventana):
        self.ventana = ventana
        self.usuario = None
        self.ventana.title("Iniciar sesión")
        self.ventana.geometry("300x200")
        
        self.label_usuario = Label(ventana, text="Usuario:")
        self.label_usuario.pack()
        
        self.entry_usuario = Entry(ventana)
        self.entry_usuario.pack()
        
        self.label_password = Label(ventana, text="Contraseña:")
        self.label_password.pack()
        
        self.entry_password = Entry(ventana, show="*")
        self.entry_password.pack()
        
        self.boton_login = Button(ventana, text="Iniciar sesión", command=self.login)
        self.boton_login.pack()
        
        self.boton_create_user = Button(ventana, text="Crear usuario", command=self.create_user)
        self.boton_create_user.pack()
        
    def login(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        with open("usuarios.json", "r") as file:
            data = json.load(file)
        
        if data["users"]:
            for user in data["users"]:
                if user["user"] == usuario and user["password"] == password:
                    print("Usuario autenticado:", usuario)
                    self.usuario = usuario
                    self.ventana.destroy()
                    Menu(self.getUsuario())
                    
                    break
            else:
                print("Usuario no encontrado o contraseña incorrecta")
        

    def create_user(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        n_usuario = {"user": usuario, "password": password, "perfil": {}, "documentos": {}}

        
        try:
            with open("usuarios.json", "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = {"users": []}

        for user in data["users"]:
            if user["user"] == usuario:
                print("El usuario ya existe")
                break
        
        
        data["users"].append(n_usuario)

        # Open the file in write mode and dump the data
        with open("usuarios.json", "w") as file:
            json.dump(data, file, indent=4)
        
        print("Nuevo usuario creado:")
        print("Usuario:", usuario)
        print("Contraseña:", password)
    
    def getUsuario(self):
        return self.usuario
