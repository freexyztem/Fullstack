//Crear un array e inicializarlo con 5 números pedidos por consola (enteros). Una vez
//guardados, buscar cuál es el número mayor. Escribir en consola el array, y devolver cuál
//es el número mayor (entero).
//Resultado (ejemplo):
//	6 23 9 45 18
//	El número mayor del array es el 45

Algoritmo MayorDe5
	//	Declarar variables
	Definir array, i, num Como Entero
	num = 0
	Dimension array[5]
	// Pedir los 5 numeros
	Para i = 0 hasta 4 Con Paso 1 hacer 
		Escribir "[", i+1,"] introduce un número"
		Leer array[i] 
		Si num < array[i] Entonces
			num = array[i]
		FinSi
	FinPara	
	Para i = 0 hasta 4 Con Paso 1 hacer 
		Escribir array[i], " " sin Saltar
	FinPara
	Escribir ""
	Escribir "El mayor numero entrado es: ", num
FinAlgoritmo
