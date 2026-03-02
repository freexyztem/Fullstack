# ingresar lista de datos
estudiantes = [
    {
        "nombre": "Rodolfo",
        "edad": 25,
    },
    {
        "nombre": "Augusto",
        "edad": 23,
    },
]
# mostrar lista de datos
for estudiante in estudiantes:
    print(estudiante)
print("agregar un estudiante")

# agregar un estudiante a la lista de datos y mostrarlo
estudiantes.append({"nombre": "Fernando", "edad": 54})
for estudiante in estudiantes:
    print(estudiante)

del estudiantes[1]
print("eliminar el segundo estudiante:")

# eliminar el segundo estudiantes y mostrarlo

for estudiante in estudiantes:
    print(estudiante)

# actualizar la edad del primer estudiante
estudiantes[0]["edad"] = 15
print("actualizar edad del primer estudiante")
for estudiante in estudiantes:
    print(estudiante)
