# tkinter es un modulo para crear interfaces g de usuarios
from tkinter import *
import os.path

class Programa:

    def  __init__(self):
        self.title = "Interfaz gráfica con python y Cecilio"
        self.icon = './imagen/chek.ico'
        self.icon_alt = '/tkinter/imagen/chek.ico'
        self.size = "770x470"
        self.resizable = False

    def cargar(self):       
        #crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #titulo de la ventana
        ventana.title(self.title)

        #comprobar ruta
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        #mostrar texto en el pograma
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Icono de la ventana
        #ventana.iconbitmap("./tkinter/imagen/chek.ico")
        ventana.geometry(self.size)

        #bolquear el tamaño de la ventana(por el lado que se desee)
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()
            
    def mostrar(self):
        #Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()  


        # Instanciar mi programa
programa = Programa()
programa.cargar()
programa.addTexto("Hola mundo")
programa.addTexto("Desde Tkinter y Python")
programa.addTexto("Soy Cecilio Avila")
programa.addTexto("Bienvenidos al mundo de la programacion")
programa.mostrar()