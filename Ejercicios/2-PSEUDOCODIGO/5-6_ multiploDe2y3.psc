	//	Pedir un número (entero) y calcular qué números desde el 1 hasta el propio número 
	//	son múltiplos de 2 y 3.
	//	Recordatorio: un número es múltiplo de 2 si al dividir por 2, el resto es 0; y es múltiplo 
	//	de 3 si al dividir por 3, el resto es 0
	//	Ejemplo: dado el número 15, los números múltiplos de 2 y 3 hasta 15 son 6 y 12 (resto 
	//	0 en ambas divisiones
Algoritmo multiploDe2y3
	//	1. Definición de variables e Inicialización 
	Definir num, i Como Entero
	num = 0
	i = 0
	//	2. Operaciones de lectura (si hay que pedir dato por pantalla)
	Escribir "Introduce un numero: " sin Saltar
	Leer num
	
	Si No(num < 6) Entonces // Se evalua que el numero no sea menor que 6 que es el primer multiplo
		Escribir "Los numeros multiplos de 2 y 3 menor que ", num ," son: " 
		Para i = 6 hasta num Con Paso 1 Hacer //	3. Se utiliza un Para que recorra hasta el numero dado 
			Si (i mod 2 = 0) Y (i MOD 3 = 0) Entonces //Condicion si es multiplo de 2 y 3
				Escribir i
			FinSi
		FinPara
	SiNo
			Escribir "No existen numeros menores que ", num, " multiplos de 2 y 3."
	FinSi

FinAlgoritmo
