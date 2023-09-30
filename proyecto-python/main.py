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
      1) registro
      2) login    
  """)

hazEl = acciones.Acciones()
accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()

