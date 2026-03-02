# importar modulos
import numpy as np

# datos de peliculas en un array numpy
peliculas = np.array(
    [
        ["Peli 1", "Comedia", 120, 1990, 8.5],
        ["Peli 2", "Acción", 110, 2005, 7.8],
        ["Peli 3", "Drama", 95, 2010, 6.9],
        ["Peli 4", "Comedia", 100, 1985, 7.5],
        ["Peli 5", "Acción", 130, 2015, 8.1],
        ["Peli 6", "Drama", 115, 2000, 6.7],
        ["Peli 7", "Comedia", 90, 1995, 8.2],
        ["Peli 8", "Acción", 105, 2010, 7.4],
        ["Peli 9", "Drama", 125, 1980, 6.8],
        ["Peli 10", "Comedia", 95, 2000, 8.0],
    ]
)
print(peliculas)
# --- genero mas popular ---

# se selecciona la columna de generos y se cuentan las ocurrencias de cada genero
generos, conteo = np.unique(peliculas[:, 1], return_counts=True)

# se ordenan los conteos de mayor a menor y se obtiene el indice del genero mas popular
conteos = np.argsort(conteo)[::-1]

# se obtiene el genero mas popular usando el indice 0 del arreglo ordenado descendentemente
genero_mas_popular = generos[conteos[0]]

# imprime el genero mas popular
print("Género más popular:", genero_mas_popular)


# --- agrupamos las peliculas por decadas ---

# se selecciona la columna de años y se agrupan por decadas usando floor division y multiplicacion para obtener el año de la decada con np.unique
decadas, conteo_decadas = np.unique(
    (peliculas[:, 3].astype(int) // 10) * 10, return_counts=True
)

# se imprime el resultado de las decadas y su conteo
print("Décadas y conteo de películas:")
for decada, conteo in zip(decadas, conteo_decadas):
    print(f"{decada}s: {conteo} películas")
