Algoritmo Gimnasio
	// 	Un gimnasio tiene las siguientes tarifas: si ELIGES ir de mañanas, 
	//	1h cuesta 10 euros, 2h cuestan 20 euros y 3h (o más) cuestan 30 euros; en cambio, si 
	//	escoges ir de tardes, 1h cuesta 20 euros, 2h cuestan 30 euros y 3h (o más) cuestan 40 euros.
	//	Pedir en qué momento del día irás, "mañanas" o "tardes" (texto), y el número de horas 
	//	que asistirás (entero), y devolver la tarifa correcta (entero).
	//			*********
	//	Declarar variables e inicializar
	Definir horas, result Como Entero
	Definir horario Como Texto
	horario = ""
	horas = 0
	result = 0
	//	Pedir Entradas
	Escribir "Cuando asistirá? (mañanas o tardes)"
	Leer horario
	Escribir "Cuantas horas asistirá?"
	Leer horas
	Si (horario = "mañanas") Entonces
		
		result = horas * 10 
	SiNo
		Si (horario = "tardes") Entonces
			result = horas * 10 +10
		FinSi
	FinSi
	Escribir "La tarifa es de ", result, " euros, por ",horas," horas, en las ", horario
	//	Logica del programa
FinAlgoritmo
