import random   
rango = 1
sumaInpares = 0
promedio = 0
for rango in range (1,301,1):
    randomNum = random.randint(1,1000)
    if randomNum % 2 != 0:
        sumaInpares = sumaInpares + randomNum
    elif randomNum % 2 == 0:
        promedio = (promedio + randomNum) / rango

print("La suma de los numeros inpares es ", sumaInpares)
print ("El promedio de los numeros pares es de ", promedio)