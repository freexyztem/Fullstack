Algoritmo Desayuno
	Definir precioCafe, precioTostada, precioZumoNaranja, precioTotalDesayuno, devolucionDesayuno Como Real
	Definir billete Como Entero
	
	billete = 10
	precioCafe = 0
	precioTostada = 0
	precioZumoNaranja = 0	
	//1. Preguntar por el precio del café, de la tostada y del zumo de naranja
	Escribir "A Continuación escribe los precios de los productos: "
	
	Mientras precioCafe <= 0
		Escribir "Precio Cafe"
		Leer precioCafe
	FinMientras
	
	Mientras precioTostada <= 0
		Escribir  "Precio Tostada"
		Leer precioTostada
	FinMientras

	Mientras precioZumoNaranja <= 0	
		Escribir "Precio Zumo Naranja"
		Leer precioZumoNaranja
	FinMientras
	//2. Hacer la suma para calcular el precio total del desayuno
	precioTotalDesayuno = precioCafe + precioTostada + precioZumoNaranja
	//3. Suponiendo que tenemos solo un billete de 10 euros, calcular cuánto nos tienen que
	//devolver
	devolucionDesayuno = billete - precioTotalDesayuno
	//--> PISTA: el coste total del desayuno puede ser mayor, igual o menor a 10 euros :-)
	
	//4. Mostrar el precio total del desayuno y la cantidad a devolver
	Escribir "El Precio Total del Desayuno es $", precioTotalDesayuno
	
	Si devolucionDesayuno > 0 Entonces
		Escribir "Te tienen que devolver $", devolucionDesayuno, " si pagas con un billete de $10"
	SiNo
		Si devolucionDesayuno = 0 Entonces
			Escribir "no tienes ni te tienen que devolver nada"
		SiNo
			Escribir "te faltan $", precioTotalDesayuno - billete, " si pagas con $10"
		FinSi
	FinSi
	
FinAlgoritmo
