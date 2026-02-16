Algoritmo TiendaRopa
	//	En una tienda de ropa, hay rebajas. Si compramos 1 prenda, nos hacen un descuento 
	//	del 15%; si compramos 3, nos hacen un descuento del 25%; y si compramos más de 3, 
	//	nos hacen el descuento del 25% y, además, nos regalan una prenda más.
	//	El precio de todas las prendas es el mismo, 10 euros. Habría que pedir por pantalla 
	//	cuántas prendas queremos comprar (entero) y calcular: el precio total (real) y el número 
	//	de prendas (entero) que nos llevamos (recordad que, si compramos más de 3 prendas, 
	//	nos llevaríamos 1 de regalo
	//	*********************
	
	//1. Definición de variables
	Definir cantidad, cantidadFinal Como Entero
	Definir precio Como Real
	//2. Inicialización de variables
	cantidad = 0
	cantidadFinal = 0
	precio = 0
	//3. Operaciones de lectura (si hay que pedir dato por pantalla)
	Escribir "Introduce la cantidad de prendas a comprar:"
	Leer cantidad
	//4. Operaciones lógico-matemáticas que requiera el algoritmo
	Segun cantidad 
		1: 	precio = cantidad * 10 * (1 - 0.15)
			cantidadFinal = cantidad
		2: 	precio = cantidad * 10 * (1 - 0.15)
			cantidadFinal = cantidad
		3: 	precio = cantidad * 10 * (1 - 0.25)
			cantidadFinal = cantidad 
		De Otro Modo:
			precio = cantidad * 10 * (1 - 0.25)
			cantidadFinal = cantidad + 1
			
	FinSegun
	
	//5. Imprimir el resultado en pantalla
	Escribir "El precio final sería: ", precio
	Escribir "La cantidad final sería: ", cantidadFinal
FinAlgoritmo