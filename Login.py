from tkinter import *
from tkinter import messagebox
import json
from Menu import Menu
from RecomendacionEscuela import RecomendacionEscuela
from MenuAlumnos import MenuAlumnos
from MenuPadres import MenuPadres
import pandas as pd
import csv

class Login:
    def __init__(self, ventana):
        """
        Clase que representa la ventana de inicio de sesión.

        Args:
            ventana (Tk): La ventana principal de la aplicación.
        """
        self.ventana = ventana
        self.usuario = None
        
        self.label_titulo = Label(ventana, text="Bienvenido a tu sistema escolar favorito", font=("Arial", 16, "bold"))
        self.label_titulo.pack()
        
        self.ventana.title("Iniciar sesión")
        self.ventana.geometry("440x250")
        
        self.label_usuario = Label(ventana, text="Usuario:")
        self.label_usuario.pack()
        
        self.entry_usuario = Entry(ventana)
        self.entry_usuario.pack()
        
        self.label_password = Label(ventana, text="Contraseña:")
        self.label_password.pack()
        
        self.entry_password = Entry(ventana, show="*")
        self.entry_password.pack()
        
        self.label_tipo_usuario = Label(ventana, text="Tipo de usuario:")
        self.label_tipo_usuario.pack()

        self.opciones_tipo_usuario = ["Padre de Familia", "Maestro", "Estudiante"]
        self.tipo_usuario = StringVar(ventana)
        self.tipo_usuario.set(self.opciones_tipo_usuario[0])

        self.menu_tipo_usuario = OptionMenu(ventana, self.tipo_usuario, *self.opciones_tipo_usuario)
        self.menu_tipo_usuario.pack()
        
        self.boton_login = Button(ventana, text="Iniciar sesión", command=self.login)
        self.boton_login.pack()
        
        self.boton_create_user = Button(ventana, text="Crear usuario", command=lambda: self.createUser(self.tipo_usuario.get()))
        self.boton_create_user.pack()
        
    def login(self):
        """
        Método que se ejecuta al hacer clic en el botón "Iniciar sesión".
        Verifica las credenciales ingresadas por el usuario y autentica al usuario si son válidas.
        """
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        with open("data\\usuarios.json", "r") as file:
            dataMaestros = json.load(file)
        
        with open("data\\usersEstudiantes.csv", "r") as file:
            estudiantesFile = pd.read_csv(file)
        
        try:
            padresFile = pd.read_csv("data\\usuariosPadres.csv")
        except FileNotFoundError:
            print("El archivo de usuarios de padres no se encontró.")
            padresFile = None
        
        if padresFile is not None and padresFile["user"].str.contains(usuario).any():
            MenuPadres(usuario)
            return
        
        elif estudiantesFile is not None and estudiantesFile["user"].str.contains(usuario).any():
            MenuAlumnos(usuario)
        
        elif dataMaestros.get("users"):
            for user in dataMaestros["users"]:
                if user["user"] == usuario and user["password"] == password:
                    print("Usuario autenticado:", usuario)
                    self.usuario = usuario
                    self.ventana.destroy()
                    
                    if user["perfil"] != {} or user["documentos"] != {}:
                        RecomendacionEscuela(usuario)
                    else: 
                        Menu(usuario)
                    
                    break
            else:
                print("Usuario no encontrado o contraseña incorrecta")
            messagebox.showerror("Error de autenticación", "Usuario no encontrado o contraseña incorrecta")
        
            
        else:
            print("No se encontraron usuarios registrados.")
            messagebox.showerror("Error de autenticación", "No se encontraron usuarios registrados.")

        
    def createPadreUser(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        # Nuevo usuario a agregar
        n_usuario = [usuario, password, "", ""]
        
        try:
            # Intentar cargar el archivo CSV de usuarios de padres
            with open("data\\usuariosPadres.csv", "r") as file:
                reader = csv.reader(file)
                data = list(reader)
        except FileNotFoundError:
            # Si el archivo no existe, crear una lista vacía
            data = []
        
        if any(usuario in row for row in data):
            print("El usuario ya existe")
        else:
            # Agregar el nuevo usuario a la lista
            data.append(n_usuario)
            
            # Guardar la lista actualizada en el archivo CSV
            with open("data\\usuariosPadres.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            
            # Mostrar mensaje de confirmación
            messagebox.showinfo("Usuario creado", f"El usuario {usuario} ha sido creado exitosamente, ya puedes iniciar sesión")
    def createStudentUser(self):

        """
        Método para crear un nuevo usuario de estudiante y agregarlo al archivo CSV.
        """
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        # Nuevo usuario a agregar
        nuevo_usuario = [usuario, password, "", ""]
        
        try:
            # Intentar cargar el archivo CSV de usuarios de estudiantes
            with open("data\\usersEstudiantes.csv", "r") as file:
                reader = csv.reader(file)
                data = list(reader)
        except FileNotFoundError:
            # Si el archivo no existe, crear una lista vacía
            data = []
        
        if any(usuario in row for row in data):
            print("El usuario ya existe")
        else:
            # Agregar el nuevo usuario a la lista
            data.append(nuevo_usuario)
            
            # Guardar la lista actualizada en el archivo CSV
            with open("data\\usersEstudiantes.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            
            # Mostrar mensaje de confirmación
            messagebox.showinfo("Usuario creado", f"El usuario {usuario} ha sido creado exitosamente, ya puedes iniciar sesión")
  
    def create_maestro_user(self):
        """
        Método que se ejecuta al hacer clic en el botón "Crear usuario".
        Crea un nuevo usuario con las credenciales ingresadas por el usuario.
        """
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        
        n_usuario = {"user": usuario, "password": password, "perfil": {}, "documentos": {}}

        
        try:
            with open("data\\usuarios.json", "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = {"users": []}

        for user in data["users"]:
            if user["user"] == usuario:
                print("El usuario ya existe")
                break
            else:
                messagebox.showinfo("Usuario creado", f"El usuario {usuario} ha sido creado exitosamente, ya puedes iniciar sesión")
                break
        
        
        data["users"].append(n_usuario)

        # Open the file in write mode and dump the data
        with open("data\\usuarios.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def createUser(self, userType):
        
        if userType == "Padre de Familia":
            self.createPadreUser()
        
        elif userType == "Maestro":
            self.create_maestro_user()
        
        elif userType == "Estudiante":
            self.createStudentUser()
        
    
    def getUsuario(self):
        """
        Método que devuelve el nombre de usuario autenticado.

        Returns:
            str: El nombre de usuario autenticado.
        """
        return self.usuario
