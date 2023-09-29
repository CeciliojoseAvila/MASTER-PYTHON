from tkinter import *

ventana = Tk()
ventana.geometry("800x500")

ventana.title("Formularios 2 en Tkinter | Cecilio Avila")

#texto encabezado
encabezado = Label(ventana, text="Formularios 2 en Tkinter")

encabezado.config(
    fg="white",
    bg="green",
    font=("Consolas", 20),
    padx=15,
    pady=15
)

encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

#Campo para Check
def mostrarProfesion():
    texto = ""

    if web.get():
        texto += " Al Desarrollo Web"
    
    if movil.get():
        if web.get():
            texto += " y Al Desarrollo móvil"
        else:
            texto += " Al Desarrollo móvil"

    mostrar.config(
        text=texto,
        fg="white", 
        bg="green"
    )

web = IntVar()
movil = IntVar()

Label(ventana, text="¿A qué te dedicas?").grid(row=1, column=0)
Checkbutton(ventana, text="Al Desarrollo Web",variable=web, onvalue=1, offvalue=0, command=mostrarProfesion).grid(row=2, column=0)

Checkbutton(ventana, text="Al Desarrollo Móvil", variable=movil, onvalue=1, offvalue=0, command=mostrarProfesion).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)


#Radio Buttons
def marcar():
    marcado.config(text=opcion.get())
    
opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cuál es tu género?").grid(row=5)
Radiobutton(
    ventana, 
    text="Masculino", value="Masculino", command=marcar,
    variable=opcion
    ).grid(row=6)

Radiobutton(
    ventana, 
    text="Femenino", value="Femenino",
    command=marcar,
    variable=opcion

    ).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)

#Option Menú
def seleccionar():
    seleccionado.config(
        text=opcion.get()
    )
 
opcion = StringVar()
opcion.set("Opcion 1")
Label(ventana, text="Selecciona una opcion").grid(row=5, column=1)

select = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)

ventana.mainloop()