"""En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide
los siguientes tiempos:
Hannah Neise: 8 minutos 3 segundos y 10 centésimas
Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
Kimberley Bos: 9 minutos 14 segundos y 3 centésimas
1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas
2. Convierte los tiempos de minutos-segundos-centésimas a segundos
3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en
metros por segundo.
4. Imprime los resultados por pantalla
"""

t_hannah = input("Introduce el tiempo para Hannah Neise: (minutos segundos centésimas)")
t_jackie = input(
    "Introduce el tiempo para Jackie Narracott: (minutos segundos centésimas)"
)
t_kimberley = input(
    "Introduce el tiempo para Kimberley Bos: (minutos segundos centésimas)"
)
# Separa los tiempos en minutos, segundos y centésimas
min1, sec1, cen1 = t_hannah.split()
min2, sec2, cen2 = t_jackie.split()
min3, sec3, cen3 = t_kimberley.split()

# Convierte los tiempos de minutos-segundos-centésimas a segundos
tiempo1 = int(min1) * 60 + int(sec1) + int(cen1) / 100
tiempo2 = int(min2) * 60 + int(sec2) + int(cen2) / 100
tiempo3 = int(min3) * 60 + int(sec3) + int(cen3) / 100

# La pista es de 100 metros, por lo que la velocidad media se calcula dividiendo la distancia entre el tiempo
velocidad1 = 100 / tiempo1
velocidad2 = 100 / tiempo2
velocidad3 = 100 / tiempo3

# Imprime los resultados por pantalla
print("Hannah Neise:", velocidad1, "m/s")
print("Jackie Narracott:", velocidad2, "m/s")
print("Kimberley Bos:", velocidad3, "m/s")
