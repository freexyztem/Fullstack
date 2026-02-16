//	Crear un array bidimensional de 4 filas y 4 columnas, inicializado con números aleatorios
//	(función azar), de 0 a 9. Crear un nuevo array bidimensional, donde las filas del array
//	anterior sean ahora las columnas. Mostrar el array bidimensional inicial por pantalla y,
//	a continuación, el nuevo array.
//	Resultado (ejemplo):
//		5 6 2 0
//		6 9 5 4
//		3 0 8 7
//		0 1 8 2
//		5 6 3 0
//		6 9 0 1
//		2 5 8 8
//		0 4 7 2
Algoritmo sin_titulo
	//  Definir e inicializar variales
	Definir filas, columnas, array, arrayT Como Entero
	Dimension array[4,4]
	Dimension arrayT[4,4]
	filas = 0	//  no creo que haya que iniciar las filas y columnas porque se inician en el PARA
	columnas = 0
	//  iniciar array con valores al azar y mostrarlo en pantalla
	Para filas = 0 hasta 3 Con Paso 1 Hacer
		Para columnas = 0 hasta 3 Con Paso 1 Hacer
			array[filas, columnas] = Azar(10)  //  Se generan numeros del 0 al 9 al azar y se asignan al array
			Escribir array[filas, columnas], " " Sin Saltar // Se aprovecha este bucle Para para ir escribiendo el array inicial
		FinPara
		Escribir ""  //  un salto de linea al terminar cada fila
	FinPara
	//  Se transpone el array en un arrayT 
	Para filas = 0 hasta 3 Con Paso 1 Hacer
		Para columnas = 0 hasta 3 Con Paso 1 Hacer
			arrayT[filas, columnas] = array[columnas, filas] //  Se intercambian filas por columnas con el array inicial 
			Escribir arrayT[filas, columnas], " " Sin Saltar // Tambien se aprovecha el mismo bucle para escribir el array transpuesto
		FinPara
		Escribir "" //  un salto de linea al terminar cada fila
	FinPara
	
FinAlgoritmo
