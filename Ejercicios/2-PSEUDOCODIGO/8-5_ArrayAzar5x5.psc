//	Crear un array bidimensional de 5 filas y 5 columnas, inicializado con números aleatorios
//	(función azar), de 0 a 9. Pedir por consola un valor de 0 a 9, y mostrar cuántas veces
//	aparece ese número en el array (entero). Escribir en consola también el array.
//	Resultado (ejemplo, con el número 5):
//		5 6 2 0 5
//		6 9 5 4 6
//		3 0 8 7 3
//		0 1 8 2 6
//		0 9 8 6 7
//		El número 5 aparece 3 veces

Algoritmo ArrayAzar5x5
	//  Declarar variables array, numero a contar, contador, iterador en x, iterador en y	
	Definir array, num, contador, i, j Como Entero 
	//  Inicializar variables
	Dimension array[5, 5]
	num = 0
	contador = 0
	i = 0
	j = 0
	//  Pedir numero que se contara
	Escribir "Inserte un numero entre 0 y 9"
	Leer num
	Si (num >= 0) Y (num <= 9) Entonces // Comprobar que el numero este en rango
		Para i = 0 hasta 4 //  Bucle para recorrer el array y contar el numero y mostrar el array
			para j = 0 hasta 4
				array[i,j] = Azar(10)
				Escribir  array[i,j], " " sin Saltar
				Si array[i,j] = num Entonces
					contador = contador + 1
				FinSi
			FinPara
			Escribir""
		FinPara
		//  mostrar cuantas veces aparece el numero
		Si contador = 1 Entonces
			Escribir "El numero ", num, " aparece ", contador," vez" 
		SiNo
			Escribir "El numero ", num, " aparece ", contador," veces" 
		FinSi
	SiNo
		Escribir "El número no está entre 0 y 9"	
	FinSi
	
FinAlgoritmo
