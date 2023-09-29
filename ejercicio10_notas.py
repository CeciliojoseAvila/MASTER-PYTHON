contador = 1
aprobados = 0
suspendidos = 0

numeros_alumnos = int(input("¿Cuántos alumnos tienes?: "))

while contador <= numeros_alumnos:
    nota = int(input(f"¿Qué nota quieres ponerle al \"alumnos{contador}\"?: "))

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

    contador += 1

print(f"\nAlumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")