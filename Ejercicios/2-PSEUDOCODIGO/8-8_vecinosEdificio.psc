//	Crear un array bidimensional de 3 filas y 4 columnas, que va a representar un edificio de
//	3 plantas, cada una de ellas con 4 pisos. Inicializar el array con valores aleatorios (función
//	azar), de 1 a 5 (incluidos). Mostrar el array por consola, y decir cuántos vecinos hay en
//	cada planta.
//	Resultado (ejemplo):
//		1 3 2 2 ? Esta sería la planta 3
//		1 2 1 5
//		2 4 2 1 ? Esta sería la planta 1
//	El número de vecinos en la planta 3 es: 8
//	El número de vecinos en la planta 3 es: 9
//	El número de vecinos en la planta 3 es: 9
//		
Algoritmo vecinosEdificio
	// Declarar variables
	Definir suma_piso, pisos, vecinos, piso, vecino, edificio Como Entero
	//  Inicializar variables
	pisos = 3  //  Se incluyen pisos y vecinos en caso de que se quiera cambiar el tamaño del edificio
	vecinos = 4
	piso = 0
	vecino = 0
	Dimension suma_piso[pisos]
	Dimension edificio[pisos, vecinos]
	Para piso = 0 Hasta pisos -1 Con Paso 1 Hacer
		suma_piso[piso] = 0 // se inicia la suma antes de empezar el piso
		Para vecino = 0 Hasta  vecinos -1 Con Paso 1 Hacer
			edificio[piso, vecino] = Azar(5)+1  //  Un numero al azar para cada vecino
			suma_piso[piso] = suma_piso[piso] + edificio[piso, vecino]  //  Suma a cada vecino del piso
		FinPara
	FinPara
	Para piso = pisos - 1 Hasta 0 Con Paso -1 Hacer
		Para vecino = 0 Hasta  vecinos - 1 Con Paso 1 Hacer
			Escribir edificio[piso, vecino], " " sin Saltar
		FinPara
		Escribir ""
	FinPara
	Para piso = pisos - 1 Hasta 0 Con Paso -1 Hacer
		Escribir "El número de vecinos en la planta ", piso + 1," es: ", suma_piso[piso]
	FinPara
	//
FinAlgoritmo
