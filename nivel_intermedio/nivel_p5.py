ciudades = {}

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave, valor in opciones.items():
        print(f' {clave}) {valor[0]}')

def leer_opcion(opciones):
    while True:
        opcion = input('Opción: ')
        if opcion in opciones:
            return opcion
        print('Opción incorrecta, vuelva a intentarlo.')

def registrar_ciudad():
    nombre_ciudad = input('Ingrese la primera ciudad: ')
    while True:
        try:
            cantidad_sismos = int(input('Ingrese la cantidad de sismos a registrar para esta ciudad: '))
            if cantidad_sismos > 0:
                ciudades[nombre_ciudad] = [0] * cantidad_sismos
                print(f'Se ha registrado la ciudad \'{nombre_ciudad}\' con {cantidad_sismos} sismos a registrar.')
                break
            print('La cantidad de sismos debe ser mayor que cero.')
        except ValueError:
            print('Ingrese un número válido para la cantidad de sismos.')

def registrar_sismo():
    ciudad = input('Ingrese el nombre de la ciudad para registrar el sismo: ')
    if ciudad in ciudades:
        sismos = ciudades[ciudad]
        for i, sismo in enumerate(sismos):
            while True:
                try:
                    magnitud = float(input(f'Ingrese la magnitud del sismo {i + 1}: '))
                    sismos[i] = magnitud
                    print(f'Sismo {i + 1} registrado para la ciudad \'{ciudad}\' con magnitud {magnitud}.')
                    break
                except ValueError:
                    print('Ingrese un número válido para la magnitud del sismo.')
    else:
        print(f'La ciudad \'{ciudad}\' no ha sido registrada.')

def buscar_sismos_por_ciudad():
    ciudad = input('Ingrese el nombre de la ciudad para ver los sismos registrados: ')
    if ciudad in ciudades:
        sismos = ciudades[ciudad]
        print(f'Sismos registrados para la ciudad \'{ciudad}\':')
        for i, magnitud in enumerate(sismos):
            print(f'  Sismo {i + 1}: Magnitud {magnitud}')
    else:
        print(f'La ciudad \'{ciudad}\' no ha sido registrada.')

def informe_de_riesgo():
    for ciudad, sismos in ciudades.items():
        if sismos:
            promedio = sum(sismos) / len(sismos)
            riesgo = 'Amarillo (Sin riesgo)' if promedio < 2.5 else ('Naranja (Riesgo medio)' if 2.5 <= promedio <= 4.5 else 'Rojo (Riesgo alto)')
            print(f'Ciudad: {ciudad} - Promedio de sismos: {promedio:.2f} - Riesgo: {riesgo}')
        else:
            print(f'Ciudad: {ciudad} - Sin sismos registrados.')

def salir():
    print('Saliendo...')
    exit()

def menu_principal():
    opciones = {
        '1': ('Registrar Ciudad', registrar_ciudad),
        '2': ('Registrar Sismo', registrar_sismo),
        '3': ('Buscar Sismos por ciudad', buscar_sismos_por_ciudad),
        '4': ('Informe de riesgo', informe_de_riesgo),
        '5': ('Salir', salir),
    }

    while True:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        opciones[opcion][1]()
        input('Presione Enter para continuar...')

if __name__ == '__main__':
    menu_principal()
