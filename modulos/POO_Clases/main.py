
class Coche:
    # Atributos o propiedades
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Métodos, acciones o funciones del coche

def setColor(self, color):
    self.color = color


def getColor(self):
    return self.color


def setModelo(self, modelo):
    self.modelo = modelo


def getModelo(self):
    return self.modelo


def acelerar(self):
    self.velocidad += 1


def frenar(self):
    self.velocidad -= 1

def getVelocidad(self):
    return self.velocidad

    # Instanciar
coche = Coche()

coche.setColor("amarillo")
coche.setModelo("Murcielago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.getVelocidad())
