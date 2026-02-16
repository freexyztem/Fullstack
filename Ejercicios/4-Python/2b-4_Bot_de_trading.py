# BOT DE TRADING:
"""Un bot de trading está programado para realizar ciertas acciones con respecto a un producto
financiero. Crea un script de manera que dado un precio introducido por el usuario, si el precio del
producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está
entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está
estrictamente por encima de 150 el bot deberá imprimir la orden de vender."""

# Pedir el precio del producto al usuario
precio = float(input("Ingrese el precio del producto: "))
# Verificar el precio del producto y imprimir la orden correspondiente
if precio < 100:
    print("Orden de comprar")
elif precio >= 100 and precio <= 150:
    print("Orden de hold")
else:
    print("Orden de vender")
