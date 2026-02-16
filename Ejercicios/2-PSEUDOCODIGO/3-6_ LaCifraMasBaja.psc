Algoritmo LaCifraMasBaja
	//	La cifra más baja. Pedir por pantalla un número de tres cifras (de 100 a 999) (entero). 
	//	Devolver cuál es la cifra más baja del número introducido.
	//	Nota: hay que comprobar que el número es de 3 cifras.
	//	Ejemplo: si introducimos el número 272, el algoritmo debe devolver: "La cifra más baja 
	//	para el número 272 es 2".
	//	Pista: hay que utilizar el operador MOD y la función trunc(valor). Esta función 
	//	devuelve la parte entera de un número real (ejemplo, de 23.45, devuelve 23).
	
	//	1. Definición de variables
	Definir num, cifraMenor, unidades, decenas, centenas Como Entero
	
	//	2. Inicialización de variables
	num = 0
	cifraMenor = 0
	unidades = 0
	decenas = 0
	centenas = 0
	//	3. Operaciones de lectura (si hay que pedir dato por pantalla)
	Escribir "Ingrese un numeor de 3 cifras: " sin saltar
	Leer num
	//	4. Operaciones lógico-matemáticas que requiera el algoritmo
	Si (num / 1000 < 1 ) Y (num / 1000 > 0 )Entonces
		Escribir "Si es de tres cifras..."
		centenas = trunc(num/100)
		decenas = trunc((num-centenas*100)/10)
		unidades = (num-(centenas*100)-(decenas*10)) 
		Si (centenas < decenas) Y (centenas < unidades) Entonces
			cifraMenor = centenas
		SiNo 
			Si (decenas < unidades) Entonces
				cifraMenor = decenas	
			SiNo 
				cifraMenor = unidades
			FinSi
		FinSi
		Escribir "La cifra más baja para el número ", num, " es ", cifraMenor
	SiNo
		Escribir "El numero no es de tres cifras"
	FinSi
	
FinAlgoritmo
