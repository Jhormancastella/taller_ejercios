def sumar_numeros():
    numeros = []
    for i in range(3):
        while True:
            numero = int(input(f"Ingrese el número positivo {i + 1}: "))
            if numero > 0:
                numeros.append(numero)
                break
            else:
                print("Error: Por favor, ingrese un número entero positivo.")
    print("La sumatoria de los tres números es:", sum(numeros))

sumar_numeros()