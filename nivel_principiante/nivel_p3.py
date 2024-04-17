# registro de estudiantes 
import os
os.system('cls')
def registro_estudiantes():
    peso_ideal = (0)
    obesidad_grado_I = (0)
    obesidad_grado_II = (0)
    obesidad_grado_III = (0)
    sobrepeso = (0)
    pordebajodelpeso =(0)

    for i in range(2):
        print(f"\nEstudiante {i+1}:")
        nombre = input('Ingrese el nombre del estudiante: ')
        edad = float(input ('ingrese la edad del estudiantes:'))
        peso = float(input('Ingrese el peso del estudiante en Kg: '))
        altura = float(input('Ingrese la altura del estudiante en metros: '))


        imc = peso / (altura ** 2)

        if imc < 18.5:
            peso_ideal += 1
        elif 18.5 <= imc < 25:
            pass  # Peso ideal
        elif 25 <= imc <=30:
            sobrepeso += 1
        elif 30 <= imc <=35:
            obesidad_grado_I += 1
        elif 35 <= imc <=40:
            obesidad_grado_II += 1
        elif 35 <= imc <=40:
            obesidad_grado_III += 1
        else:
            pordebajodelpeso += 1
    

    print('\nReporte de salud de la comunidad estudiantil:')
    print('a). Estudiantes en peso ideal:', peso_ideal)
    print('b). Estudiantes en obesidad grado I:', obesidad_grado_I)
    print('c). Estudiantes en obesidad grado II:', obesidad_grado_II)
    print('d). Estudiantes en obesidad grado III:', obesidad_grado_III)
    print('e). Estudiantes en sobrepeso:', sobrepeso)
    print('f). Estudiantes se encuentra poor debajo de su peso ideal:',pordebajodelpeso)

# Llamamos a la función para probarla
registro_estudiantes()