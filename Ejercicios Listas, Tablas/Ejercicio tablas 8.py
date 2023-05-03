matriz = [[0 for j in range(3)] for i in range(2)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])): 
        matriz[i][j] = int(input("Ingrese un numero positivo y entero: "))
        while matriz[i][j] <= 0:
            matriz[i][j] = int(input("Numero invalido,  ingrese un numero positivo y entero: "))
            
