matriz = [[0 for i in range (3)]for i in range (2)]

minXFila = []
maxXColum = []

for i in range (len(matriz)):
        for j in range (len(matriz[i])): 
            matriz[i][j] = int(input("Ingrese un numero positivo y entero: "))
            while matriz[i][j] <= 0:
                matriz[i][j] = int(input("Numero invalido,  ingrese un numero positivo y entero: "))
           
for i in range(len(matriz)):
    minXFila.append(min(matriz[i]))
    maxXColum.append(max(matriz[i]))


minimo = min (minXFila)
indiceMin = minXFila.index(minimo)

maximo = max (maxXColum)
indiceFila = maxXColum.index(maximo)
indiceMax = matriz[indiceFila].index (maximo)


print ()
print ("El valor menor esta en la fila " + str(indiceMin + 1)) 
print("El valor mayor esta en la columna " + str(indiceMax + 1))