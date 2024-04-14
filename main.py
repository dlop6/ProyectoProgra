
import tkinter
from tkinter import filedialog
from Login import Login

ventana = tkinter.Tk()
ventana.title("")

def main():
    """
    Función principal del programa.
    Crea una ventana de tkinter y muestra la pantalla de inicio de sesión.
    """
    Login(ventana)

ventana.mainloop()
