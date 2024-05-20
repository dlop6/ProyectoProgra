import tkinter as tk
import json
from Estadisticas import Estadisticas

class RecomendacionEscuela:
    def __init__(self, usuario):
        self.usuario = usuario
        self.perfil = None
        self.departamentosDisponibles = []
        self.ventana = tk.Tk()
        self.ventana.resizable(True, True)
        self.ventana.title("Recomendación de escuela")
        self.ventana.geometry("300x200")
        
        self.label_usuario = tk.Label(self.ventana, text="Usuario: " + self.usuario)
        self.label_usuario.pack(pady=10)
        
        self.botonMenuEstadisticas = tk.Button(self.ventana, text="Estadisticas", command= lambda: Estadisticas(self.usuario))
        self.botonMenuEstadisticas.pack(pady=10)
        
        self.label_recomendacion = tk.Label(self.ventana, text="Basado en tu perfil, encontramos estas escuelas para ti")
        self.label_recomendacion.pack(pady=10)
        
        self.boton_recomendar = tk.Button(self.ventana, text="Recomendar escuela", command=self.recomendar)
        self.boton_recomendar.pack(pady=10)
         
        self.boton_salir = tk.Button(self.ventana, text="Salir", command=self.ventana.destroy)
        self.boton_salir.pack(pady=10)
        
        
        self.ajustar_geometria(self.ventana)
        
        self.ventana.mainloop()
        
    def recomendar(self):
            
        with open("data\\usuarios.json", "r") as file:
            dataUsuarios = json.load(file)
            
        for user in dataUsuarios["users"]:
            if user["user"] == self.usuario:
                self.perfil = user["perfil"]
                break
        
        if self.perfil["Clima"] == "Templado":
            self.departamentosDisponibles = ["Quiche", "Solola", "Sacatepequez"]
        elif self.perfil["Clima"] == "Calido":
            self.departamentosDisponibles = ["El Progreso", "Retalhuleu"]
        elif self.perfil["Clima"] == "Frio":
            self.departamentosDisponibles = ["Huehuetenango"]
            
        for departamento in self.departamentosDisponibles:
            boton_departamento = tk.Button(self.ventana, text=departamento, command=lambda dep=departamento: self.mostrar_escuelas(dep))
            boton_departamento.pack(pady=5)
            
    def mostrar_escuelas(self, departamento):
        newScreen = tk.Toplevel(self.ventana)
        newScreen.title("Escuelas en " + departamento)
        newScreen.geometry("300x200")
        
        
        
        with open("data\\escuelas.json", "r") as file:
            dataEscuelas = json.load(file)
        img = tk.PhotoImage(file=f"img/{(departamento).lower()}.png")
        
        # redimensionar imagen 
        img = img.subsample(2)
        
        escuela = dataEscuelas[departamento]
        
        row = 1
        for key, value in escuela.items():
            label_key = tk.Label(newScreen, text=key.title() + ":")
            label_key.grid(row=row, column=1, pady=5, sticky="nsew")
            
            label_value = tk.Label(newScreen, text=value)
            label_value.grid(row=row, column=2, pady=5, sticky="nsew")
            
            row += 1
        
        aplicarButton = tk.Button(newScreen, text="Aplicar", command=lambda: self.aplicar_escuela(escuela))
        aplicarButton.grid(row=row+1, column=1, columnspan=2, pady=10, sticky="nsew")
            
        img_label = tk.Label(newScreen, image=img)
        img_label.grid(row=row+1, column=1, columnspan=2, pady=10, sticky="nsew")
        
        
        self.ajustar_geometria(newScreen)
        self.ventana.mainloop()
        
    
    def ajustar_geometria(self, root):
        root.update_idletasks()
        width = root.winfo_width()  # Obtener el ancho de la ventana
        height = root.winfo_height()  # Obtener la altura de la ventana
        x = (root.winfo_screenwidth() // 2) - (width // 2)  # Calcular la posición x centrada
        y = (root.winfo_screenheight() // 2) - (height // 2)  # Calcular la posición y centrada
        root.geometry(f"{width}x{height}+{x}+{y}")
    
    def aplicar_escuela(self, dataEscuela):
        with open("data\\usuarios.json", "r") as file:
            dataUsuarios = json.load(file)
        
        for user in dataUsuarios["users"]:
            if user["user"] == self.usuario:
                user["Escuela"] = dataEscuela["nombre"]
                break
        
if __name__ == "__main__":
    
    RecomendacionEscuela("perro")
