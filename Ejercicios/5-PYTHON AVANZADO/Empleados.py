"""
Supongamos que estás construyendo un sistema de gestión de empleados
para una empresa. Crea un sistema de clases que maneje la información de
los empleados, incluyendo empleados a tiempo completo y empleados a
tiempo parcial.
- Clase base: `Empleado`
 - Atributos: nombre, apellido, salario base
- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
 - Atributo adicional: bono anual
- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
 - Atributo adicional: horas trabajadas por semana
Resuelve el problema creando instancias de estas clases y calculando los
salarios totales para diferentes tipos de empleados.
"""


class Empleado:
    def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base, bono_anual):
        super().__init__(nombre, apellido, salario_base)
        self.bono_anual = bono_anual

    def calcular_salario_total(self):
        return self.salario_base + self.bono_anual


class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario_base, horas_semana):
        super().__init__(nombre, apellido, salario_base)
        self.hora_semana = horas_semana

    def calcular_salario_total(self):
        # Suponiendo que el salario_base es semanal y se ajusta por las horas trabajadas (40 horas estándar)
        return self.salario_base * (self.hora_semana / 40)


empleado_tiempo_completo1 = EmpleadoTiempoCompleto("Francis", "Ramirez", 50000, 3000)
print(
    "Salario Total del empleado a tiempo completo:",
    empleado_tiempo_completo1.calcular_salario_total(),
)

empleado_tiempo_parcial1 = EmpleadoTiempoParcial("Alexi", "Gonzalez", 50000, 30)
print(
    "Salario Total del empleado a tiempo parcial:",
    empleado_tiempo_parcial1.calcular_salario_total(),
)
