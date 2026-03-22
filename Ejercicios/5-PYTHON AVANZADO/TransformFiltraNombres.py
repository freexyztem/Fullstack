lista_nombres = [
    "Perez,Juan",
    "lopez,Maria",
    "Garcia,Jose",
    "Martin,Ana",
    "Lea,Kho",
    "Gonzalez,Alexi",
]


def filtrar_nombres(lista_nombres_transformados):
    def nombre_valido(nombre):
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        return sum(1 for letra in nombre if letra in vocales) >= 2 and len(nombre) > 10

    return [nombre for nombre in lista_nombres_transformados if nombre_valido(nombre)]


# Lista de nombres transformados a un nuevo formato
lista_nombres_transformados = [
    (
        lambda nombre_original: nombre_original.split(",")[1]
        + " "
        + nombre_original.split(",")[0]
    )(nombre_original)
    for nombre_original in lista_nombres
]
lista_nombres_filtrados = filtrar_nombres(lista_nombres_transformados)
print(lista_nombres_filtrados)
