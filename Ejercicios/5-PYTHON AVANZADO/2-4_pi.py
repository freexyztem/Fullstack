"""
Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y
en que posición. Puedes usar find()).
Puedes usar el archivo pi_10000.txt
"""

fecha = "1986"
file_name = "pi_10000.txt"
print(f"Fecha: {fecha} en  Pi")
# Intentar abrir el archivo y leerlo
try:
    with open(file_name) as pi:
        numeros = pi.read()
        print("archivo leido correctamente")
except FileNotFoundError:
    print("Archivo  no encontrado")
    # en caso de que lo pueda abrir:
else:

    # imprimir la posicion de fecha en numeros
    if numeros.find(fecha) != -1:
        posicion = numeros.find(fecha)
        print("Se encontro en la posición", posicion)
    else:
        print("Fecha no encontrada")
