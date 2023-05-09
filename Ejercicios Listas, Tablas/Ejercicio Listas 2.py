lstNombres = []
lstEdad = []
lstSalario = []
n = 1

while n == 1:
    lstNombres.append(input("\nIngrese el nombre del empleado: "))
    lstEdad.append(int(input("Ingrese la edad del empleado: ")))
    lstSalario.append(float(input("Ingrese el salario del empleado: $")))
    n = int(input("\n¿Desea añadir otro empleado? (Escriba 1 para si y 2 para no): "))
    while n != 1 and n != 2:
        n = int(input("\nValor no valido ¿Desea añadir otro empleado? (Escriba 1 para si y 2 para no): "))

salarioMax = max(lstSalario)
indice = lstSalario.index(salarioMax)

print("\nEl empleado mejor pagado es " + lstNombres[indice] + "\n")