from LibreriaExponente import *
while True:
    print("Que operación desea realizar: ")
    print("")
    print("1: Potencia cubica")
    print("2: Potencia vaiada")
    print("3: Eulet")
    print("4: PI")
    # print("4: ")
    print("5: Salir")
    print("")
    opc = int(input("Digite la operación que desea realizar: "))
    if(opc==1):
        valorexponer=int(input("Ingrese valor de Exponente"))
        powCubica(valorexponer)
    elif(opc==2):
        valorexponer=int(input("Ingrese valor de la base"))
        exponente=int(input("Ingrese valor de Exponente"))
        powVarios(valorexponer,exponente)
    elif(opc==3):
        print(euler())
    elif(opc==4):
        print(pi())