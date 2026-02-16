Algoritmo ComparacionDiez
	//	Pedir un número por consola (entero) y decir si es menor, igual o mayor a 10. Hacer 
	//	que el programa continúe pidiendo un número hasta que introduzcamos el 0, y 
	//	entonces, terminará.
	//	Ejemplo:
	//	1) Introduce número: 23
	//	2) 23 es mayor que 10
	//	1) Introduce número: 10
	//	2) 10 es igual a 10
	//	1) Introduce número: 2
	//	2) 2 es menor que 10
	//	1) Introduce número: 0
	//	2) 0 es menor que 10
	//	3) Adios!
	
	//	1. Definición de variables
	Definir num Como Entero
	num = 1 //Se inicializa a 1 para que comience el bucle 
	Mientras (num <> 0) //Mientras no sea 0 
		Escribir "Introduce un número: " sin Saltar
		Leer num //	Operacion de lectura 
		Si (num < 10 ) Entonces
			Escribir num " es menor que 10"
		SiNo 
			Si (num > 10 ) Entonces
				Escribir num " es mayor que 10"
			SiNo
				Escribir num " es igual a 10"
			FinSi			
		FinSi
	FinMientras
	Escribir "Adiós!"
FinAlgoritmo
