"""Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas.
(Pista: Necesitarás in If Statement anidado)"""

# Variable con la clave
clave = "u.123"
# Pedir contraseña al usuario
user_pass = input("Ingrese la contraseña")
# Comprobacion Primer intento
if clave == user_pass:
    print("Contraseña Correcta!")
else:
    print("Contraseña Incorrecta!")
    # Segundo intento
    user_pass = input("Intente la contraseña otra vez:")
    if clave == user_pass:
        print("Contraseña Correcta!")
    else:
        print("Contraseña Incorrecta!\nBorrando el Sistema...")
