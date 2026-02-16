"""MAYUSCULA O MINUSCULA
Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es
una mayúscula o una minúscula."""

# Pedir una letra al usuario
letra = input("Ingrese una letra: ")
# condicion para comprobar si es una sola letra
if len(letra) != 1 or not letra.isalpha():
    print("Por favor, ingrese una sola letra del alfabeto latino.")
else:
    # Verificar si la letra es mayuscula o minuscula
    if letra.isupper():
        print("La letra es mayuscula")
    elif letra.islower():
        print("La letra", letra, "es minuscula")
    else:
        print("No se ha ingresado una letra")
