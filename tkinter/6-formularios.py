from tkinter import *

ventana = Tk()
ventana.geometry("700x400")

ventana.title("Formularios en Tkinter | Cecilio Avila")

#texto encabezado
encabezado = Label(ventana, text="Formularios en Tkinter | Cecilio Avila")
encabezado.config(
    fg="white",
    bg="darkblue",
    font=("Open Sans", 18),
    padx=10,
    pady=10

)
#encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

# Label para el Campo (nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)


#Campo de texto(nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

# Label para el Campo (apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5)

#Campo de texto(apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

# Label para el Campo (descripcion)
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

#Campo de texto GRANDE(descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=40, 
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15

)

#Campo para BOTON (Enviar)
boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(
   padx=10,
   pady=10,
   bg="green",
   fg="white"

)

ventana.mainloop()