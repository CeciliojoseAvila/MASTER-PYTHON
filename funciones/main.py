def mostrarNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

mostrarNombre(nombre, edad)