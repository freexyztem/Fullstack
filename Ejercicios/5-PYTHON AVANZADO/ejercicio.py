class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self._numero_cuenta = numero_cuenta  # atributo protegido
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad de depósito no válida.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("Cantidad de retiro no válida.")


# Ejemplo de uso

cuenta = CuentaBancaria("123456789", 1000)
print(
    cuenta._numero_cuenta
)  # Acceso al número de cuenta a través del atributo protegido
print(cuenta._CuentaBancaria__saldo)  # Intento de acceso directo al saldo

print(cuenta.get_saldo())  # Acceso al saldo a través del método getter
cuenta.depositar(500)  # Depósito de dinero
cuenta.retirar(200)  # Retiro de dinero
print(cuenta.get_saldo())  # Verificación del saldo después de las operaciones
