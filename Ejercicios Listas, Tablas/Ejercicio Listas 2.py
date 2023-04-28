lstNombres = []
lstEdad = []
lstSalario = []
empleados = 1
while empleados == 1:
    lstNombres.append(input("\nIngrese el nombre del empleado: "))
    lstEdad.append(int(input("Ingrese la edad del empleado: ")))
    lstSalario.append(float(input("Ingrese el salario del empleado: $")))
    empleados = int(input("\n¿Desea añadir otro vector? (Escriba 1 para si y 2 para no)  "))   

salarioMax = max(lstSalario)
indice = lstSalario.index(salarioMax)

print("\nEl empleado mejor pagado es " + lstNombres[indice])