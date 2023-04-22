while True:
    nTabla=int(input('Digite la tabla que desea consultar: '))
    print("")
    print("Seleccione la opcion deseada:")
    print("1. For")
    print("2. While")
    print("3. Do while")
    print("")
    opc = int(input("Digite: "))

    if opc == 1:
        print("")
        print("La tabla del " + str(nTabla))
        for i in range(11):
            print(str(nTabla) + " × " + str(i) + " = " + str(i * nTabla))
    elif opc == 2:
        print("")
        print("La tabla del " + str(nTabla))
        cont = 1
        while cont <= 10:
            print(str(nTabla) + " × " + str(cont) + " = " + str(cont * nTabla))
            cont += 1
    elif opc == 3:
        print("")
        print("La tabla del " + str(nTabla))
        cont = 1
        while True:
            print(str(nTabla) + " × " + str(cont) + " = " + str(cont * nTabla))
            if cont >= 10:
                break
            else:
                cont += 1
    else:
        print("Digite una opcion valida")
    
    print("")
    menu = int(input("Digite 0 para salir ó 1 para continuar: "))
    print("")

    if menu == 0:
        print ("~~ Hasta luego ~~")
        print("")
        break