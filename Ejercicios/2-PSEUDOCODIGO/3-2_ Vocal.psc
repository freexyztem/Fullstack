Algoritmo Vocal
	// Pedir una letra (texto) por pantalla y decir si es una vocal a, e, i, o, u (texto).
	//	*************
	//Declarar variables
	Definir letra Como Texto
	//	Iniciar variables
	letra = ""
	//	pedir entradas
	Escribir "entre una letra"
	Leer letra
	//Condicion en caso de que sea vocal
	Si (letra = "a") O (letra = "e") O (letra = "i") O (letra = "o") O (letra = "u") Entonces
		Escribir "Es una vocal"
	SiNo 
		Escribir "Es una consonante"
	FinSi
	
FinAlgoritmo
