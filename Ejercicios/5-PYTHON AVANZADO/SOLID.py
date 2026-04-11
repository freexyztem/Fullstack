class Empleados:
    numero_empleados = 0

    # Creacion del CONSTRUCTOR
    # nombre, cargo y salario --> atributos de instancia
    def __init__(self, nombre, cargo, salario):
        # DATOS ////////////////////////////////////////////////////////////////////////
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        Empleados.numero_empleados += (
            1  # Incrementar el contador de empleados cuando un empleado se registre
        )
        # COMPORTAMIENTO ////////////////////////////////////////////////////////////////////////

    def presentarse(self):
        print(f"Hola soy {self.nombre} y ocupo el cargo de {self.cargo}")

    def aumentar_salario(self, porcentaje):
        self.salario *= 1 + porcentaje / 100
        print(f"Nuevo salario de {self.nombre}: {self.salario}")

    @classmethod
    def desde_string(cls, datos_empleado):  # metodo de una clase
        nombre, cargo, salario = datos_empleado.split(",")
        return cls(nombre, cargo, float(salario))

    @staticmethod
    def es_feriado(dia):
        feriados = 1, 10, 27
        return dia in feriados


# INSTANCIAR UNA CLASE -- CREAR OBJETOS
# Utilizar el metodo de instancia
empleado1 = Empleados("Alexi Gonzalez", "Gerente", 10000)
empleado2 = Empleados("Raquel Lopez", "Desarrollador", 5000)
# Utilizar el metodo de clase
empleado3 = Empleados.desde_string("Samuel Quiroz,UX/UI,3000")

# Utilizar los metodos de instancia
empleado1.presentarse()
# empleado2.presentarse()
# empleado3.presentarse()

empleado1.aumentar_salario(10)

# Utilizar los metodos estaticos
print(Empleados.es_feriado(1))

# Acceder al atributo de la clase
print(Empleados.numero_empleados)
