a = 0
print("Suma de numeros enteros, para salir ingresa un numero negativo.")
while True:
    try:
        num = int(input("ingresa un numero: "))
        if num < 0:
            break
        a += num
    except ValueError:
        print("Intenta con un numero valido.")
    else:
        print(f"La suma total es: {a}")
