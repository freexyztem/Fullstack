def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.
    Args:
        n (int): El número del cual se desea calcular el factorial.
    Returns:
        int: El factorial de n.
    Raises:
        ValueError: Si n es un número negativo.
    """
    # caso base
    if n == 0 or n == 1:
        return 1

    # sentencia recursiva
    else:
        return n * factorial(n - 1)


# Caso de uso
numero = 15
factorial = factorial(numero)
print(f"El factorial de {numero} es: {factorial}")
