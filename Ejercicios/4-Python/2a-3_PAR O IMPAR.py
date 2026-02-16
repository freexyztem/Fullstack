"""Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa
potencia es par o impar. (Pista: los números pares tiene resto = 0 al dividirlos por 2)
"""

# Insertar dos numeros
base = int(input("introduce la base: "))
potencia = int(input("introduce la potencia: "))

# comprobar que la potencia sea multiplo de 2
if base**potencia % 2 == 0:
    print("Es Par ")
else:
    print("Es impar")
