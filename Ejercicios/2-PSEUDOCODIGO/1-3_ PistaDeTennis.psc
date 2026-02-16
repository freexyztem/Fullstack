Algoritmo PistaDeTennis
	//	Hemos alquilado una pista de tenis y el precio por minuto es de 20 céntimos (0.2). 
	//	Sin embargo, hay un descuento del 10% si estamos más de 90 minutos jugando.
	//	Pedir por pantalla dos números, donde el primero será el número de horas (entero) y el 
	//	segundo el número de minutos (entero) que hemos estado jugando, y calcular cuánto 
	//	tendríamos que pagar (real)
	//	*********************
	
	//1. Definición de variables
	Definir horas, minutos, minTotal Como Entero
	Definir pagar Como Real
	//2. Inicialización de variables
	horas = 0
	minutos = 0
	minTotal = 0
	//3. Operaciones de lectura (si hay que pedir dato por pantalla)
	Escribir "Ingrese las horas: "
	Leer horas
	Escribir "Ingrese las minutos: "
	Leer minutos
	//4. Operaciones lógico-matemáticas que requiera el algoritmo
	minTotal = horas * 60 + minutos
	Si (minTotal > 90) Entonces 
		pagar = minTotal * 0.2 * (1 - 0.1)
	SiNo 
		pagar = minTotal * 0.2
	FinSi
	// Escribir Resultado
	Escribir pagar
FinAlgoritmo
