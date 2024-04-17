import os
os.system('cls')
numeros = []
numero = int(input('Ingrese un número entero positivo (o ingrese un numero negativo para finalizar): '))

while numero >= 0:
    numeros.append(numero)
    numero = int(input('Ingrese otro número entero positivo (o ingrese un numero negativo para finalizar): '))
if not numeros:
    print('No se ingresaron números.')
else:
    total_numeros = len(numeros)
    total_pares = sum(1 for num in numeros if num % 2 == 0)
    total_impares = total_numeros - total_pares
    suma_pares = sum(num for num in numeros if num % 2 == 0)
    suma_impares = sum(num for num in numeros if num % 2 != 0)
    promedio_pares = suma_pares // total_pares if total_pares > 0 else 0
    promedio_impares = suma_impares // total_impares if total_impares > 0 else 0
    menores_10 = sum(1 for num in numeros if num < 10)
    entre_20_y_50 = sum(1 for num in numeros if 20 <= num <= 50)
    mayores_100 = sum(1 for num in numeros if num > 100)
    
    print('Reporte:')
    print('a. Total de números ingresados:', total_numeros)
    print('b. Total de números pares ingresados:', total_pares)
    print('c. Promedio de los números pares:', promedio_pares)
    print('d. Promedio de los números impares:', promedio_impares)
    print('e. Cuantos números son menores que 10:', menores_10)
    print('f. Cuantos números están entre 20 y 50:', entre_20_y_50)
    print('g. Cuantos números son mayores que 100:', mayores_100)