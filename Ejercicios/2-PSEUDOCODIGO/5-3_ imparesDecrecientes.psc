Algoritmo imparesDecrecientes
	//	Pedir un número por consola (entero) y escribir todos los números impares, en orden 
	//	decreciente, desde ese número hasta el 1.
	//	Ejemplo: si el número introducido es el 23, se escribirían el: 23, 21, 19, 17, ?, 5, 3, 1
	
	//	1. Definición e Inicialización de variables
	Definir num Como Entero
	num = 0
	Escribir "Ingrese un numero:  " sin saltar
	Leer num
	Si (num MOD 2 = 0 ) Entonces
		num = num - 1
	FinSi
	Mientras(num > 0)
		Escribir num," " sin Saltar
		num = num- 2
	FinMientras
FinAlgoritmo
