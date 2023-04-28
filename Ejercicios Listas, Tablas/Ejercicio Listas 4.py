listA = []
listB = []
listResult = []

vectores = 1
productoTotal = 1

while vectores == 1:
    listA.append(int(input("\nIngrese un valor para A: ")))
    listB.append(int(input("Ingrese un valor para B: ")))
    vectores = int(input("\n¿Desea añadir otro vector? (Escriba 1 para si y 2 para no)  "))   

    
for i  in range (0,len(listA),1):
    listResult.append(listA[i] * listB[i])
    producto = listResult[i]
    print("\nEl producto del vector", i+1, "es igual a", producto)
    
for i in range(0,len(listA),1):
    productoTotal *= listA[i] * listB[i]
    
print("\n\nEl producto total de todos los vectores de A y B es igual a:", productoTotal,"\n")