Funcion rAumen <- Aumen (Num)
	rAumen=Num+5
	
Fin Funcion

//Implementar una función tal que vaya aumentando el valor recibido en 5 hasta un límite de 8 veces
//Retornar el valor final.
//Usar el bucle do ... while.

Algoritmo Aumentar5en5
	
	Escribir "Ingrese el valor que desee aumentar"
	Leer Num
	
	i=1 
	
	Repetir
		
		Escribir "Los valores aumentados son " , Aumen(num);
		
		i=i+1;
		
	Hasta Que i>8;
	
FinAlgoritmo
