"""En un restaurante el menú consta de las siguientes opciones:
Ensalada mixta ———————— 12 EU
Sopa de pescado ——————— 10 EU
Dorada al horno ———————— 18 EU
Arroz al curry ————————— 14 EU
Lasaña de carne ——————— 15 EU
Brownie de chocolate ————— 8 EU
Helado ——————————— 6 EU
Refrescos —————————— 5,5 EU
Café ———————————— 3,5 EU
Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
de la cuenta.
"""

# --- Inicializar variables
precio_ensalada_mixta = 12
precio_sopa_de_pescado = 10
precio_dorada_al_horno = 18
precio_arroz_al_curry = 14
precio_lasana_de_carne = 15
precio_brownie_de_chocolate = 8
precio_helado = 6
precio_refrescos = 5.5
precio_cafe = 3.5

# --- Leer datos
print("Ingrese la cantidad de..")
n_ensalada_mixta = int(input("Ensalda mixta: "))
n_sopa_de_pescado = int(input("Sopa de pescado: "))
n_dorada_al_horno = int(input("Dorada al horno: "))
n_arroz_al_curry = int(input("Arroz al curry: "))
n_lasana_de_carne = int(input("Lasaña de carne: "))
n_brownie_de_chocolate = int(input("Brownie de chocolate: "))
n_helado = int(input("Helado: "))
n_refrescos = int(input("Refrescos: "))
n_cafe = int(input("Café: "))

# Sumar todas las cantidades
total = (
    n_ensalada_mixta * precio_ensalada_mixta
    + n_sopa_de_pescado * precio_sopa_de_pescado
    + n_dorada_al_horno * precio_dorada_al_horno
    + n_arroz_al_curry * precio_arroz_al_curry
    + n_lasana_de_carne * precio_lasana_de_carne
    + n_brownie_de_chocolate * precio_brownie_de_chocolate
    + n_helado * precio_helado
    + n_refrescos * precio_refrescos
    + n_cafe * precio_cafe
)
print("El total seria de: $", total)
