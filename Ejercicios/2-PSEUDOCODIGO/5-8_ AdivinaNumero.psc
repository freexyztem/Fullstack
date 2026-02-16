
	//	Juego "Adivina mi número". Pedir al jugador que entre un número (entero) del 1 al 
	//	10, y dejarle 5 segundos para pensar ("Esperar 5 Segundos"). A partir de ahí, el 
	//	ordenador tratará de adivinar el número, preguntando al jugador si su número es "X". 
	//	En caso de que no lo sea, volverá a preguntar por otro número. Tiene 5 intentos para 
	//	tratar de adivinarlo.
	//	Nota: Utilizar las función "azar" para que el ordenador pregunte de forma aleatoria.
	//	Recordatorio: el juego acaba cuando el "número es acertado" O "se han hecho 5 	

Algoritmo AdivinaMiNumero	
//	1. Definición de variables
	Definir num, cont, adivinando, i Como Entero
	Definir acertado, unico Como Logico
//	2. Inicialización de variables
	num = 0
	i = 0
	cont  = 5
	acertado = Falso
	unico = Verdadero
	Dimension adivinando[5]
//	3. Operaciones de lectura
	Repetir //Repetir lectura de numero hasta que el numero este entre 1 y 10
		Escribir "Inserta un numero del 1 al 10: " sin Saltar
		Leer num
		Si (num < 1) O (num > 10) Entonces
			Escribir "Error" // Escribe Error si esta fuera del rango
		FinSi
	hasta que (num >= 1) Y (num <=10)
//	4. Esperar 2 segundos antes de empezar con animacion de puntos 
	Para i = 0 hasta 19 Hacer
		Escribir ". " sin Saltar
		Esperar 100 Milisegundos
	FinPara
	Escribir ""
//	5. Inicializa los 5 numeros propuestos y se asegura que sean diferentes
	Para cont = 0 hasta 4 hacer// para los 5 numeros
		adivinando[cont] = Azar(10)+1 // genere un numero al azar entre 1 y 10
		Si cont > 0 Entonces // si no es el primer numero a chequear
			Repetir// Repetir hasta que sea unico el numero
				unico = Verdadero //Se inicializa como unico 
				Para i = 0 hasta cont-1 Hacer //desde el primer numero hasta uno antes del actual
					Si adivinando[i] = adivinando[cont] Entonces // Comprueba si existe alguna coincidencia
						unico = Falso //Si se encuentra una coincidencia entonces unico es Falso
						adivinando[cont] = Azar(10)+1 // se genera otro numero al azar en ese caso
					FinSi
				FinPara
			Hasta que (unico=Verdadero) // Si unico es Falso entonces hay que repetir para comprobar el nuevo numero generado
		FinSi		
	FinPara
	Para cont = 0 hasta 4 
		Escribir "[",adivinando[cont], "] " Sin Saltar
	FinPara
	Escribir ""
	// 6. Comenzar juego con los numeros generados unicos
	cont = 0
	Repetir	// repetir hasta que se encuentre una coicidencia o hasta que se hagan los 5 intentos
		Escribir "	Intento # ", cont+1,": ", adivinando[cont] //se escribe el numero del intento

		Si (adivinando[cont] = num) Entonces // Si se encuentra coincidencia con el numero dado
			Escribir "He adivinado tu numero en ",cont+ 1," intentos y es: ", adivinando[cont] // Se muestra en pantalla la coincidencia
			acertado = Verdadero // se encontro el valor, el intento es acertado 
		SiNo
			cont = cont+1 // si no se encontro el valor se prueba con el intento siguiente
		FinSi
	Hasta Que (cont > 4) o acertado = Verdadero
	Si cont = 5 Entonces
		Escribir "No he adivinado tu numero en los 5 intentos" // mensaje cuando no se adivina el numero
	FinSi
FinAlgoritmo
