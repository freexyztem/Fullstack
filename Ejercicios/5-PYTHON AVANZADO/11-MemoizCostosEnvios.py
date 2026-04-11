from functools import lru_cache
from time import time


@lru_cache(maxsize=None)
def calcular_costo_envio(destino, distancia_km, peso_kg):
    costo_base = 5.0
    costo_km = 0.1
    costo_kg = 0.2
    costo_total = costo_base + costo_km * distancia_km + costo_kg * peso_kg
    return destino, costo_total


inicio1 = time()
print(calcular_costo_envio("Destino 1", 150, 2.5))
print(calcular_costo_envio("Destino 2", 100, 4.5))
fin1 = time()

inicio2 = time()
print(calcular_costo_envio("M Destino 1", 150, 2.5))
print(calcular_costo_envio("M Destino 2", 100, 4.5))
fin2 = time()


tiempo1 = fin1 - inicio1
tiempo2 = fin2 - inicio2
print(
    "Tiempo1: ", tiempo1, "Tiempo2 con Mem: ", tiempo2, "Diferencia:", tiempo2 - tiempo1
)
