valor = int(input('Ingrese cuantas veces desea hacer la operacion fibonacci: '))

cont = 1
a=0
b=1
c=0

print (a)
print (b)

while True:
    c=a+b
    a=b
    b=c
    cont=cont+1
    print (b)
    if cont > valor:
        break