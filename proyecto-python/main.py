"""
proyecto python y Mysql:
-Abrir asistente
-Login o Registro
-Si elegimos registro, creará un usuario en la bbdd
-Si elegimos Login, identifica al usuario y nos preguntará
-Crear nota, mostrar notas, borrarlas.
"""


from usuarios import acciones

print("""
Acciones disponibles:
      1) Registro
      2) Login    
  """)

hazEl = acciones.Acciones()
accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()

""" if accion == "registro":
    print("\nOK!! Vamos a registrarte en el sistema...")

    nombre = input("\n¿Cuál es tu nombre?: ")
    apellidos = input("\n¿Cuales son tus apellidos?: ")
    email = input("\nIngresa tu email: ")
    password = input("\nIngresa tu contraseña: ")
elif accion == "login":
    print("\nVale!! Identificate en el sistema...")
    email = input("\nIngresa tu email: ")
    password = input("\nIngresa tu contraseña: ")
"""