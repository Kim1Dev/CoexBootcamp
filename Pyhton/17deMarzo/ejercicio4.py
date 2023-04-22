num=int(input("Ingrese un numero enero positivo: "))
factorial=1
if num<0:
    print("El factoral no esta definido para numero negativos")
elif num==0:
    print("El factorial de 0 es 1")
else:
    for i in range(1, num+1):
        factorial*=i
    print("El factorial ", num, "es", factorial)