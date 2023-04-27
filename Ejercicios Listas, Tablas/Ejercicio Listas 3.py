lista1 = []
lista2 = []
lista3 = []

for i in range(0,15,1):
    numero = float(input("\nIngrese un numero: "))
    if numero >= 0 and numero < 50:
        lista1.append(numero)
    elif numero >=50 and numero < 100:
        lista2.append(numero)
    elif numero >= 100 and numero <= 150:
        lista3.append(numero)
        
print ("\n", lista1,"\n", lista2, "\n", lista3)