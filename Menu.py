import tkinter 
from tkinter import filedialog
import json

class Menu:
    
    def __init__(self, user):
        self.usuario = user
        self.menuScreen = tkinter.Tk()
        self.menuScreen.title("Menú")
        self.menuScreen.geometry("600x300")
        self.perfil = {}
        self.documentos = {}
        
        self.label_primer_nombre = tkinter.Label(self.menuScreen, text="Primer nombre:")
        self.label_primer_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.entry_primer_nombre = tkinter.Entry(self.menuScreen)
        self.entry_primer_nombre.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_segundo_nombre = tkinter.Label(self.menuScreen, text="Segundo nombre (si tiene):")
        self.label_segundo_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.entry_segundo_nombre = tkinter.Entry(self.menuScreen)
        self.entry_segundo_nombre.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_primer_apellido = tkinter.Label(self.menuScreen, text="Primer apellido:")
        self.label_primer_apellido.grid(row=2, column=0, padx=10, pady=10)
        self.entry_primer_apellido = tkinter.Entry(self.menuScreen)
        self.entry_primer_apellido.grid(row=2, column=1, padx=10, pady=10)
        
        self.label_segundo_apellido = tkinter.Label(self.menuScreen, text="Segundo apellido (si tiene):")
        self.label_segundo_apellido.grid(row=3, column=0, padx=10, pady=10)
        self.entry_segundo_apellido = tkinter.Entry(self.menuScreen)
        self.entry_segundo_apellido.grid(row=3, column=1, padx=10, pady=10)
        
        self.label_fecha_nacimiento = tkinter.Label(self.menuScreen, text="Fecha de nacimiento:")
        self.label_fecha_nacimiento.grid(row=0, column=2, padx=10, pady=10)
        self.entry_fecha_nacimiento = tkinter.Entry(self.menuScreen)
        self.entry_fecha_nacimiento.grid(row=0, column=3, padx=10, pady=10)
        
        self.label_nacionalidad = tkinter.Label(self.menuScreen, text="Nacionalidad:")
        self.label_nacionalidad.grid(row=1, column=2, padx=10, pady=10)
        self.entry_nacionalidad = tkinter.Entry(self.menuScreen)
        self.entry_nacionalidad.grid(row=1, column=3, padx=10, pady=10)
        
        self.label_departamento = tkinter.Label(self.menuScreen, text="Departamento:")
        self.label_departamento.grid(row=2, column=2, padx=10, pady=10)
        self.departamento_options = ["Quiché", "Sololá", "Huehuetenango", "Retalhuleu", "El Progreso", "Sacatepéquez"]
        self.departamento_var = tkinter.StringVar(self.menuScreen)
        self.departamento_var.set(self.departamento_options[0])
        self.entry_departamento = tkinter.OptionMenu(self.menuScreen, self.departamento_var, *self.departamento_options)
        self.entry_departamento.grid(row=2, column=3, padx=10, pady=10)
        
        self.label_clima = tkinter.Label(self.menuScreen, text="Clima:")
        self.label_clima.grid(row=4, column=0, padx=10, pady=10)

        self.clima_options = ["Templado", "Frio", "Caliente"]
        self.clima_var = tkinter.StringVar(self.menuScreen)
        self.clima_var.set(self.clima_options[0])
        self.entry_clima = tkinter.OptionMenu(self.menuScreen, self.clima_var, *self.clima_options)
        self.entry_clima.grid(row=4, column=1, padx=10, pady=10)
        
        self.label_identificacion = tkinter.Label(self.menuScreen, text="Identificación:")
        self.label_identificacion.grid(row=3, column=2, padx=10, pady=10)
        
        self.label_archivoSeleccionado = tkinter.Label(self.menuScreen, text="Ningún archivo seleccionado")	
        self.label_archivoSeleccionado.grid(row=3, column=3, columnspan=4, padx=10, pady=10)
                
        self.boton_file = tkinter.Button(self.menuScreen, text="Abrir archivo", command=lambda: self.browse_file(self.label_archivoSeleccionado))
        self.boton_file.grid(row=4, column=3, columnspan=4, padx=10, pady=10)
        
        self.botonContinuar = tkinter.Button(self.menuScreen, text="Continuar", command=self.agregarPerfil)
        self.botonContinuar.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
        
    def browse_file(self, label):
        file_path = filedialog.askopenfilename()
        file = file_path.split("/")[-1]
        if file_path:
            tkinter.messagebox.showinfo("Información", f"El archivo {file_path} se ha cargado correctamente.")
            self.documentos["Identificacion"] = file_path
            label.config(text=file)

    def agregarPerfil(self):
        primer_nombre = self.entry_primer_nombre.get()
        primer_apellido = self.entry_primer_apellido.get()
        fecha_nacimiento = self.entry_fecha_nacimiento.get()
        nacionalidad = self.entry_nacionalidad.get()
        
        if primer_nombre != "" and primer_apellido != "" and fecha_nacimiento != "" and nacionalidad != "" and self.documentos != {}:
            self.perfil["Primer nombre"] = primer_nombre
            self.perfil["Segundo nombre"] = self.entry_segundo_nombre.get()
            self.perfil["Primer apellido"] = primer_apellido
            self.perfil["Segundo apellido"] = self.entry_segundo_apellido.get()
            self.perfil["Fecha de nacimiento"] = fecha_nacimiento
            self.perfil["Nacionalidad"] = nacionalidad
            self.perfil["Departamento"] = self.departamento_var.get()
            self.perfil["Clima"] = self.clima_var.get()
            
            with open("usuarios.json", "r") as file:
                data = json.load(file)
            
            for user in data["users"]:
                if user["user"] == self.usuario:
                    user["perfil"] = self.perfil
                    user["documentos"] = self.documentos
                    break
                
            with open("usuarios.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            tkinter.messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios.")
            
    def menuDocumentos(self):
        self.menuScreen.destroy()
        self.menuScreen = tkinter.Tk()
        self.menuScreen.title("Menú")
        self.menuScreen.geometry("600x300")
        
        self.label_antecedentes_penales = tkinter.Label(self.menuScreen, text="Antecedentes penales:")
        self.label_antecedentes_penales.grid(row=0, column=0, padx=10, pady=10)
        self.label_antecedentes_penales_documento = tkinter.Label(self.menuScreen, text="Ningún archivo seleccionado")
        self.label_antecedentes_penales_documento.grid(row=0, column=1, padx=10, pady=10)
        self.boton_antecedentes_penales = tkinter.Button(self.menuScreen, text="Ingresar documento", command=lambda: self.browse_file(self.label_antecedentes_penales_documento))
        self.boton_antecedentes_penales.grid(row=0, column=2, padx=10, pady=10)

        self.label_antecedentes_policiales = tkinter.Label(self.menuScreen, text="Antecedentes policiales:")
        self.label_antecedentes_policiales.grid(row=1, column=0, padx=10, pady=10)
        self.label_antecedentes_policiales_documento = tkinter.Label(self.menuScreen, text="Ningún archivo seleccionado")
        self.label_antecedentes_policiales_documento.grid(row=1, column=1, padx=10, pady=10)
        self.boton_antecedentes_policiales = tkinter.Button(self.menuScreen, text="Ingresar documento", command=lambda: self.browse_file(self.label_antecedentes_policiales_documento))
        self.boton_antecedentes_policiales.grid(row=1, column=2, padx=10, pady=10)

        self.label_boleto_ornato = tkinter.Label(self.menuScreen, text="Boleto de ornato:")
        self.label_boleto_ornato.grid(row=2, column=0, padx=10, pady=10)
        self.label_boleto_ornato_documento = tkinter.Label(self.menuScreen, text="Ningún archivo seleccionado")
        self.label_boleto_ornato_documento.grid(row=2, column=1, padx=10, pady=10)
        self.boton_boleto_ornato = tkinter.Button(self.menuScreen, text="Ingresar documento", command=lambda: self.browse_file(self.label_boleto_ornato_documento))
        self.boton_boleto_ornato.grid(row=2, column=2, padx=10, pady=10)

        self.label_constancia_laboral = tkinter.Label(self.menuScreen, text="Constancia laboral:")
        self.label_constancia_laboral.grid(row=3, column=0, padx=10, pady=10)
        self.label_constancia_laboral_documento = tkinter.Label(self.menuScreen, text="Ningún archivo seleccionado")
        self.label_constancia_laboral_documento.grid(row=3, column=1, padx=10, pady=10)
        self.boton_constancia_laboral = tkinter.Button(self.menuScreen, text="Ingresar documento", command=lambda: self.browse_file(self.label_constancia_laboral_documento))
        self.boton_constancia_laboral.grid(row=3, column=2, padx=10, pady=10)

        self.label_cartas_recomendacion = tkinter.Label(self.menuScreen, text="Cartas de recomendación:")
        self.label_cartas_recomendacion.grid(row=4, column=0, padx=10, pady=10)
        self.label_cartas_recomendacion_documento = tkinter.Label(self.menuScreen, text="Ningún archivo seleccionado")
        self.label_cartas_recomendacion_documento.grid(row=4, column=1, padx=10, pady=10)
        self.boton_cartas_recomendacion = tkinter.Button(self.menuScreen, text="Ingresar documento", command=lambda: self.browse_file(self.label_cartas_recomendacion_documento))
        self.boton_cartas_recomendacion.grid(row=4, column=2, padx=10, pady=10)

        self.label_presentar_cv = tkinter.Label(self.menuScreen, text="Presentar CV:")
        self.label_presentar_cv.grid(row=5, column=0, padx=10, pady=10)
        self.label_presentar_cv_documento = tkinter.Label(self.menuScreen, text="Ningún archivo seleccionado")
        self.label_presentar_cv_documento.grid(row=5, column=1, padx=10, pady=10)
        self.boton_presentar_cv = tkinter.Button(self.menuScreen, text="Ingresar documento", command=lambda: self.browse_file(self.label_presentar_cv_documento))
        self.boton_presentar_cv.grid(row=5, column=2, padx=10, pady=10)
        
        
Menu("perro")
tkinter.mainloop()
