class Producto:
    def __init__(sn, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
        sn.codigo = codigo
        sn.nombre = nombre
        sn.valor_compra = valor_compra
        sn.valor_venta = valor_venta
        sn.stock_minimo = stock_minimo
        sn.stock_maximo = stock_maximo
        sn.proveedor = proveedor
        sn.stock_actual = 0  # Se inicializa el stock actual en cero

class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, producto):
        self.productos.append(producto)
        print("Producto registrado con éxito.")

    def visualizar_productos(self):
        if self.productos:
            for producto in self.productos:
                print("Código:", producto.codigo)
                print("Nombre:", producto.nombre)
                print("Valor de compra:", producto.valor_compra)
                print("Valor de venta:", producto.valor_venta)
                print("Stock mínimo:", producto.stock_minimo)
                print("Stock máximo:", producto.stock_maximo)
                print("Proveedor:", producto.proveedor)
                print()
        else:
            print("No hay productos registrados en el inventario.")

    def actualizar_stock(self, codigo, cantidad):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.stock_actual += cantidad
                if producto.stock_actual < 0:
                    producto.stock_actual = 0  # No permitir stock negativo
                print("Stock actualizado para el producto", producto.nombre)
                print("Nuevo stock:", producto.stock_actual)
                break
        else:
            print("Producto no encontrado.")

    def generar_informe_critico(self):
        productos_criticos = [producto for producto in self.productos if producto.stock_actual < producto.stock_minimo]
        if productos_criticos:
            print("Productos críticos:")
            for producto in productos_criticos:
                print("Código:", producto.codigo)
                print("Nombre:", producto.nombre)
                print("Stock actual:", producto.stock_actual)
                print()
        else:
            print("No hay productos críticos en el inventario.")

    def calcular_ganancia_potencial(self):
        ganancia_total = sum((producto.valor_venta - producto.valor_compra) * producto.stock_actual for producto in self.productos)
        print("Ganancia potencial total:", ganancia_total)


def main():
    inventario = Inventario()
    
    while True:
        print("Menú de opciones:")
        print("1. Registrar Producto")
        print("2. Visualizar Productos")
        print("3. Actualizar Stock")
        print("4. Generar Informe de Productos Críticos")
        print("5. Calcular Ganancia Potencial")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            inventario.visualizar_productos()
        elif opcion == "3":
            actualizar_stock(inventario)
        elif opcion == "4":
            inventario.generar_informe_critico()
        elif opcion == "5":
            inventario.calcular_ganancia_potencial()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


def registrar_producto(inventario):
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    valor_compra = validar_float_input("Ingrese el valor de compra del producto: ")
    valor_venta = validar_float_input("Ingrese el valor de venta del producto: ")
    stock_minimo = validar_int_input("Ingrese el stock mínimo permitido: ")
    stock_maximo = validar_int_input("Ingrese el stock máximo permitido: ")
    proveedor = input("Ingrese el nombre del proveedor del producto: ")
    producto = Producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor)
    inventario.registrar_producto(producto)


def actualizar_stock(inventario):
    codigo = input("Ingrese el código del producto: ")
    cantidad = validar_int_input("Ingrese la cantidad a agregar o restar al stock: ")
    inventario.actualizar_stock(codigo, cantidad)


def validar_float_input(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")


def validar_int_input(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


if __name__ == "__main__":
    main()
