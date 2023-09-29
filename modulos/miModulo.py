def holaMundo(nombre):
    return f"Hola mundo que tal, MI NOMBRE ES: {nombre}"

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    Multiplicacion = numero1 * numero2
    Division = numero1 / numero2

    cadena = " "

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"        
        cadena += "Resta: " + str(resta)
        cadena += "\n"     
    else:
        cadena += "Multiplicacion: " + str(Multiplicacion)
        cadena += "\n" 
        cadena += "Division: " + str(Division)   

    return cadena

