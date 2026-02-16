Algoritmo SorteoInstagram
	//	Participación en un sorteo. Para participar en un sorteo de Instagram, tienes que 
	//	cumplir los siguientes requisitos: tener más de 1000 seguidores, seguir a la cuenta 
	//	"sorteo_conquer_blocks" y residir en Francia, Alemania o Italia.
	//	Pedir, como datos, el número de seguidores que tienes (entero), si sigues a la cuenta 
	//	"sorteo_conquer_blocks" (lógico) y el país de residencia (texto), y devolver si puedes 
	//	participar en el sorteo o no (texto).
	
	//	1. Definición de variables
	Definir numSeguidores, contar Como Entero
	Definir seguidorCB, participara Como Logico
	Definir seguidor, pais, participar Como Texto
	
	//	2. Inicialización de variables
	numSeguidores = 0
	seguidorCB = Falso
	participara = Falso
	participar = ""
	pais = ""
	seguidor = ""
	//	3. Operaciones de lectura (si hay que pedir dato por pantalla)
	Escribir "Cuantos seguidores tienes:"
	Leer numSeguidores 
	Si (numSeguidores < 1000) Entonces
		Escribir "esto no te favorece"
	FinSi
	Escribir "Eres seguidor de ConquerBlocks?"
	Leer seguidor
	seguidor = Minusculas(seguidor)
	Si seguidor = "si" O seguidor = "yes" o seguidor = "s" o seguidor = "y" Entonces
		seguidorCB = Verdadero
	SiNo
		Escribir "esto no te favorece"
	FinSi
	Escribir "De que país es?"
	leer pais
	pais = Minusculas(pais)
	Si No((pais = "francia") o (pais = "alemania") o (pais = "italia")) Entonces
		Escribir "esto no te favorece"
	FinSi
	Escribir "Puede participar en el sorteo?"
	Leer participar
	participar = Minusculas(participar)
	Si participar = "si" O participar = "yes" o participar = "s" o participar = "y" Entonces
		participara = Verdadero
	SiNo
		Escribir "esto no te favorece"
	FinSi
	//Limpiar Pantalla
	//	4. Operaciones lógico-matemáticas que requiera el algoritmo
	
	Escribir "Calculando. " Sin Saltar
	Para contar = 0 hasta 5 Hacer
		Esperar 500 Milisegundos
		Escribir ". " Sin Saltar
	FinPara
	Escribir ""
	//Limpiar Pantalla
	Si (numSeguidores >= 1000) Y seguidorCB Y participara Y((pais = "francia") o (pais = "alemania") o (pais = "italia")) Entonces
		Escribir "Si puedes participar en el sorteo"
	SiNo
		Escribir "No puedes participar en el sorteo"
	FinSi
	//	5. En caso necesario, operaciones de escritura (escribir resultado si no lo hemos tenido 
	//		que hacer antes
	
FinAlgoritmo
