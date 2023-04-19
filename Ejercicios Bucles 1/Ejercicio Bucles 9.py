numero = float(input("\nIngrese un numero positivo mayor a 12 y menor a 20: "))

while numero < 12 or numero > 20:
    numero = float(input("\nNumero incorrecto, ingrese un numero positivo mayor a 12 y menor a 20: "))

if numero % 2 == 0:
    print ("\n\nEl numero " + str(numero) + " es par\n")
else:
    print ("\n\nEl numero " + str(numero) + " es inpar\n")