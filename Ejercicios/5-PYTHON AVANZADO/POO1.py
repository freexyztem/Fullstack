class Persona:
    def __init__(self, name):
        self.name = name
        print(f"hello {self.name}")

    def saludar(self):
        print("Hola")


class Papa(Persona):
    def __init__(self, name):
        super().__init__(name)
        print(f"dad... {name}")


persona1 = Persona("Omar")
persona2 = Persona("Jose")
persona3 = Persona("Tomas")

papa = Papa("Jesus")

persona1.saludar()
