nTabla=int(input("Digite la tabla que desea consultar: "))
def funcion(nTabla , i):
    return nTabla*i

for i in range(11):
        print(str(nTabla) + " ×" , str(i) , " = " , str(funcion(nTabla, i)))