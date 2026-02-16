
	//	Juego "Piedra, Papel, Tijera". Vamos a enfrentarnos contra el ordenador en el juego de 
	//	piedra, papel o tijera. Reglas:
	//	- Piedra gana a Tijera y pierde con Papel
	//	- Papel gana a Piedra y pierde con Tijera
	//	- Tijera gana a Papel y pierde con Piedra
	//	Pedir al jugador que escoja entre "Piedra | Papel | Tijera" (texto); el ordenador hará su 
	//	elección al azar. Y se comparan las dos elecciones para ver quién gana. Al terminar una 
	//	partida, se pedirá si se quiere jugar de nuevo (texto) y, en caso afirmativo, se reinicia el 
	//	juego (sin que acabe el programa).
	//	Recordatorio: hay que controlar que el jugador introduzca una de las 3 opciones 
	//	(Piedra | Papel | Tijera), y no otra.
	//	Pista: la función "azar(3)" devuelve un número al azar entre 0, 1 y 2. Cada una de estas 
	//	opciones podríamos asociarla a "piedra", "papel" o "tijera": "Si numAzar = 0 Entonces 

Funcion result = Verificar(e) // funcion de verificacion de la eleccion del usuario devuelve verdadero si es una de las 3 opciones
	definir result Como Logico
	Si (("piedra" = e) O ("papel" = e) O ("tijera" = e)) Entonces
		result = Verdadero
	SiNo
		result = Falso
	FinSi
FinFuncion
Funcion result = Jugar //devuelve el texto de la opcion generada al azar
	Definir result Como Texto
	Definir ordenador Como Entero
	result = ""
	ordenador = Azar(3)
	Segun ordenador 
		0:	result = "tijera"
		1:	result = "papel"
		2:	result = "piedra"
	FinSegun
	Escribir "ordenador: ", result
FinFuncion
Algoritmo PiedraPapelTijera		
	//	1. Definición e Inicialización de variables
	Definir eleccion, salir, ordenador Como Texto
	eleccion = ""
	ordenador = ""
	salir = ""
	// 	2. Incio de Bucle para comenzar el juego hasta que se escriba salir cuando se pregunte si continuar o salir?
	Repetir
		Escribir "Elija entre: Piedra | Papel | Tijera"	//	Pedir que introduzca su eleccion
		Leer eleccion
		eleccion = Minusculas(eleccion) //Convertimos la eleccion a minusculas para evitar algun error
		Si Verificar(eleccion) Entonces // Funcion para la verificacion de la eleccion del usuario
			ordenador = Jugar // Funcion para que el ordenador elija su respuesta
			Segun eleccion
				"tijera": 
					Segun ordenador
						"tijera": Escribir "Empate" Sin Saltar //se hacen los cruces de empate, ganador y perdedor
						"papel": Escribir "Ganas" Sin Saltar
						"piedra": Escribir"Pierdes" Sin Saltar
					FinSegun
				"papel":
					Segun ordenador
						"papel": Escribir "Empate" Sin Saltar
						"piedra": Escribir "Ganas" Sin Saltar
						"tijera": Escribir"Pierdes" Sin Saltar
					FinSegun
				"piedra":	
					Segun ordenador
						"piedra": Escribir "Empate" Sin Saltar
						"tijera": Escribir "Ganas" Sin Saltar
						"papel": Escribir"Pierdes" Sin Saltar
					FinSegun
					
			FinSegun
			Escribir " (",eleccion, " vs. ", ordenador, ")"	// se termina haciendo el resumen de las elecciones por los dos bandos
		SiNo
			Escribir "Eleccion Incorrecta" //Mensaje de error en entrada
		FinSi
		Escribir "Desea Continuar | Salir?"
		Leer salir
	Hasta Que (Minusculas(salir) = "salir") //si Salir es verdadero se acaba
	
	//	Mensaje de despedida y termina el algoritmo
	
FinAlgoritmo
