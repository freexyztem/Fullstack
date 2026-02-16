//	Pedir un número (entero) y calcular su factorial (entero)
//	Recordatorio: el factorial de un número se calcula multiplicando los números desde el 
//	1 hasta el propio número, incluidos los números intermedios
//	Ejemplo: el factorial de 6 sería 1 * 2 * 3 * 4 * 5 * 6 = 720

Funcion factorial(i)
	Definir cont, factor Como Entero
	factor=1
	Para cont = 1 hasta i Hacer
		factor = cont * factor
	FinPara
	Escribir factor
FinFuncion
Algoritmo FactorialDeUnNumero
	//	1. Definición e Inicialización de variables
	Definir num Como Entero
	num = 0
	Escribir "Ingrese el numero a calcular el factorial: " sin Saltar
	Leer num
	factorial(num)
FinAlgoritmo
