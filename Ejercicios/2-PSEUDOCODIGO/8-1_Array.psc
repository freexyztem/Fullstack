//	Crear un array de dimensión 5, inicializado con números aleatorios (función azar), del 0
//	al 19. Pedir por consola un valor de 0 a 4, y mostrar el número guardado en esa posición
//	del array (entero). Escribir en consola también el array.
//	Nota: si el número que introduce el usuario es mayor a 4, el programa debería mostrar
//	el array y avisar del error: "La longitud del array es de 0 a 4, por lo que la posición [5] no es válida"
//	Resultado (ejemplo array 2 0 36 15 9 y posición 2):
//		2 0 36 15 9
//		El número del array en la posición [2] es el 36
Algoritmo Array
	// 1. definir las variables
	Definir lista, i, num Como Entero
	num = 0
	Dimension lista[5]
	// 2. Inicializar la lista 
	Para i = 0 hasta 4 con Paso 1 Hacer
		lista[i] = azar(20)
	FinPara
	// 3. Pedir un numero entre 0 y 4 y le dira cual es
	Escribir "Introducir un numero entre 0 y 4 "
	Leer num
	Escribir "0   1    2   3   4  "
	Para i = 0 hasta 4 Con Paso 1 Hacer
		Escribir lista[i],"   " Sin Saltar	
	FinPara	
	Escribir ""
	// Evaluar si el numero esta en rango 0 a 4
	Si num <= 4 Y num >= 0 Entonces
		// 	Mostrar el numero en la posicion y luego el array
		Escribir "en la posicion ", num," esta el ",lista[num]
	SiNo
		Escribir "La longitud del array es de 0 a 4, por lo que la posición [", num ,"] no es válida"
	FinSi
FinAlgoritmo
