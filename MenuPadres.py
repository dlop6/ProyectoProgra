import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MenuPadres:
    
    def __init__(self, usuario):
        self.usuario = usuario
        self.ventana = tk.Tk()
        self.padresfile = pd.read_csv("data\\usuariosPadres.csv")
        
        self.ventana.title("Menú de Padres")
        self.ventana.geometry("300x200")
        
        self.label_usuario = tk.Label(self.ventana, text="Usuario: " + self.usuario)
        self.label_usuario.pack(pady=10)
        
        self.calificarEscuela = tk.Button(self.ventana, text="Calificar Escuela", command=self.calificar_escuela)
        self.calificarEscuela.pack(pady=10)
        
        self.graficaCalificaciones = tk.Button(self.ventana, text="Ver gráfica de calificaciones", command=self.grafica_calificaciones)  
        self.graficaCalificaciones.pack(pady=10)
        
        self.boton_salir = tk.Button(self.ventana, text="Salir", command=self.ventana.destroy)
        self.boton_salir.pack(pady=10)
        
        self.ventana.mainloop()
        
    
    def calificar_escuela(self):
        calificacionWindow = tk.Toplevel(self.ventana)
        calificacionWindow.title("Calificar Escuela")
        calificacionWindow.geometry("250x300")
        
        escuelas = ["Escuela Barrio Norte", "Escuela de Chuisamayac", "EORM FRANCISCA MERIDA DE CHAVEZ",
                    "Escuela de La Reforma","Escuela Oficial Urbana Mixta Pablo Jimenez Cruz",
                    "Escuela Oficial Urbana Mixta Estados Unidos de America"
                    ]
        
        self.label_escuela = tk.Label(calificacionWindow, text="Escoge la escuela para calificar")
        self.label_escuela.pack(pady=10)
        
        self.escuela_var = tk.StringVar()
        self.escuela_var.set(escuelas[0])
        
        self.escuela_menu = tk.OptionMenu(calificacionWindow, self.escuela_var, *escuelas)
        self.escuela_menu.pack(pady=10)
        
        self.label_calificacion = tk.Label(calificacionWindow, text="Calificación (0-10):")
        self.label_calificacion.pack(pady=10)
        
        self.calificacion_var = tk.IntVar()
        self.calificacion_var.set(0)

        self.calificacion_menu = tk.OptionMenu(calificacionWindow, self.calificacion_var, *range(11))
        self.calificacion_menu.pack(pady=10)

        self.boton_subir = tk.Button(calificacionWindow, text="Subir calificación", command=lambda: self.calificar(self.escuela_var.get(), calificacionWindow))
        self.boton_subir.pack(pady=10)
    
    def calificar(self, escuela: str, window):
        # Acá se debe actualizar el archivo CSV con la calificación de la escuela
        row_index = self.padresfile.loc[self.padresfile['user'] == self.usuario].index[0]

        # se actualiza la calificación de la escuela
        self.padresfile.at[row_index, 'escuela'] = escuela
        self.padresfile.at[row_index, 'rating'] = self.calificacion_var.get()

        # Save the updated dataframe to the CSV file
        self.padresfile.to_csv("data\\usuariosPadres.csv", index=False)
        messagebox.showinfo("Calificación guardada", "Tu calificación ha sido guardada exitosamente.")
        
        # destroy window
        
        window.destroy()
        
        
    def grafica_calificaciones(self):
        # Load data into a DataFrame
        df = pd.read_csv("data\\usuariosPadres.csv")

        # Create the boxplot using seaborn
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='escuela', y='rating', data=df)
        plt.title('Boxplot of Ratings by School')
        plt.xlabel('School')
        plt.ylabel('Rating')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        
        
if "__main__" == __name__:
    MenuPadres("padre1")
