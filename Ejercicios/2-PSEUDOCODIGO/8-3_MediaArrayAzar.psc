//	Pedir por consola el tamaño de un array (entero) y crear un array de esa dimensión
//	inicializado con números aleatorios entre 5 y 20 (función azar). Escribir en consola el
//	array, y devolver cuál es la media de todos los números del array (real).
//	Nota: la media será la suma de todos los números del array dividido entre la dimensión
//	Resultado (ejemplo con array de dimensión 4):
//		17 11 5 20
//		La media de los números del array es 13.25

Algoritmo sin_titulo
	//	Definir variables
	Definir array, largo, mayor, menor, iterador, repeticion, num Como Entero
	Definir media Como Real
	Dimension repeticion[14]
	//	Inicializar variables
	largo = 0
	iterador = 0
	media = 0
	mayor = 0
	menor = 20 // este valor se inicializa al mas alto posible pues se va eligiendo el mejor
	num = 0
	//	Pedir  dimension al usuario
	Escribir "Introduce el largo del array: " Sin Saltar
	Leer largo
	Dimension array[largo]
	Para iterador =  0 hasta largo - 1 Con Paso 1 Hacer
		array[iterador] = azar(14) +6
		media = media + array [iterador]
		Si mayor < array[iterador] Entonces
			mayor = array[iterador] //	funcion agregada para saber el mayor numero
		FinSi
		Si menor > array[iterador] Entonces
			menor = array[iterador] //	funcion agregada para saber el mayor numero
		FinSi
		Escribir array[iterador], " " Sin Saltar //	Escribir el array en pantalla
	FinPara	
	Escribir ""
	Escribir "La media es: ", media / largo //	Escribir y calcular la media
	Escribir "El menor numero es: ", menor
	Escribir "El mayor numero es: ", mayor
	// Ahora vamos a contar la cantidad de veces que aparecen cada numero:
	Escribir "Cantidad de veces que aparecen los numeros: "
	Para  iterador = 0 hasta 14 - 1 con paso 1 Hacer // primero inicializo el array de contar la repeticiones
		repeticion[iterador] = 0
	FinPara
	Para iterador = 0 hasta largo -1 con Paso 1 Hacer // luego recorro el array aleatorio y empiezo a contar
		num = array [iterador]  //	Si el numero que esta en la posicion iterada 
		repeticion[num-6] = repeticion[num-6] + 1// lo usamos como indice del array repeticion y le sumamos 1
	FinPara
	Para iterador = 0 Hasta 14 - 1 Con Paso 1 Hacer
		Escribir " ",iterador + 6,"->",repeticion[iterador] sin Saltar
	FinPara
	Escribir""
FinAlgoritmo
