Algoritmo tablasDeMultiplicar
	Definir tablademultiplicar, v, continuar Como Entero
	
	
	Repetir
		Escribir "Digite el numero a multiplicar";
		Leer tablademultiplicar;
		
		Escribir "Como desea realizar la operación, escriba 1 para for, 2 para while y 3 para do while";
		Leer v
		
		Segun v Hacer
			
			1:
				Para i <- 1 Hasta 10 Hacer
					
					Escribir tablademultiplicar, "x", i, "=" , i*tablademultiplicar;
					
				Fin Para
				
			2:
				i = 1;
				
				Mientras i<=10 Hacer 
					
					Escribir tablademultiplicar, "x", i, "=" , i*tablademultiplicar;
					
					i=i+1;
					
				Fin Mientras
			3:
				i=1 
				
				Repetir
					
					Escribir tablademultiplicar, "x" , i , "=" , i*tablademultiplicar;
					
					i=i+1;
					
				Hasta Que i>10;
				
			De Otro Modo:
				Escribir "Ingrese un numero valido";
				
		Fin Segun
		
		Escribir "Desea hacer otra operación, digite 1 para continuar y 2 para salir";
		Leer continuar;
		
		si continuar <> 1 ;
			
			
			Escribir  " el numero es invalido, intente de nuevo";
			Leer  continuar;
			
		FinSi
		
		
	Hasta Que continuar=2;
	
FinAlgoritmo
