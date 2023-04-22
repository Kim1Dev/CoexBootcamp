from Loteria import*

x= rn()

while True:
    numero=int(input("Ingrese el numero del 1 al 10 que desee "))
    if x>numero:
        print("El numero es mayor")
    elif numero<x:
        print("El numero es menor")
    else:
        print("Has ganado")
        break