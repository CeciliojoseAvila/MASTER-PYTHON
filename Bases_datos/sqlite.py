import sqlite3

conexion = sqlite3.connect('./bases_datos/pruebas.db')

#crear cursor para poder ejecutar las consultas
cursor = conexion.cursor()

#crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
               "id INTEGER PRIMARY KEY AUTOINCREMENT," +
               "titulo VARCHAR(255), "+
               "descripcion TEXT, "+ 
               "precio int(255)"+
                ")")

#Guardar cambios
conexion.commit()

#Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")
#Guardar cambios
conexion.commit()

""" #Eliminar registros
cursor.execute("DELETE FROM productos") """

#Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen pc", 700),
    ("Telefono movil", "Buen telefono", 140),
    ("Placa base", "Buena placa", 80),
    ("Tablet 15", "Buena tablet", 300)
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

#Actualizar datos
cursor.execute("UPDATE productos SET precio = 800 WHERE precio = 80")

#Listar datos
cursor.execute("SELECT * FROM productos;")
#print(cursor)
productos = cursor.fetchall()
#print(productos)
for producto in productos:
    #print(producto)
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
print("\n")



conexion.close()