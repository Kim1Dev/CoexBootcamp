Algoritmo  miAlgo
	
	Definir edad, repetirOperacion Como entero;
	Definir nacionalidad Como Caracter;
	
	Repetir

		Escribir "Digite su edad";
		Leer edad;
		Escribir "Digite su nacionalidad";
		Leer nacionalidad
		
		Si edad >=18 Entonces
			
			Si nacionalidad = "Colombiano" Entonces
				Escribir "Puede votar";
				
			SiNo
				Escribir "No puede votar";
			Fin Si
			
		SiNo
			Escribir  "No puede votar";
		FinSi
		
		Escribir "1 para repetir o 0 para salir";
		Leer  repetirOperacion
		
	Hasta Que repetirOperacion = 0;

FinAlgoritmo
