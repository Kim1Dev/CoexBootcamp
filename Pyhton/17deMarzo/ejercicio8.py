num=int(input("Ingrese un numero entero: "))

print("los divisores de ", num, "son: ")

for i in range(1, num+1):
    if num%i==0:
        print(i)