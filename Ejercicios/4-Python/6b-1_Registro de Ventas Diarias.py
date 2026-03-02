# importar modulos
import os

# Crear un diccionario vacio para los productos de la tienda productos = { producto_1 : [fecha_1 , venta_1], [fecha_2 , venta_2]...}
productos = {}
# Pedir al usuario opcion
exit = False  # Inicializar la salida del bucle
# Mostrar las ventas actuales de todos los productos, por productos, nombre de los productos, Ingresar nuevas ventas
while not (exit):
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[34mSeleccione una de las siguientes opciones: \033[0m")
    print("  1. Mostrar ventas en una fecha de todos los productos")
    print("  2. Mostrar todos los productos")
    print("  3. Mostrar ventas de un solo producto")
    print("  4. Ingresar nuevas ventas de un producto")
    print(f"\033[33m*** {productos} ***\033[0m")
    opcion = input("opción > ")

    # --- 1. Mostrar todas las ventas en una fecha
    if opcion == "1":
        print("Fechas disponibles:")
        datos = productos.values()
        print(type(datos))
        if len(datos) > 0:
            fechas = [fecha for ventas in productos.values() for fecha, _ in ventas]
            print(set(fechas))
            fecha_elegida = input("Elija una fecha: ")  # Pedir fecha elegida
            total_ventas = 0
            for (
                producto
            ) in (
                productos.values()
            ):  # sumar todas las ventas de cada producto en la fecha elegida
                for fecha, venta in producto:
                    if fecha == fecha_elegida:
                        total_ventas += venta
            print(f"Total de ventas en {fecha_elegida}: {total_ventas}")
        else:
            print("\033[31mNo hay datos aun\033[0m")
        input("\033[32m*** Enter para actualizar... ***\033[0m")

    # --- 2. Mostrar  todos los productos
    elif opcion == "2":
        for p in productos.keys():
            print(p)
        input("\033[32m*** Enter para actualizar... ***\033[0m")
    # --- 3. Mostrar ventas de un solo producto
    elif opcion == "3":
        producto = input(
            "Ingrese el producto:"
        )  # Pedir el nombre del producto a visualizar
        resultado = sum([venta for fecha, venta in productos.get(producto, [])])
        print(resultado)
        input("\033[32m*** Enter para actualizar... ***\033[0m")
    elif opcion == "4":
        producto = input(
            "Ingrese el producto:"
        )  # Pedir el nombre del producto a agregar ventas
        fecha = input("Ingrese la fecha: ")
        venta = int(input(f"Ingrese la venta de {producto} para {fecha}: "))
        if producto in productos:
            productos[producto].append([fecha, venta])
        else:
            productos[producto] = [[fecha, venta]]
        input("\033[32m*** Enter para actualizar... ***\033[0m")
    # else:
    # exit = True
