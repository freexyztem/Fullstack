	//	Dibuja la X del cuadrado. Pedir el tamaño del lado de un cuadrado (entero) y dibujar la 
	//	"X" de ese cuadrado mediante "*"
	//	Pista1: Se necesita un "Para" anidado.
	//	Pista2: Se dibuja un "*" cuando:
	//	- (altura = ancho) O (lado + 1 = ancho + alto)
	//	En otro caso, se dibuja un " "
	//	Nota: al Escribir, recordad que podéis añadir "Sin Saltar" para que siga escribiendo en 
	//	la misma línea	
Algoritmo DibujaX
	//	1. Definición de variables unas para el tamaño y otras para cada bucle
	Definir tam, i, j Como Entero 
	//	2. Inicialización de variables
	tam = 0
	i = 0
	j = 0
	//	3. Leer el tamaño del cuadrado
	Escribir "Ingrese el tamaño: "sin Saltar
	Leer tam
	//	4. Dibujar la X
	Para i = 0 hasta tam-1 Hacer 
		para j = 0 hasta tam-1 Hacer
			Si (j = i) O (j + i = tam - 1 ) Entonces // Si las filas tienen el mismo valor o si suman el largo se hace la X
				Escribir " * " sin Saltar 
			SiNo
				Escribir "   " Sin Saltar
			FinSi
		FinPara
		Escribir ""
	FinPara
FinAlgoritmo
