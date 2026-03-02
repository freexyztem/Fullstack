info = {
    "0000": {"nombre": "Juan Palomillo", "edad": 30, "ciudad": "Madrid"},
    "0001": {"nombre": "Ana García", "edad": 25, "ciudad": "Barcelona"},
    "0002": {"nombre": "Luis Martínez", "edad": 28, "ciudad": "Valencia"},
}
continuar = True
while continuar:
    print("Seleccione una de las siguientes opciones: ")
    print("  1. Mostrar información de un empleado")
    print("  2. Mostrar información de todos los empleados")
    print("  3. Agregar un nuevo empleado")
    print("  4. Eliminar un empleado")
    opcion = input("opción > ")

    if opcion == "1":
        id_empleado = input("Ingrese el ID del empleado: ")
        empleado = info.get(id_empleado)
        if empleado:
            print(f"Nombre: {empleado['nombre']}")
            print(f"Edad: {empleado['edad']}")
            print(f"Ciudad: {empleado['ciudad']}")
        else:
            print("Empleado no encontrado.")
    elif opcion == "2":
        for id_empleado, empleado in info.items():
            print(f"ID: {id_empleado}")
            print(f"Nombre: {empleado['nombre']}")
            print(f"Edad: {empleado['edad']}")
            print(f"Ciudad: {empleado['ciudad']}")
            print("-" * 20)
    elif opcion == "3":
        id_empleado = input("Ingrese el ID del nuevo empleado: ")
        nombre = input("Ingrese el nombre del nuevo empleado: ")
        edad = int(input("Ingrese la edad del nuevo empleado: "))
        ciudad = input("Ingrese la ciudad del nuevo empleado: ")
        info[id_empleado] = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
        print("Empleado agregado exitosamente.")
    elif opcion == "4":
        id_empleado = input("Ingrese el ID del empleado a eliminar: ")
        if id_empleado in info:
            del info[id_empleado]
            print("Empleado eliminado exitosamente.")
        else:
            print("Empleado no encontrado.")
    else:
        continuar = False
