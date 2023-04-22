def calcular_mcd(num1, num2):
    if num2==0:
        return num1
    else:
        return calcular_mcd(num2, num1%num2)

num1=int(input("Ingrese el primero numero entero positivo"))
num2=int(input("Ingrese el segundo numero entero positivo"))

if num1 > 0 and num2 > 0:
    mcd = calcular_mcd (num1, num2)
    print("El maximo comun divisor de ", num1, "Y", num2, "es", mcd)
    
else:
    print("Los numero ingresados no son enteros positivos")