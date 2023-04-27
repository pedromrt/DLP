lstNombres = []
lstEdad = []
lstSalario = []
n = (int(input("Ingrese la cantidad de empleados: ")))

for i in range(0,n,1):
    lstNombres.append(input("\nIngrese el nombre del empleado: "))
    lstEdad.append(int(input("Ingrese la edad del empleado: ")))
    lstSalario.append(float(input("Ingrese el salario del empleado: $")))

salarioMax = max(lstSalario)
indice = lstSalario.index(salarioMax)

print("\nEl empleado mejor pagado es " + lstNombres[indice] )