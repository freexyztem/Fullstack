"""Crea un script que pida al usuario 3 números diferentes y le indique si alguno de ellos es la suma
de los otros dos"""

# Pedir 3 numeros al usuario
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
# Verificar si alguno de los numeros es la suma de los otros dos
if num1 == num2 + num3:
    print("El numero ", num1, " es la suma de ", num2, " y ", num3)
elif num2 == num1 + num3:
    print("El numero ", num2, " es la suma de ", num1, " y ", num3)
elif num3 == num1 + num2:
    print("El numero ", num3, " es la suma de ", num1, " y ", num2)
else:
    print("Ninguno de los numeros es la suma de los otros dos")
