Algoritmo SumaEntreDos
	//	Pedir dos números por consola (enteros) y sumar (entero) todos los números que hay 
	//	entre ellos.
	//	Nota: vamos a suponer que el primer número que introduce el usuario SIEMPRE es 
	//	menor que el segundo
	//	Ejemplo: si los números introducidos son el 4 y el 11, el resultado sería:
	//		5 + 6 + 7 + 8 + 9 + 10 = 45
	
	//	1. Definición e Inicialización de variables
	Definir num1, num2, result, cont Como Entero
	num1 = 0
	num2 = 0
	result = 0
	cont = 0
	//	2. Operaciones de lectura 
	Escribir "Ingrese dos numeros"
	Leer num1, num2
	//	3. Operaciones lógico-matemáticas que requiera el algoritmo
	Para cont = num1+1 hasta num2-2 Hacer
		result = result + cont 					//sumar 1 despues hasta el penultimo
		Escribir cont," + " sin Saltar
	FinPara
	Escribir num2-1, " = ", result+num2-1 		//sumarle luego el ultimo numero y mostrar el resultado final
FinAlgoritmo
