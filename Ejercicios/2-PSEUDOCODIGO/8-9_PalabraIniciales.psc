Algoritmo PalabraIniciales
	// Declarar variables
	Definir oracion, palab, caract Como Texto
	Definir i, largo Como Entero
	// Iniciar variables
	palab = ""
	oracion = ""
	caract = " "
	// leer oracion
	Escribir "Introduce una frase: "
	Leer oracion
	// sacar el largo de la oracion
	largo = longitud(oracion) 
	// recorrer oracion y por cada espacio
	palab = subcadena(oracion, 0, 0)
	Para i=0 hasta (largo -1) hacer
		caract = subcadena(oracion,i,i)
		Si caract = " " Entonces
			palab = concatenar(palab, subcadena(oracion, i+1, i+1))
		FinSi
		
	FinPara
	Escribir "las inciales de palabras son: ",palab
FinAlgoritmo