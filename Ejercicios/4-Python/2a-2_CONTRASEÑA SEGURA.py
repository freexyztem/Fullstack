"""Por motivos de seguridad una contraseña debe tener una vocal en minúscula, dos símbolos
especiales diferentes (pueden ser solo * o #). Dada una contraseña ingresada por el usuario,
comprueba si es una contraseña segura e indícalo por pantalla."""

# Pedir copntraseña
contraseña = input("Ingrese su contraseña: ")

# Inicializar caracteres especiales y vocales minusculas
especiales = "*#/-.,;:!@#$%^&*()_+=-?<>[]}{"
vocales = "aeiou"
result = ""

# Inicializar variables en False para comprobar luego
tiene_vocal, tiene_especiales, especial = False, False, ""

# Comprobar que contraseña al menos tenga 2 caracteres de la lista de especiales y una vocal en minuscula
for letra in contraseña:
    if letra in especiales and especial == "":
        especial = letra
        result += letra
    elif letra in especiales:
        tiene_especiales = True
        result += letra
    if letra in vocales:
        vocal = True
        result += letra

# imprimir resultado si es segura o no
if vocal and especial:
    print("La contraseña es segura!")
    print(result)
else:
    print("Advertencia, La contraseña es insegura!")
