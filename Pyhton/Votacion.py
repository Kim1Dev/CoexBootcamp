while True:
    edad=int(input("Digite su edad "))
    print("")
    nacionalidad=str(input("Digite su nacionalidad "))
    print("")
    if edad>=18 and nacionalidad=="Colombiano":
        print("Puede votar")
    else:
        print("No puede votar")
        print("")
    menu = int(input("Digite 0 para salir ó 1 para continuar: "))
    print("")