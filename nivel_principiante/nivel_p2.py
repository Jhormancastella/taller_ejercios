# ejercicio de imc de los estudiantes
import os
os.system('cls')
def calcular_imc():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    peso = float(input("Ingrese el peso del estudiante en kg: "))
    altura = float(input("Ingrese la altura del estudiante en metros: "))
    imc = (peso // (altura ** 2))
    print("Nombre del estudiante:", nombre)
    print("Edad del estudiante:", edad)
    print("IMC del estudiante:",imc)
    if 18.5 <= imc < 25:
        print("Categoría: NORMAL")
    elif 25 <= imc < 30:
        print("Categoría: SOBREPESO")
    elif 30 <= imc < 35:
        print("Categoría: OBESIDAD grado I")
    elif 35 <= imc < 40:
        print("Categoría: OBESIDAD grado II")
    else:
        print("Categoría: OBESIDAD grado III") 

# Ejecutar la función
calcular_imc()