import mysql.connector

# conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"

)
# database="master_python"

# comprobar la conexion
# print(database)

# ejecutar las consultas
cursor = database.cursor(buffered=True)

# Crear base de datos
# cursor.execute("CREATE DATABASE master_python")

# for bd in cursor:
#   print(bd)

# crear tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
        
    )
    """)

""" #verificar la tabla
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table) """

#Insertar datos a la tabla
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel','Astra', 18500)")
#commit para que se puedan guardar los registros

#Registrar varios campos al tiempo
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000)
]
#lo comento para que no se vuelva a ejecutar los registros
#cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
database.commit()

#consultar las db, tablas y sus registros
#cursor.execute("SELECT * FROM vehiculos")
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'") #consultas mas especificas
result = cursor.fetchall()
print("------TODOS MIS COCHES--------")

for coche in result:
    #print(coche)
    print(coche[1], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche= cursor.fetchone()
print(coche) 

""" cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault'")
database.commit()
print(cursor.rowcount, "Borrados!!") 
"""

#Actualizar
cursor.execute("UPDATE vehiculos SET modelo='León' WHERE marca='Seat'")
database.commit()
print(cursor.rowcount, "Actualizados!!")