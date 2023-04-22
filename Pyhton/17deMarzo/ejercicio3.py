num=int(input("Ingrese un numero entero posivo mayor que 1: "))

if num>1:
   es_primo=True
   for i in range(2, num):
      if num%i==0:
         es_primo=False
         break
   if es_primo:
      print(num, "es un numero primo.")
   else:
      print(num, "no es un numero primo")
else:
   print(num, "No es un numero entero positivo mayor que 1")