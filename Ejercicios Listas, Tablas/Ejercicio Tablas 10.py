n = int (input ("\nIngrese el numero de columnas de la matriz: "))
m = int (input ("Ingrese el numero de filas de la matriz: "))

matriz = [[0 for i in range (n)]for i in range(m)]

print ("\n")

for i in range(len (matriz)):
    for e in range(len (matriz[1])):
        matriz[i][e] = float(input ("Ingrese un valor positivo entre 5 y 15: "))
        while matriz[i][e] < 5 or matriz[i][e] > 15:
            matriz [I][e] = float(input ("Valor no valido, Ingrese un valor positivo entre 5 y 15: "))

print ("\n")

for i in range(len (matriz)):
    for e in range (len (matriz[i])):
        print (matriz[i][e], end=" ")
    print()