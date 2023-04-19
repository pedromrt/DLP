i = 10
suma = 0
producto = 1
while i <= 30:
    if i % 2 == 0:
        suma = suma + i
        producto = producto * i
    i += 1

print ("\nLa suma de los numeros es igual a", suma)
print ("El producto de los numeros es iguao a", producto)