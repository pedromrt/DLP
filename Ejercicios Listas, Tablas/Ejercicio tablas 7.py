import random

sumPares = 0
sumInpares = 0

matriz = [[random.randint(10,99) for j in range(10)] for i in range(6)]

for i in matriz:
    print (i)
    
for i in range (len(matriz)):
    for k in range (len(matriz[i])): 
        if matriz[i][k] % 2 == 0:
            sumPares += 1
        else:
            sumInpares += 1

print("\nLa suma de numeros pares es igual a " + str(sumPares))
print("\nLa suma de numeros inpares es igual a " + str(sumInpares))