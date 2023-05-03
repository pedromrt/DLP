matriz = [[0 for j in range(6)] for i in range(6)]

for i in range(6):
    matriz[i][i] = 1

for i in range(6):
    matriz[i][-i-1] = 1

for i in matriz:
    print(i)
    
