Algoritmo Divisible
	//	Pedir un número (entero) por pantalla y decir si es múltiplo de 2 y de 3 a la vez (texto).
	//	Recordatorio: un número (número 1) es múltiplo de otro (número2) si al dividir el 
	//	primero por el segundo, el RESTO de la división es 0.
	
	Definir num Como Entero
	num = 0
	Escribir "Entre un numero"
	Leer num
	Si (num MOD 2 = 0) Y (num MOD 3 = 0) Entonces
		Escribir "Si es multiplo de 2 y 3 a la vez"
	SiNo
		Escribir "No es multiplo de 2 y 3 a la vez"
	FinSi
FinAlgoritmo
