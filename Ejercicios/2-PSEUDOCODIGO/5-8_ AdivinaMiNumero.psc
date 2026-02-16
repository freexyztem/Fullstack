
	//	Juego "Adivina mi número". Pedir al jugador que piense un número (entero) del 1 al 
	//	10, y dejarle 5 segundos para pensar ("Esperar 5 Segundos"). A partir de ahí, el 
	//	ordenador tratará de adivinar el número, preguntando al jugador si su número es "X". 
	//	En caso de que no lo sea, volverá a preguntar por otro número. Tiene 5 intentos para 
	//	tratar de adivinarlo.
	//	Nota: Utilizar las función "azar" para que el ordenador pregunte de forma aleatoria.
	//	Recordatorio: el juego acaba cuando el "número es acertado" O "se han hecho 5 	

Algoritmo AdivinaMiNumero	
	
//	1. Definición de variables
	Definir intentos, adivinando, i Como Entero
	Definir unico, acertado Como Logico
	Definir respuesta Como Texto
	
//	2. Inicialización de variables
	i = 0
	respuesta = ""
	acertado = Falso
	intentos  = 5
	unico = Verdadero
	Dimension adivinando[5] //es una matriz que guarda los 5 numeros y permite revisar que no se repitan
	
//	3. Pedir que piense en un numero no necesita operacion de lectura
	Escribir "Piensa en un numero del 1 al 10: " sin Saltar	
	
//	4. Esperar 5 segundos antes de empezar con animacion de puntos 
	Para i = 1 hasta 20 Hacer
		Escribir ". " sin Saltar
		Esperar 250 Milisegundos
	FinPara
	Escribir ""
	
//	5. Inicializa los 5 numeros propuestos y se asegura que sean diferentes
	Para intentos = 0 hasta 4 hacer// para los 5 numeros
		adivinando[intentos] = Azar(10)+1 // genere un numero al azar entre 1 y 10
		Si intentos > 0 Entonces // si no es el primer numero a chequear
			Repetir// Repetir hasta que sea unico el numero
				unico = Verdadero //Se inicializa como unico 
				Para i = 0 hasta intentos-1 Hacer //desde el primer numero hasta uno antes del actual
					Si adivinando[i] = adivinando[intentos] Entonces // Comprueba si existe alguna coincidencia
						unico = Falso //Si se encuentra una coincidencia entonces unico es Falso
						adivinando[intentos] = Azar(10)+1 // se genera otro numero al azar en ese caso
					FinSi
				FinPara
			Hasta que (unico=Verdadero) // Si unico es Falso entonces hay que repetir para comprobar el nuevo numero generado
		FinSi		
	FinPara
	Escribir ""
	
// 6. Comenzar juego con los numeros generados unicos
	intentos = 0
	Repetir	// repetir hasta que diga que si es el numero o hasta que se hagan los 5 intentos
		Escribir "	Tu numero será?: ", adivinando[intentos] , " ( Si | No )"//se escribe el numero del intento
		Leer respuesta
		respuesta = Minusculas(respuesta) // Se lleva la respuesta a minusculas para que todo coincida 
		Si (respuesta = "si" ) Entonces // Si se es el numero pensado
			acertado = Verdadero
		FinSi
		intentos = intentos+1 // si no se enintentosro el valor se prueba con el intento siguiente
	Hasta Que (intentos = 5) o acertado
	
	Si acertado = Verdadero  Entonces
		Escribir "*** Perfecto, he adivinado en ",intentos," intentos ***" // escribir confirmacion
	SiNo 
		Escribir "No he acertado mis 5 intentos  :(" // Escribir fallo 
	FinSi
FinAlgoritmo
