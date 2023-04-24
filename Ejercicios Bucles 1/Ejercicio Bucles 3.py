import random   
sumaInpares = 0
sumaPares = 0
for i in range (1,301,1):
    randomNum = random.randint(1,1000)
    if randomNum % 2 != 0:
        sumaInpares += randomNum
    elif randomNum % 2 == 0:
        sumaPares += randomNum

promedio = sumaPares / i

print("La suma de los numeros inpares es ", sumaInpares)
print ("El promedio de los numeros pares es de ", promedio)