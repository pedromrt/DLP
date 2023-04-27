listA = []
listB = []
listResult = []

nvectores = 4
productoTotal = 1

for i in range (0,nvectores,1):
    listA.append(int(input("\nIngrese un valor para A: ")))
    listB.append(int(input("Ingrese un valor para B: ")))
    listResult.append(listA[i] * listB[i])
    
for i  in range (0,nvectores,1):
    producto = listResult[i]
    print("\nEl producto del vector", i+1, "es igual a", producto)
    
for i in range(0,nvectores,1):
    productoTotal *= listA[i] * listB[i]
    
print("\nEl producto total de todos los vectores de A y B es igual a:", productoTotal)