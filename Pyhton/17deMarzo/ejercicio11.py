cadena=input("Ingrese una cadena de caracteres: ")
letras_contador={}

for letra in cadena:
    if letra in letras_contador:
        letras_contador[letra]+=1
    else:
        letras_contador[letra]=1
        
print("Contador de letras: ")
for letra, contador in letras_contador.items():
    print(letra, ":", contador)