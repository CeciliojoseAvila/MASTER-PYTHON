from tkinter import *
from tkinter import messagebox as Messagebox

ventana = Tk()

ventana.config(
    bd=70
)

def sacarAlerta():
    Messagebox.showinfo("Alerta", "Hola soy CECILIO JOSE AVILA")

Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()

def salir(nombre):
    resultado = Messagebox.askquestion("Salir", "¿Deseas continuar en la aplicacion?")
    
    if resultado != "yes":
        Messagebox.showinfo("Chao!!", f"Adiós {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("CECILIO AVILA")).pack()

ventana.mainloop()