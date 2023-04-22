Funcion rAreaCuadrado <- areaCuadrado(datoAreaCuadrado)
	rAreaCuadrado = datoAreaCua * 2;
Fin Funcion

Funcion areaCirculo (datoAreaCirculo)
	RareaCirculo = PI * (datoAreaCir^2);
	Escribir "El area del circulo es " , RareaCirculo;
FinFuncion

Funcion perimetroCuadrado (datoPeriCuadrado)
	rPerimetroCuadrado = 4 * datoPeriCua;	
	Escribir "El perimetro del cuadrado es ", rPerimetroCuadrado
FinFuncion

Funcion perimetroCirculo(datoUno)
	rPerimetroCirculo=2*PI*datoUno
	Escribir "El perimetro del circulo es ", rPerimetroCirculo
FinFuncion

Algoritmo CalculadoraGeometrica
	
	Definir datoUno Como Real;
	
	Repetir
		
		Repetir
		
			Escribir "Que operación desea realizar";
			Escribir "1: Area del cuadrado";
			Escribir "2: Area del circulo";
			Escribir "3:perimetro del cuadrado";
			Escribir "4:perimetro del circulo";
			Leer operacion;
			
		Hasta Que operacion="1" o operacion="2" o operacion="3" o operacion="4";
			
			Segun operacion Hacer
				
				"1":
					Escribir "Digité el valor del lado del cuadrado";
					Leer datoAreaCua;
					
					Escribir "El area del cuadrado es " , areaCuadrado(datoAreaCua)					
					
				"2":
					Escribir "Digité el valor del radio del circulo";
					Leer datoAreaCir;
					
					areaCirculo(datoAreaCir)
					
				"3":
					Escribir "Digité el valor del lado del cuadrado";
					Leer datoUno;
					
					perimetroCuadrado(datoUno)
					
				"4":
					Escribir "Digité el valor del radio del circulo";
					Leer datoUno;
					
					perimetroCirculo(datoUno)
					
				De Otro Modo:
					Escribir "Ingrese una opción valida";
					
			Fin Segun
			
			Repetir
				Escribir "Digite 1 si desea realizar otra consulta o 2 si desea finalizar";
				Leer ya;
			Hasta Que ya=1 o ya =2;
		
	Hasta Que ya=2;
	
FinAlgoritmo
