Algoritmo numerosCreciente
	//	Pedir un número (entero) y escribir por consola todos los números hasta ese número, 
	//	en orden creciente.
	//	Ejemplo: si el número es 12, habría que escribir por consola todos los números desde 
	//	el 1 hasta el 12.
	
	//	1. Definición de variables
	Definir num, cont Como Entero
	//	2. Inicialización de variables
	num = 0
	cont = 0
	//	3. Operaciones de lectura (si hay que pedir dato por pantalla)
	Escribir "numero: " sin Saltar
	Leer num
	//	4. Operaciones lógico-matemáticas que requiera el algoritmo
	Para cont = 1 Hasta num Hacer
		Escribir cont," " sin Saltar
	FinPara
	//	4.1. A veces, se necesita una estructura condicional SI-ENTONCES
	//	4.1.1. A veces, las operaciones de escritura (resultado), pueden ir en la estructura condicional
	//	5. En caso necesario, operaciones de escritura (escribir resultado si no lo hemos tenido 
	//		que hacer antes
FinAlgoritmo
