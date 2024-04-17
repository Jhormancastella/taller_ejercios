class Dependencia:
    def __init__(can,nombre,):
        can.nombre = nombre
        can.consumo_electricidad = 0  # en kWh
        can.consumo_dispositivos = 0  # en kWh
        can.aparatos_electricos = 0 # en kwh
    def agregar_consumo_electricidad(can, consumo):
        can.consumo_electricidad += consumo

    def agregar_consumo_dispositivos(can, consumo):
        can.consumo_dispositivos += consumo

    def agregar_emisiones_transportes(can, emisiones):
        can.aparatos_electricos += emisiones

    def calcular_emisiones_totales(can, factor_emision_electricidad):
        emisiones_electricidad = can.consumo_electricidad * factor_emision_electricidad
        emisiones_totales = emisiones_electricidad + can.consumo_dispositivos + can.aparatos_electricos
        return emisiones_totales
dependencias = []
def registrar_dependencia():
    nombre = input("Ingrese el nombre de la dependencia: ")
    dependencia = Dependencia(nombre)
    dependencias.append(dependencia)
    print("Dependencia registrada correctamente.")

def registrar_consumo_dependencia():
    nombre_dependencia = input("Ingrese el nombre de la dependencia: ")
    for dependencia in dependencias:
        if dependencia.nombre == nombre_dependencia:
            consumo_electricidad = float(input("Ingrese el consumo de electricidad en kWh: "))
            consumo_dispositivos = float(input("Ingrese el consumo de dispositivos en kWh: "))
            
            dependencia.agregar_consumo_electricidad(consumo_electricidad)
            dependencia.agregar_consumo_dispositivos(consumo_dispositivos)
            print("Consumo registrado correctamente para la dependencia", nombre_dependencia)
            return
    print("La dependencia no se encuentra registrada.")

def ver_CO2_producido():
    for dependencia in dependencias:
        print("Dependencia:", dependencia.nombre)
        print("CO2 producido:", dependencia.calcular_emisiones_totales(factor_emision_electricidad))
        print()

def dependencia_mayor_CO2():
    mayor_emisiones = 0
    dependencia_mayor = None
    for dependencia in dependencias:
        emisiones = dependencia.calcular_emisiones_totales(factor_emision_electricidad)
        if emisiones > mayor_emisiones:
            mayor_emisiones = emisiones
            dependencia_mayor = dependencia.nombre
    if dependencia_mayor:
        print("La dependencia que produce mayor CO2 es:", dependencia_mayor)
    else:
        print("No se han registrado dependencias.")

factor_emision_electricidad = 0.5  # Factor de emisión de electricidad en tCO2eq/kWh

while True:
    print("\nMenú Principal:")
    print("1. Registrar Dependencia")
    print("2. Registrar Consumo por Dependencia")
    print("3. Ver CO2 Producido")
    print("4. Dependencia que Produce Mayor CO2")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_dependencia()
    elif opcion == "2":
        registrar_consumo_dependencia()
    elif opcion == "3":
        ver_CO2_producido()
    elif opcion == "4":
        dependencia_mayor_CO2()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
