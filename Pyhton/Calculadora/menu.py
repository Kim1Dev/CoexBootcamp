from suma import*
from resta import*
from multi import*
from division import*

while True:
    print("Que operación desea realizar: ")
    print("")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("")
    opc = int(input("Digite la opcion requerida: "))

    if opc==1:
        sumando1=int(input("Digité el primer sumando: "))
        sumando2=int(input("Digité el segundo sumando: "))
        print("Su operación es " + str(sumando1) + " +" , str(sumando2) , "=" , str(suma(sumando1,sumando2)))

    elif opc == 2:
        resta1=int(input("Digité el minuendo: "))
        resta2=int(input("Digité el sustraendo: "))
        print("Su respuesta es " + str("Su operación es "+str(resta1)+" - "+str(resta2)+"="+str(resta(resta1,resta2))))

   
    elif opc == 3:
        factor1=int(input("Digité el primer factor: "))
        factor2=int(input("Digité el segundo factor: "))
        print("Su operación es " + str(factor1) + "×" + str(factor2) + "=" , str(multiplicacion(factor1, factor2)))
    
    elif opc == 4:
        dividendo=int(input("Digité el dividendo: "))
        divisor=int(input("Digité el divisor: "))
        print("Su operación es " + str(dividendo) + "/" , str(divisor) , "=" , str(division(dividendo,divisor)))
        if divisor==0:
         print("Ingrese un numero diferente  0")
        else:
         division(dividendo,divisor)   
    
    else:
        print("Digite una opcion valida")
  
    print("")
    menu = int(input("Digite 0 para salir ó 1 para continuar: "))
    print("")

    if menu == 0:
        print ("~~ Hasta luego ~~")
        print("")
        break