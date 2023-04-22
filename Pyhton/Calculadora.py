def suma(dSuma1,dSuma2):
    rSuma=dSuma1+dSuma2
    return rSuma
    
def resta():
    resta1=int(input("Digité el minuendo: "))
    resta2=int(input("Digité el sustraendo: "))
    rResta=resta1-resta2
    return rResta

def multiplicacion():
    factor1=int(input("Digité el primer factor: "))
    factor2=int(input("Digité el segundo factor: "))
    rMulti=factor1*factor2
    print("Su operación es " + str(factor1) + "×" + str(factor2) + "=" , str(rMulti))

def division(dividendo,divisor):
    rdivision=dividendo/divisor
    print("Su operación es " + str(dividendo) + "/" , str(divisor) , "=" , str(rdivision))

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
        rResta=resta()
        print("Su respuesta es " + str(rResta))
# "Su operación es "+str(resta1)+" - "+str(resta2)+"="+
   
    elif opc == 3:
        multiplicacion()
    
    elif opc == 4:
        dividendo=int(input("Digité el dividendo: "))
        divisor=int(input("Digité el divisor: "))
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