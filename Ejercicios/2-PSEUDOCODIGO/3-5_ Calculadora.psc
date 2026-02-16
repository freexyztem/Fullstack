Algoritmo Calculadora
	//	Pedir dos números (enteros) por pantalla, y pedir ELEGIR entre una operación de 
	//	"sumar", "restar", "multiplicar" y "dividir" (texto). Una vez tengamos los datos, realizar 
	//	la operación en función de la operación seleccionada (real).
	//	Recordatorio: si se elige "dividir", recordad que no se puede dividir entre 0.
	//	Nota: Hay que tener en cuenta que pueden introducir otra operación que no sea la que 
	//	esperamos, a lo que habría que decir: "No es posible realizar la operación solicitada"
	
	//	1. Definición de variables
	Definir operacion Como Texto
	Definir num1, num2 Como Entero
	Definir resultado Como Real
	//	2. Inicialización de variables
	operacion = ""
	resultado = 0
	//	3. Operaciones de lectura (si hay que pedir dato por pantalla)
	Escribir "Calculadora de 2 numeros"
	Escribir "inserte el primero: " Sin Saltar
	Leer num1
	Escribir "inserte el segundo: " Sin Saltar
	Leer num2
	Escribir "Que operacion?(Sumar+ Restar- Multiplicar* Dividir/): " Sin Saltar
	Leer operacion
	operacion = Minusculas(operacion)
	//	4. Operaciones lógico-matemáticas que requiera el algoritmo
	Segun operacion Hacer
		"sumar": resultado = num1 + num2
		"restar": resultado = num1 - num2
		"dividir": 	
			Si num2 = 0 Entonces
				Escribir "no se puede dividir entre 0"
			SiNo
				resultado = num1 / num2
			FinSi
		"multiplicar": resultado = num1 * num2
		"+": 
			resultado = num1 + num2
			operacion = "sumar"	
		"-": 
			resultado = num1 - num2
			operacion = "restar"
		"/": 	
			operacion = "dividir"
			Si num2 = 0 Entonces
				Escribir "no se puede dividir entre 0"
			SiNo
				resultado = num1 / num2
			FinSi
		"*":
			resultado = num1 * num2
			operacion = "multiplicar"
		De Otro Modo:
			Escribir "No es posible realizar la operación solicitada"
	FinSegun
	Escribir "El resultado de la operación ", operacion, " es: ",resultado
	//	4.1. A veces, se necesita una estructura condicional SI-ENTONCES
	//	4.1.1. A veces, las operaciones de escritura (resultado), pueden ir en la estructura condicional
	//	5. En caso necesario, operaciones de escritura (escribir resultado si no lo hemos tenido 
	//		que hacer antes
FinAlgoritmo
