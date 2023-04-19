n = 1
sumaSal = 0
while n == 1:
    salario = float(input("\nEsbriba su salario: $"))
    sumaSal = sumaSal + salario
    n = int( input("\n¿Desea continuar?\nEscriba 1 para Si y 0 para No: "))

print ("\nEl salario total de la plantilla es de $", sumaSal,"\n")