"""
CALCULADORA:
-Dos campos de texto
-4 botones
-mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox 

ventana = Tk()
ventana.geometry("400x400")

ventana.title("Ejercicio completo con Tkinter | Cecilio Avila")
ventana.config(
    bd=35,
)

def convFloat(numero):
    try:
        result.float(numero)
        mostrarResultado()
    except:
        result = 0
        messagebox.showerror("Error: se require solo numeros", "Ingresa los datos correctamente")
    
    return result

def sumar():   
        resultado.set(convFloat(numero1.get()) + convFloat(numero2.get()))
        mostrarResultado()    
        messagebox.showwarning("Error", "Ingresa los datos correctamente")
   

def restar():
    resultado.set(convFloat(numero1.get()) - convFloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(convFloat(numero1.get()) * convFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(convFloat(numero1.get()) / convFloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado.get()}")
    numero1.set("")
    numero2.set("")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=400, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()


Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text=" ").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()