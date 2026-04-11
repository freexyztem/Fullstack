class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar_pedido(self, tipo_pedido, detalles):
        if tipo_pedido == "para_llevar":
            print(f"Procesando pedido para llevar: {detalles}")
        elif tipo_pedido == "comer_en_local":
            print(f"Procesando pedido para comer en local: {detalles}")
        elif tipo_pedido == "entrega_a_domicilio":
            print(f"Procesando pedido para entrega a domicilio: {detalles}")
        else:
            print("Tipo de pedido no valido")
