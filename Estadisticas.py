import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import json

class Estadisticas:
    
    def __init__(self, user):
        self.root = tk.Tk()
        self.usuario = user
        self.root.title("Estadisticas")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        with open("data\\usuarios.json", "r") as file:
            self.data = json.load(file)
            
        with open("data\\Escuelas.json", "r") as file:
            self.escuelas_data = json.load(file)
            
        self.estudiantes_data = pd.read_csv("data\\estudiantes.csv")
        
        self.label = tk.Label(self.root, text="Estadisticas", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)
        
        self.estEdadMaestros = tk.Button(self.root, text="Estadisticas de edad de maestros", command=self.estadisticas_edad_maestros)
        self.estEdadMaestros.pack(pady=10)
        
        self.EST_edad_alumnos = tk.Button(self.root, text="Estadisticas de edad de alumnos", command=self.estadisticas_alumnos)
        self.EST_edad_alumnos.pack(pady=10)
        
        self.ratingApp = tk.Button(self.root, text="Calificar  App", command=self.rating_app)
        self.ratingApp.pack(pady=10)
        
        self.mi_Calificacion = tk.Button(self.root, text="Mi calificación", command=self.mi_calificacion)
        self.mi_Calificacion.pack(pady=10)
        
        
        self.root.mainloop()
        
    def estadisticas_edad_maestros(self):
        with open('data\\usuarios.json', 'r') as file:
            data = json.load(file)

        # Extract relevant data
        users = data["users"]
        user_list = []

        for user in users:
            perfil = user.get("perfil", {})
            if perfil:
                escuela = user.get("Escuela", "Unknown")
                edad = perfil.get("Edad")
                if edad:
                    user_list.append({"Escuela": escuela, "Edad": int(edad)})

        # Create a DataFrame
        df = pd.DataFrame(user_list)

        # Group by "Escuela" and calculate the average "Edad"
        avg_age_per_school = df.groupby("Escuela")["Edad"].mean()

        # Plot the results
        avg_age_per_school.plot(kind='bar', color='skyblue')
        plt.title('Average Age for Each School')
        plt.xlabel('School')
        plt.ylabel('Average Age')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        
    def estadisticas_alumnos(self):
        
        df = pd.DataFrame(self.estudiantes_data)
        
        plt.figure(figsize=(10, 6))
        plt.boxplot([df[df['Escuela'] == escuela]['Edad'] for escuela in df['Escuela'].unique()], vert=False)
        plt.title('Distribución de Edades por Escuela')
        plt.xlabel('Edad')
        plt.ylabel('Escuela')
        plt.yticks(range(1, len(df['Escuela'].unique()) + 1), df['Escuela'].unique())
        plt.tight_layout()
        plt.show()
    
    def rating_app(self):
        
        def guardar_calificacion(calificacion):
            try:
                calificacion = float(calificacion)
                if calificacion < 0 or calificacion > 10:
                    raise ValueError
            except ValueError:
                tk.messagebox.showerror("Error", "La calificación debe ser un número entre 0 y 10.")
                return
            
            for user in self.data["users"]:
                if user["user"] == self.usuario:
                    user["Rating App"] = calificacion
                    break
            
            messagebox.showinfo("Calificación guardada", "Tu calificación ha sido guardada exitosamente.")
            
            ratingWindow.destroy()
        
        
        ratingWindow = tk.Toplevel(self.root)
        
        ratingWindow.title("Calificación de la App")
        ratingWindow.geometry("300x200")
        
        ratingLabel = tk.Label(ratingWindow, text="Introduce tu calificación (0-10):")
        ratingLabel.pack(pady=10)

        ratingEntry = tk.Entry(ratingWindow)
        ratingEntry.pack(pady=10)

        ratingButton = tk.Button(ratingWindow, text="Guardar calificación", command=lambda: guardar_calificacion(ratingEntry.get()))
        ratingButton.pack(pady=10)
        
    def mi_calificacion(self):
        
        df = pd.read_csv("data\\usersEstudiantes.csv")
        
        maestrodf = df[df["maestro Calificado"] == self.usuario]
        avg_rating = maestrodf["rating"].mean() 
        
        messagebox.showinfo("Calificación", f"Tu calificación promedio es: {avg_rating}")
        
        
        
       
if "__main__" == __name__:
    Estadisticas("user10")


        
    
    