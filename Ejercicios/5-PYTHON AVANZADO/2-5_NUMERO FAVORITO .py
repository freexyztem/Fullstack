"""
Escribe un programa que solicite al usuario su número favorito. Utiliza
json.dump() para almacenar este número en un archivo. Escribe un
programa separado que lea este valor e imprima el mensaje: "Sé cuál es tu
número favorito… Es ____.” Combina ambos programas en un solo archivo
(puedes crear tantas funciones como necesites). Si el número ya está
almacenado, muestra el número favorito al usuario. Si no lo está, solicita al
usuario su número favorito y guárdalo en un archivo. Ejecuta el programa al
menos dos veces para asegurarte de que funciona correctamente.
"""

# importar modulos
import json

# guardar variables
file_name = "fav.json"


def write_file(favorito, f_name):
    """
    escribe en un archivo json el contenido de la variable de entrada
    input:
        favorito(int) el número favorito
        f_name(str) el nombre del archivo a escribir
    """
    try:
        with open(f_name, "w") as f:
            json.dump(favorito, f)
    except FileNotFoundError:
        print("No ha sido posible guardar el archivo")
    else:
        print(
            "el numero", favorito["numero_favorito"], "ha sido guardado correctamente"
        )


try:
    fav = int(input("Introduce tu numero favorito: "))
except ValueError:
    print("No ingreso un NUMERO")
else:
    write_file(dict(numero_favorito=fav), file_name)
