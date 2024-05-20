import tkinter as tk
from tkinter import messagebox
import pandas as pd
import json
import csv

class MenuAlumnos:
    
    def __init__(self, user):
        self.user = user
        self.alumnosfile = pd.read_csv("data\\usersEstudiantes.csv")
        
        self.window = tk.Tk()
        self.window.title("Menu Alumnos")
        self.window.geometry("300x200")
        
        # Create a label with the welcome message
        welcome_label = tk.Label(self.window, text=f"Bienvenido {self.user}", font=("Arial", 12, "bold"))
        welcome_label.pack()
        
        # Create a button to rate maestros
        rate_button = tk.Button(self.window, text="Calificar Maestros", command=self.rate_maestros)
        rate_button.pack()
        
        # Create an exit button that destroys the window
        exit_button = tk.Button(self.window, text="Salir", command=self.window.destroy)
        exit_button.pack()
        
        self.window.mainloop()
        
    def rate_maestros(self):
        with open("data\\usuarios.json", "r") as file:
            data = json.load(file)
            
        maestros = []
        
        for user in data["users"]:
            maestros.append(user["user"])
            
        # widget con todos los maestros para calificar
        
        self.ratings_window = tk.Toplevel(self.window)
        self.ratings_window.title("Calificar Maestros")
        self.ratings_window.geometry("300x200")
        
        self.escogeMaestro = tk.Label(self.ratings_window, text="Escoge al maestro para calificar") 
        self.escogeMaestro.pack(pady=10)
        
        self.maestro_var = tk.StringVar()
        self.maestro_var.set(maestros[0])
        
        self.maestro_menu = tk.OptionMenu(self.ratings_window, self.maestro_var, *maestros)
        self.maestro_menu.pack(pady=10)
        
        self.calificarLabel = tk.Label(self.ratings_window, text="Calificación (0-10):")
        self.calificarLabel.pack(pady=10)
        
        self.calificacion_var = tk.IntVar()
        self.calificacion_var.set(0)
        
        self.calificacion_menu = tk.OptionMenu(self.ratings_window, self.calificacion_var, *range(11))
        self.calificacion_menu.pack(pady=10)
        
        self.submit_button = tk.Button(self.ratings_window, text="Enviar calificación", command=self.submit_ratings)
        self.submit_button.pack(pady=10)
        
    

    def submit_ratings(self):
        maestro = self.maestro_var.get()
        calificacion = self.calificacion_var.get()
        
        self.alumnosfile.loc[self.alumnosfile['user'] == self.user, ['maestro Calificado', 'rating']] = [maestro, calificacion]
        self.alumnosfile.to_csv("data\\usersEstudiantes.csv", index=False)
        
        messagebox.showinfo("Calificación enviada", f"Se ha enviado la calificación {calificacion} al maestro {maestro}")
        
        
if "__main__" == __name__:
    MenuAlumnos("student1") 

