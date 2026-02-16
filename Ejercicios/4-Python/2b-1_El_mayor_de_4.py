# Pedir 4 numeros al usuario
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
num4 = float(input("Ingrese el cuarto numero: "))
# imprimir el mayor de los 4 numeros
if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print("El mayor numero es: ", num1)
        else:
            print("El mayor numero es: ", num4)
    else:
        if num3 > num4:
            print("El mayor numero es: ", num3)
        else:
            print("El mayor numero es: ", num4)
else:
    if num2 > num3:
        if num2 > num4:
            print("El mayor numero es: ", num2)
        else:
            print("El mayor numero es: ", num4)
    else:
        if num3 > num4:
            print("El mayor numero es: ", num3)
        else:
            print("El mayor numero es: ", num4)
