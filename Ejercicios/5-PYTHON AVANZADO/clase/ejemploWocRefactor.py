from abc import ABC, abstractmethod


class ManejadorPedidos(ABC):
    @abstractmethod
    def realizar_pedido(self, detalles):
        pass


class PedidoParaLlevar(ManejadorPedidos):
    def realizar_pedido(self, detalles):
        print(f"Procesando pedido para llevar: {detalles}")


class PedidoLocal(ManejadorPedidos):
    def realizar_pedido(self, detalles):
        print(f"Procesando pedido para comer en local: {detalles}")


class PedidoEntregaADomicilio(ManejadorPedidos):
    def realizar_pedido(self, detalles):
        print(f"Procesando pedido para entrega a domicilio: {detalles}")


class PedidoEspecial(ManejadorPedidos):
    def realizar_pedido(self, detalles):
        print(f"Procesando pedido para evento especial: {detalles}")


class Restaurante:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.manejadores_pedido = []

    def registrar_pedidos(self, manejador):
        self.manejadores_pedido.append(manejador)

    def realizar_pedido(self, detalles):
        for manejador in self.manejadores_pedido:
            manejador.realizar_pedido(detalles)

    def mostrar_pedidos(self):
        print("pedidos registrados:")
        for manejador in self.manejadores_pedido:
            print(f"- {manejador.__class__.__name__}")


# Ejemplo de uso
restaurante = Restaurante("Mi Restaurante de pastas")
restaurante.registrar_pedidos(PedidoParaLlevar())
restaurante.registrar_pedidos(PedidoLocal())
restaurante.registrar_pedidos(PedidoEspecial())
restaurante.realizar_pedido("Pasta al pesto para llevar")
restaurante.realizar_pedido("Pasta grande para comer en local")
restaurante.realizar_pedido("Pasta al pesto para evento especial")
restaurante.mostrar_pedidos()
