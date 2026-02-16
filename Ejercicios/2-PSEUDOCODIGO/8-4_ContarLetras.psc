//Pedir una frase por consola (texto) y una letra (texto). Decir cuántas veces aparece la
//letra en el texto (entero). En este caso, no vamos a tener en cuenta
//mayúsculas/minúsculas, de forma que el texto será completamente en minúsculas, al
//igual que la letra.
//Resultado (ejemplo "hola, soy nueva"):
//	La letra - a - aparece 2 veces en la frase ? Hola, soy nueva -
Algoritmo ContarLetras
	//  Definir variables
	Definir letra, frase Como texto
	Definir veces, i Como Entero
	//  Inicializar variables
	veces = 0
	i = 0
	frase = ""
	letra = ""
	//  Pedir entrada de datos
	Escribir "Inserte la frase: " 
	Leer frase
	frase = Minusculas(frase)
	//	Un bucle para contar letras hasta que se deje de introducir
	Repetir
		Escribir "Inserta letra a contar o presiona [Enter] para salir: " Sin Saltar 
		Leer letra	// Pedir letra a contar
		letra = Minusculas(letra)
		Para i = 0 hasta longitud(frase)-1 Con Paso 1 hacer //  desde 0 hasta la longitud - 1 pues la longitud no cuenta el 0 
			Si subcadena(frase, i, i) = letra Entonces //  se recorre la frase con el iterador y se selecciona con este solo una letra como subcadena de la frase
				veces = veces + 1 // se incrementa el contador
			FinSi
		FinPara
		Si NO (letra = "") Entonces //  En caso de que la letra no este vacia se escribe el resultado
			Escribir "La letra [", letra,"] aparece [", veces, "] veces en la frase [ ", frase," ]"
		FinSi
		veces = 0	// se reinicia el contador para contar otra letra
	Hasta Que  (letra = "") // si no se introdujo letra se termina el bucle
FinAlgoritmo
