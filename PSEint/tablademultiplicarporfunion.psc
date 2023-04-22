Funcion construirtablaWhile( numerotabla )
	i = 1;
	
	Mientras i<=10 Hacer 
		
		Escribir tablademultiplicar, "x", i, "=" , i*tablademultiplicar;
		
		i=i+1;
		
	Fin Mientras
Fin Funcion

Funcion construirtablaDowhile( numerotabla )
	i=1 
	
	Repetir
		
		Escribir numerotabla, "x" , i , "=" , (i*numerotabla);
		
		i=i+1;
		
	Hasta Que i>10;
Fin Funcion

Funcion construirtablaFor( numerotabla )
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir numerotabla, "*", i, "=", (numerotabla*i);
	Fin Para
Fin Funcion

Algoritmo tablademultiplicarporfunion
	
	Definir numerotabla, opcionmenu, salir Como Entero
	
	Repetir
		
		Escribir "Que tabla quieres";
		Leer numerotabla;
		
		Escribir "1. for 2. while 3. Do while";
		Leer opcionmenu;		

		Segun opcionmenu Hacer
			1:
				construirtablaFor( numerotabla );
			2:
				construirtablaWhile( numerotabla );
			3:
				construirtablaDowhile( numerotabla );
			De Otro Modo:
				Escribir "No ingreso una opcion validad";
		Fin Segun
		
		Escribir "0 para salir otro valor para continuar";
		Leer salir;
		
	Hasta Que salir = 0;
	
	Escribir "Adios.....";
	
FinAlgoritmo
