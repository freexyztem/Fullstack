//	Pedir una frase por consola (texto) y contar el número de cantidad_vocaleses y n_consantes que
//	tiene la frase (enteros). No vamos a tener en cuenta los acentos, símbolos, ni las
//	mayúsculas y minúsculas (el texto será en minúsculas).
//	Resultado (ejemplo "soy nuevo en conquerblocks"):
//		La frase - Hola, soy nuevo - tiene 6 vocales y 6 consonantes
	
Algoritmo VocalesConsonantes
	// Definir variables 
	Definir frase, letra, vocales, consonantes Como Texto
	Definir n_vocales, n_consonantes, i, j Como Entero
	Definir letra_encontrada Como Logico
	// iniciar variables
	n_vocales = 0		//  contador para las vocales
	vocales ="aeiou"	//  todas las vocales
	n_consonantes = 0	//  contador para las consonantes
	consonantes ="bcdfghjklmnpqrstvwxyz" //  todas las consonantes
	i = 0  //  contador para bucle de la frase
	frase = ""	
	letra = ""
	//  Pedir entrada de la frase
	Escribir "Introduce una frase: "
	leer frase
	frase = Minusculas(frase) //  Lo llevamos todo a minusculas
	
	//  Bucle para recorrer la frase por cada letra y contar las cantidad_vocales y consonantes
	Para i = 0 Hasta Longitud(frase)-1 con Paso 1 Hacer
		letra = subcadena(frase,i, i)		//  Leer cada letra segun la posicion del iterador (i)
		letra_encontrada = Falso			//  inicializa que no se ha encontrado la letra para optimizar el tiempo de busqueda en cada bucle de vocales y consonantes
		j = 0								// Se inicializa aqui el iterador (j) para usarlo en las vocales y luego en las consonantes
		Repetir
			Si subcadena(vocales,j,j) = letra Entonces
				n_vocales = n_vocales + 1
				letra_encontrada = verdadero	//  Se ha encontrado la letra en vocales
			FinSi
			j = j + 1							
		Hasta Que (j = longitud(vocales)-1) O (letra_encontrada = Verdadero)  //  repetir hasta que se acaben las vocales o se encuentre la letra en vocales
		Si No letra_encontrada Entonces	//  Si No se ha encontrado la letra en Vocales entonces vamos a buscar en consonantes
			j = 0 							// Se inicializa otra vez el iterador (j) para reusarlo en las consonantes
			Repetir
				Si subcadena(consonantes,j,j) = letra Entonces
					n_consonantes = n_consonantes + 1
					letra_encontrada = verdadero	// Se ha encontrado la lentra en cosonante
				FinSi
				j = j + 1
			Hasta Que (j = longitud(consonantes)) O (letra_encontrada = Verdadero)  //  repetir hasta que se acaben las consonantes o se encuentre la letra en consonantes
		FinSi
	FinPara
	Escribir "La frase - ",frase," - tiene ",n_vocales," vocales y ",n_consonantes," consonantes"// Mostrar en pantalla el resultado
FinAlgoritmo
