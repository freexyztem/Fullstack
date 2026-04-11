class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def encender(self):
        self.encendido = True
        print("El vehículo está encendido.")

    def apagar(self):
        self.encendido = False
        print("El vehículo está apagado.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"El vehículo ha acelerado a {self.velocidad} km/h.")
        else:
            print("No se puede acelerar. El vehículo está apagado.")

    def frenar(self, decremento):
        if self.encendido:
            if self.velocidad - decremento >= 0:
                self.velocidad -= decremento
                print(f"El vehículo desacelero a {self.velocidad} km/h.")
            else:
                self.velocidad = 0
                print(f"El vehículo se ha detenido.")
        else:
            print("No se puede frenar. El vehículo está apagado.")
