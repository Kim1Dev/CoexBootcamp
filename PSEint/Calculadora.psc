Funcion suma ( datoSumaUno, datoSumaDos )
	
	rsum = datoSumaUno + datoSumaDos
	Escribir "Su operación es " , datoSumaUno , " + " , datoSumaDos , ", entonces su respuesta es " , rsum;
	
Fin Funcion

Funcion resta ( datoRestaUno, datoRestaDos )
	
	rresta=datoRestaUno-datoRestaDos
	Escribir "Su operación es " , datoRestaUno , " - " , datoRestaDos , ", entonces su respuesta es " , rresta;
	
Fin Funcion

Funcion multi ( datoMultiUno, datoMultiDos )
	
	rmulti=datoMultiUno*datoMultiDos
	Escribir "Su operación es " , datoMultiUno , " * " , datoMultiDos , ", entonces su respuesta es " , rmulti;
	
Fin Funcion

Funcion divi ( datoDivUno, datoDiDos )
	
	rdivi=datoDivUno/datoDiDos
	Escribir "Su operación es " , datoDivUno , " / " , datoDiDos , ", entonces su respuesta es " , rdivi;
	
Fin Funcion



Algoritmo Calculadora
	
	Definir datoUno, datoDos, operacion Como Entero;
	
	Repetir
		
		Escribir "Que operación desea realizar 1: suma, 2: resta, 3:multiplicación, 4:división";
		Leer operacion;
		
		Escribir "Digité el primer factor";
		Leer datoUno;
		
		Escribir "Digité el segundo factor";
		Leer datoDos;
		
		Segun operacion Hacer
			1:
				suma(datoUno,datoDos)
			2:
				resta(datoUno,datoDos)
			3:
				multi(datoUno,datoDos)
			4:
				divi(datoUno,datoDos)
				
			De Otro Modo:
				Escribir "Ingrese una opción valida, Que operación desea realizar 1: suma, 2: resta, 3:multiplicación, 4:división";
		Fin Segun
		Repetir
			
			Escribir "Digite 1 si desea realizar otra consulta o 2 si desea finalizar";
			
			Leer ya;
			
		Hasta Que ya=1 o ya =2;
		
	Hasta Que ya=2;
	
FinAlgoritmo
