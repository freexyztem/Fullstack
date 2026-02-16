"""En una obra es necesario construir para el tejado de una casa una estructura triangular con tres
piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir
este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo
con esas piezas.
(Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para
todas las posibles combinaciones)"""

# Pedir 3 numeros al usuario
num1 = float(input("Ingrese la longitud de la primera pieza: "))
num2 = float(input("Ingrese la longitud de la segunda pieza: "))
num3 = float(input("Ingrese la longitud de la tercera pieza: "))
# Verificar si se puede construir un triangulo con las piezas
if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
    print("Se puede construir un triangulo con las piezas")
else:
    print("No se puede construir un triangulo con las piezas")
