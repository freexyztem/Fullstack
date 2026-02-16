"""Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida
por el usuario de el resultante en dólares.
1. Crea un script que reciba una cantidad de euros del usuario e imprima por pantalla el
correspondiente en dólares (considera una tasa de cambio donde 1 EU = 1.2 $)
2. La casa de cambios se queda un 10% en concepto de 'tasas de gestión'. Calcula el monto
recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
forma que quede claro para el usuario"""

# Inicializar tasa de cambiio
tasa_EURUSD = 1.2

# Introducir la cantidad en euros
monto_EUR = float(input("Introduce la cantidad de Euros: "))

# Mostrar en pantalla el cambio en USD
cambio_USD = monto_EUR * tasa_EURUSD
print(
    "La tasa del EURUSD es de 1.2\nPor",
    monto_EUR,
    "euros son",
    cambio_USD,
    "dolares",
)

# Calcular la tasa de gestion 10%
tasa_gestion = cambio_USD * 0.1
print("la tasa de gestion es:", tasa_gestion, "dolares")

# Calcular el monto recibido en USD
print("El monto que recibiras es de:", cambio_USD - tasa_gestion, "dolares")
