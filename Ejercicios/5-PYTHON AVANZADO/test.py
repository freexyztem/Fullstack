import json

filename = "data.json"
data = {
    "it4142": {
        "IT4142-K": "IT4242-K",
        "IT4142-K-R1": "IT4242-K",
        "IT4142-P": "IT4242-P",
    },
    "it4143": {"IT4143-K": "IT4243", "IT4143-K-R1": "IT4243", "IT4143-P": "IT4243"},
}
try:
    with open(filename, "w") as file:
        json.dump(data, file)
        print(f"Datos guardados correctamente en {filename}")
except IOError as e:
    print(f"Error al escribir en el archivo: {e}")
