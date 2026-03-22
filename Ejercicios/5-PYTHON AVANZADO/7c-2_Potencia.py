def potencia(base, exponente):
    """Calcula la potencia de un número.
    Inputs:
        base (int): La base de la potencia.
        exponente (int): El exponente de la potencia.
    Outputs:
        int: El resultado de elevar la base al exponente.
    """

    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


# Caso de uso
base = 2
exponente = 64
resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es: {resultado}")
