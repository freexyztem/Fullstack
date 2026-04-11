"""
1. La función debe ser capaz de manejar textos y ser insensible a
mayúsculas/minúsculas (por ejemplo, "Hola" y "hola" se consideran la
misma palabra).
2. Se deben excluir las palabras comunes (artículos, preposiciones, etc.) que
no aportan información relevante al análisis.
3. Utiliza memoización para evitar recalcular la frecuencia de palabras para el
mismo texto
"""

from functools import lru_cache
from time import time


@lru_cache(maxsize=None)
def quitar_palabras(palabra):
    reservadas = "a ante bajo con contra de desde durante mediante versus via en entre hasta hacia para por sin segun sobre tras pero aunque sino y e ni o u ademas por lo tanto porque entonces el la lo los las un una unos unas"
    reservadas = reservadas.split()
    if palabra in reservadas:
        return True
    else:
        return False


@lru_cache(maxsize=None)
def calcular_frecuencia_palabras(texto):
    """
    tome como entrada un texto y devuelva un diccionario que muestre la
    frecuencia de cada palabra en el texto.
    """
    # Se inicializa el diccionario
    frecuencia = {}

    # Se convierte todo el texto a minusculas
    texto = texto.lower()

    # Separar texto en palabras
    palabras = texto.split(" ")

    # Excluir articulos, preposiciones, conjunciones,
    # Contar palabras
    for palabra in palabras:
        if quitar_palabras(palabra) or len(palabra) <= 3:
            pass
        elif palabra in frecuencia.keys():
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


print(
    calcular_frecuencia_palabras(
        "Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos apilados en orden descendente, desde el disco N en la parte inferior hasta el disco 1 en la parte superior. Tu tarea es implementar una solución recursiva para mover todos los discos desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de Hano"
    )
)
