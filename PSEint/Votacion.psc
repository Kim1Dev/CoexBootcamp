Algoritmo Votacion
	
	Definir edad Como Entero
	Definir nacionalidad Como Caracter;
	
	Repetir
		
		Escribir  "Digite su edad";
		Leer edad;
		
		Escribir "Digite su nacionalidad";
		Leer nacionalidad
		
		Si edad>=18 y nacionalidad = "Colombiano" Entonces
			Escribir "Puede votar";
		SiNo
			Escribir "No puede votar";
		Fin Si
		
		Escribir "1 para repetir o 0 para salir";
		Leer  repetirOper
		
	Hasta Que repetirOper = 0;
	
	
	
FinAlgoritmo