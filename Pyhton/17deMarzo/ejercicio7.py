palabras=input("Ingrese una lista de palabras separadas por coma ")
palabras_listas=palabras.split((","))

longitud_maximo=0

for palabra in palabras_listas:
    longitud_palabra=len(palabra.strip())
    
    if longitud_palabra>longitud_maximo:
        longitud_maximo=longitud_palabra
        
print("La longitud de la palabra es ", longitud_maximo)