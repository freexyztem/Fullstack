"""Un ordenador tiene tres usuarios distintos (Alejandro, Naomi y Sergio) y otro usuario invitado.
Haz un script que pida el nombre al usuario y le dé una bienvenida personalizada. Crea el script
de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico.
¿Que ocurre si uno de los usuarios introduce su nombre completamente en minúsculas?¿Y si lo
introduce en mayúsculas? ¿Y si sin querer pone un punto en mitad de su nombre (p.e. nao.mi)?¿Y
si se le cuela una almohadilla (p.e se#rgio)?"""

# inicializar una variable tipo lista con los nombres
users = ["alejandro", "naomi", "sergio"]

# Pedir nombre de usuario
user = input("Introduce tu nombre de usuario: ")

# Normalizar a minusculas el nombre de usuario
user = user.lower()

# Eliminar puntos, almohadillas, comas, slashes
obviar = ",./ !@#$%^&*()_+=-?<>;:[]}'{"
for letra in user:
    if letra in obviar:
        user = user.replace(letra, "")

# Comprobar si existe en users
if user in users:
    print("Hola " + user.title() + ", que bueno verte otra vez")
else:
    print("Bienvenido " + user.title() + "!")
