Algoritmo Multiplicaciones
	
	Definir factor, ya Como Entero;
	
	Repetir
		
		Escribir "Digité el factor a multiplicar";
		Leer factor;
		
		Escribir "Cómo desea realizar la multiplicación, escriba 1 para for, 2 para while y 3 para do while";
		Leer eleccion
		
		Segun eleccion Hacer
			1:
				Para i <- 1 Hasta 10 Hacer
					
					Escribir factor, "x" , i , "=" , i*factor;
					
				FinPara
				
			2:
				i = 1
				
				Mientras i<=10 Hacer
					
					Escribir factor, "x" , i , "=" , i*factor;
					
					i=i+1;
					
				Fin Mientras
				
			3:
				i=1 
				
				Repetir
					
					Escribir factor, "x" , i , "=" , i*factor;
					
					i=i+1;
					
				Hasta Que i>10;
				
			De Otro Modo:
				
				Escribir "Escribe una opción valida, Cómo desea realizar la multiplicación, escriba 1 para for, 2 para while y 3 para do while";
				
		Fin Segun
		
		Repetir
			
			Escribir "Digite 1 si desea realizar otra consulta o 2 si desea finalizar";
			
			Leer ya;
			
		Hasta Que ya=1 o ya =2;
		
	Hasta Que Ya=2
	
FinAlgoritmo