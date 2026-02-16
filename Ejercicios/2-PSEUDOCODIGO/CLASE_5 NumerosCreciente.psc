Algoritmo NumerosCreciente
	// Pedir un número (entero) y escribir por consola todos los números hasta ese número, en orden creciente.
	// Ejemplo: si el número es 12, habría que escribir por consola todos los números desde el hasta el 12.
	// Definir variables
	Definir tuNumero , contador Como Entero
	// Iniciar variables
	tuNumero = 0
	// Pedir datos
	Escribir "Escriba un numero entre 1 y 100"
	// Leer datos
	Leer tuNumero 
	// Calcular resultado + mostrar resultado
	Si (tuNumero > 0) Y (tuNumero) <= 100 Entonces
		Para contador = 1 hasta tuNumero
			Escribir contador
			//Esperar 1 Segundos
		FinPara
	SiNo
		Escribir "dato incorrecto"
	FinSi
	
FinAlgoritmo
