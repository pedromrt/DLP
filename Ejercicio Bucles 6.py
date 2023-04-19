continuar = 1
sumaSal = 0
while continuar == 1:
    n = float(input("\nEsbriba su salario: $"))
    sumaSal = sumaSal + n
    continuar = int( input("\n¿Desea continuar?\nEscriba 1 para Si y 0 para No: "))

print ("\nEl salario total de la plantilla es de $", sumaSal,"\n")