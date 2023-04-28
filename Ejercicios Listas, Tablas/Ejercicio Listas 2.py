lstNombres = []
lstEdad = []
lstSalario = []
continuar = 1
while continuar == 1:
    lstNombres.append(input("\nIngrese el nombre del empleado: "))
    lstEdad.append(int(input("Ingrese la edad del empleado: ")))
    lstSalario.append(float(input("Ingrese el salario del empleado: $")))
    continuar = int(input("\n¿Desea añadir otro empleado? (Escriba 1 para si y 2 para no)  "))   

salarioMax = max(lstSalario)
indice = lstSalario.index(salarioMax)

print("\nEl empleado mejor pagado es " + lstNombres[indice])