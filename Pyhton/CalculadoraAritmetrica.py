def aCuadrado(ladoCudra):
    ladoCudra=int(input("Igrese el lado del cuadrado"))
    return ladoCudra*2

while True:
    print("Que operación desea realizar: ")
    print("")
    print("1: Area del cuadrado")
    print("2: Area del circulo")
    print("3:perimetro del cuadrado")
    print("4:perimetro del circulo")
    print("")
    opc = int(input("Digite la opcion requerida: "))

    if opc==1:
        print(f"El area del cuadrado es {aCuadrado()}")

#     elif opc == 2:
#         rResta=resta()
#         print("Su respuesta es " + str(rResta))
# # "Su operación es "+str(resta1)+" - "+str(resta2)+"="+
   
#     elif opc == 3:
#         multiplicacion()
    
#     elif opc == 4:
#         dividendo=int(input("Digité el dividendo: "))
#         divisor=int(input("Digité el divisor: "))
#         if divisor==0:
#          print("Ingrese un numero diferente  0")
#         else:
#          division(dividendo,divisor)   
    
#     else:
#         print("Digite una opcion valida")
  
#     print("")
#     menu = int(input("Digite 0 para salir ó 1 para continuar: "))
#     print("")

#     if menu == 0:
#         print ("~~ Hasta luego ~~")
#         print("")
#         break

#--------------------------------------------------------------------------------------------
# def division(dividendo,divisor):
#     rdivision=dividendo/divisor
#     print("Su operación es " + str(dividendo) + "/" , str(divisor) , "=" , str(rdivision))

#--------------------------------------------------------------------------------------------
# Funcion rAreaCuadrado <- areaCuadrado(datoAreaCuadrado)
# 	rAreaCuadrado = datoAreaCua * 2;
# Fin Funcion

# Funcion areaCirculo (datoAreaCirculo)
# 	RareaCirculo = PI * (datoAreaCir^2);
# 	Escribir "El area del circulo es " , RareaCirculo;
# FinFuncion

# Funcion perimetroCuadrado (datoPeriCuadrado)
# 	rPerimetroCuadrado = 4 * datoPeriCua;	
# 	Escribir "El perimetro del cuadrado es ", rPerimetroCuadrado
# FinFuncion

# Funcion perimetroCirculo(datoUno)
# 	rPerimetroCirculo=2*PI*datoUno
# 	Escribir "El perimetro del circulo es ", rPerimetroCirculo
# FinFuncion

# Algoritmo CalculadoraGeometrica
	
# 	Definir datoUno Como Real;
	
# 	Repetir
		
# 		Repetir
		
# 			
			
# 		Hasta Que operacion="1" o operacion="2" o operacion="3" o operacion="4";
			
# 			Segun operacion Hacer
				
# 				"1":
# 					Escribir "Digité el valor del lado del cuadrado";
# 					Leer datoAreaCua;
					
# 					Escribir "El area del cuadrado es " , areaCuadrado(datoAreaCua)					
					
# 				"2":
# 					Escribir "Digité el valor del radio del circulo";
# 					Leer datoAreaCir;
					
# 					areaCirculo(datoAreaCir)
					
# 				"3":
# 					Escribir "Digité el valor del lado del cuadrado";
# 					Leer datoUno;
					
# 					perimetroCuadrado(datoUno)
					
# 				"4":
# 					Escribir "Digité el valor del radio del circulo";
# 					Leer datoUno;
					
# 					perimetroCirculo(datoUno)
					
# 				De Otro Modo:
# 					Escribir "Ingrese una opción valida";
					
# 			Fin Segun
			
# 			Repetir
# 				Escribir "Digite 1 si desea realizar otra consulta o 2 si desea finalizar";
# 				Leer ya;
# 			Hasta Que ya=1 o ya =2;
		
# 	Hasta Que ya=2;
	
# FinAlgoritmo
