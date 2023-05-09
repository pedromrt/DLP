xA = Int (Input("\nIngrese el numero de columnas de la matriz A: "))
yA = Int(Input ("Ingrese el numero de filas de la matriz A: "))

matrizA = [[0 for i in range (xA) ]for i in range(yA)]

print ("\n")

for i in range (len (natrizA)):
    for e in range(len (matrizA[i])):
        matrizA[i][e] = int(input("Ingrese un valor entero para la matriz A: "))

xB = Int(Input("IninIngrese el numero de columnas de la matriz 8: "))
yB = Int(Input("Ingrese el numero de filas de la matriz 8: "))

print ("\n")

matrizB = [[0 for i in range (xB)]for i in range(yB)]

for i in range(len (matrizB)):
    for e in range(len(matrizB[i])):
        matrizB[i][e] = int(input("Ingrese un valor entero para la natriz B: "))

if matrizA == matrizB:
    print ("\n\nLa matriz A y B son iguales\n")
else:
    print("\n\nLa matriz A y B son diferentes\n")