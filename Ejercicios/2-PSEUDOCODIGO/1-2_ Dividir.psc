Algoritmo Dividir
	//Pedir dos números (entero) por pantalla y devolver el resultado de la división (real)
	//Cuidado!! Cuando el divisor (el segundo número que pedimos por pantalla) es 0, se 
	//debería avisar con el texto "Error: no se puede dividir por 0"
	//1. Definición de variables
	Definir dividendo, divisor Como Real
	//2. Inicialización de variables
	dividendo = 1
	divisor = 1
	//3. Operaciones de lectura (si hay que pedir dato por pantalla)
	Escribir "*** Calcular división ***"
	Escribir ""
	Escribir "Ingrese el dividendo: "
	Leer dividendo
	Escribir "Ingrese el divisor: "
	Leer divisor
	//4. Operaciones lógico-matemáticas que requiera el algoritmo
	Si divisor = 0  Entonces
		Escribir "Error: no se puede dividir por 0"
	SiNo 
		Escribir dividendo / divisor 
	FinSi
	//4.1. A veces, se necesita una estructura condicional SI-ENTONCES
	//4.1.1. A veces, las operaciones de escritura (resultado), pueden ir en la estructura condicional
	//5. En caso necesario, operaciones de escritura (escribir resultado si no lo hemos tenido 
	//que hacer antes 
FinAlgoritmo