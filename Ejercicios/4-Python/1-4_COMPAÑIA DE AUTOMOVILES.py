"""Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM
todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%
RMB Serie plus:
precio: 35.000 EU, comisión: 5%
RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes"""

# --- Datos de los coches
precio_rbm_s1 = 20000
comision_rbm_s1 = 0.03
precio_rbm_plus = 35000
comision_rbm_plus = 0.05
precio_rbm_td = 60000
comision_rbm_td = 0.07

# --- Ingresar datos por el usuario
rbm_s1 = float(input("Ingrese el número de coches RBM Serie 1 vendidos: "))
rbm_plus = float(input("Ingrese el número de coches RBM Serie plus vendidos: "))
rbm_td = float(input("Ingrese el número de coches RBM todoterreno vendidos: "))

# --- Calcular comisiones
comision_total = (
    (rbm_s1 * precio_rbm_s1 * comision_rbm_s1)
    + (rbm_plus * precio_rbm_plus * comision_rbm_plus)
    + (rbm_td * precio_rbm_td * comision_rbm_td)
)
print("La cantidad a comisionar este mes es:", comision_total, "euros")
