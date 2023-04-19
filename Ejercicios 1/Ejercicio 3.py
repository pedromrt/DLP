valorP = int (input("\nIngrese el valor entero de P: "))
valorQ = int (input("\nIngrese el valor entero de Q: "))

condicion = valorP * 3 + valorQ * 4 - 2 * valorP * 2 < 680

if condicion == True:
    print ("\nEl valor de 'P' es igual a: ",valorP)
    print ("\nEl valor de 'Q' es igual a: ",valorQ,"\n")
else:
    print ("\nLos valores para 'P' y 'Q' no satisfacen la expresión\n")