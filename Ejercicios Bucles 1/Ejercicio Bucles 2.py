positivos = 0
negativos = 0
nulos = 0

for i in range (1,101,1):
    numero = int(input("Ingrese un numero entero: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        nulos += 1

print ("\nUsted escribio",positivos, "positivos")
print ("Usted escribio",negativos, "negativos")
print ("Usted escribio",nulos, "nulos")