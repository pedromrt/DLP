cont = 1
positivos = 0
negativos = 0
nulos = 0

for cont in range (1,6,1):
    numero = int(input("Ingrese un numero entero: "))

    if numero == 0:
        nulos = nulos + 1
    elif numero < 0:
        positivos = positivos + 1
    elif numero > 0:
        negativos = negativos + 1

print ("\nUsted escribio",positivos, "positivos")
print ("Usted escribio",negativos, "negativos")
print ("Usted escribio",nulos, "nulos")

