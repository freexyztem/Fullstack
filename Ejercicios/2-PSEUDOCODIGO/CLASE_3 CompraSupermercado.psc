Algoritmo CompraSupermercado
	Definir precioLeche, precioPollo, precioManzana Como Real
	Definir precioTotalLeche, precioTotalPollo, precioTotalManzana Como Real
	Definir precioTotalSuperA, precioTotalSuperB Como Real
	Definir supermercadoEconomico Como Texto
	
	precioLeche = 0
	precioPollo = 0
	precioManzana = 0
	
	Escribir "Supermercado A"
	Escribir "Precio Leche: " Sin Saltar
	Leer precioLeche
	Escribir "Precio Pollo: " Sin Saltar
	Leer precioPollo 
	Escribir "Precio Manzana: " Sin Saltar
	Leer precioManzana
	
	precioTotalLeche = precioLeche * 3
	precioTotalPollo = precioPollo * 1
	precioTotalManzana = precioManzana * 4
	
	precioTotalSuperA = precioTotalLeche + precioTotalManzana + precioTotalPollo
	
	precioLeche = 0
	precioPollo = 0
	precioManzana = 0
	Escribir "Supermercado B"
	Escribir "Precio Leche: " Sin Saltar
	Leer precioLeche
	Escribir "Precio Pollo: " Sin Saltar
	Leer precioPollo 
	Escribir "Precio Manzana: " Sin Saltar
	Leer precioManzana
	
	precioTotalLeche = precioLeche * 3
	precioTotalPollo = precioPollo * 1
	precioTotalManzana = precioManzana * 4
	
	precioTotalSuperB = precioTotalLeche + precioTotalManzana + precioTotalPollo
	
	Si precioTotalSuperA = precioTotalSuperB Entonces
		supermercadoEconomico = "Ninguno de los dos"
	SiNo
		Si precioTotalSuperA > precioTotalSuperB Entonces
			supermercadoEconomico = "Supermercado B"
		SiNo
			supermercadoEconomico = "Supermercado A"
		FinSi
	FinSi
	Escribir supermercadoEconomico, " es más económico"	
	
	
	
FinAlgoritmo
