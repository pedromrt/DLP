i = 2
suma = 0
while i <= 1800:
    if i % 5 == 0:
        i += 2
    else:
        i += 3
    suma = suma + i
    
print("\nLa suma de la serie es igual a ", suma,"\n")