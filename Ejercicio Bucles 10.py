import math

numero = float(input("\nIngrese un numero multiplo de 5: "))

while numero % 5 != 0:
    numero = float(input("\nNumero incorrecto, ingrese un numero multiplo de 5: "))

raiz = math.sqrt(numero)

print ("\n\nLa raiz cuadrada de " + str(numero) + " es " + str(raiz) + "\n")