numeros=[]
while True:
    num=input("Ingrese un numero o presione enter para finalizar")
    if num==" ":
        break
    numeros.append(float(num))
    
if len(numeros)==0:
    print("No se ingresaron numeros")

else:
    media=sum(numeros)/len(numeros)
    print("La media de los numeros ingresados es: ", media)
    