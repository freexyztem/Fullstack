# cantidad de decoradores y tipo
cantidad = 10
tipo = "="


def decorador_print(func):
    def wrapper(n, t, nombre):
        cantidad, tipo, texto = func(n, t, nombre)
        print(tipo * cantidad, "Inicio", tipo * cantidad)
        print(texto, nombre)
        print(tipo * cantidad, " Fin  ", tipo * cantidad)
        print()

    return wrapper


@decorador_print
def saludo(n, t, nombre):
    return n, t, "Hola"


@decorador_print
def despedida(n, t, nombre):
    return n, t, "Adiós"


# --- sin usar la sintaxis @ ---


def saludo_sindecorador(n, t, nombre):
    return n, t, "Hola sin decorador"


def despedida_sindecorador(n, t, nombre):
    return n, t, "Adiós sin decorador"


# --- Llamar a las funciones ---

saludo(cantidad, tipo, "Ana")
despedida(cantidad, tipo, "Luis")

saludo_sindecorador = decorador_print(saludo_sindecorador)
despedida_sindecorador = decorador_print(despedida_sindecorador)
saludo_sindecorador(cantidad, tipo, "Ana")
despedida_sindecorador(cantidad, tipo, "Luis")
