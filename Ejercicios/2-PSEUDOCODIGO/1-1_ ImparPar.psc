Algoritmo ImparPar
	//Pedir un número (entero) por pantalla y decir si es par o impar
	
	//1. Definición de variables
	Definir dato Como Entero
	//2. Inicialización de variables
	Dato = 0
	//3. Operaciones de lectura (si hay que pedir dato por pantalla)
	Escribir "Ingrese el numero a chequear: "
	Leer Dato
	//4. Operaciones lógico-matemáticas que requiera el algoritmo
	Si dato ^ 2 = 0  Entonces
		Escribir "El numero es Par"
	SiNo 
		Escribir "El numero es impar"
	FinSi
	//4.1. A veces, se necesita una estructura condicional SI-ENTONCES
	//4.1.1. A veces, las operaciones de escritura (resultado), pueden ir en la estructura condicional
	//5. En caso necesario, operaciones de escritura (escribir resultado si no lo hemos tenido 
	//que hacer antes 
FinAlgoritmo