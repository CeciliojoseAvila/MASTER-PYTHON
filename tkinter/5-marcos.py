from tkinter import *

ventana = Tk()
ventana.title("Marcos | Máster en Python")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue"
)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT, anchor=SW)

marco.pack_propagate(False)
#Label(marco, text="Primer texto en marco con Tkinter").pack()
Label(marco, text="Primer texto en marco con Tkinter").pack(side=BOTTOM, anchor=CENTER)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue"
)
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco.pack_propagate(False)
#Label(marco, text="Primer texto en marco con Tkinter").pack()
texto = Label(marco, text="Segundo texto en marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial",10)  
    
)
texto.pack( )

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="blue",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="orange",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT)

ventana.mainloop()