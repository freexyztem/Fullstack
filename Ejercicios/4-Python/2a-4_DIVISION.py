"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
divisor es cero el programa debe mostrar un error."""

# Pedir dos numeros:
a = float(input("Ingrese el dividendo: "))
b = float(input("Ingrese el divisor: "))

# Comprobar que no sea 0 el divisor
if b == 0:
    print("Error! El divisor no puede ser 0")
else:
    print("El resultado es: ", a / b)
