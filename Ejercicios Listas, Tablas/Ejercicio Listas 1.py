lstNombres = []
lstEdad = []
lstSalario = []
i = 1

while i <= 5:
    lstNombres.append(input("\nIngrese el nombre del empleado #" + str(i) + ": "))
    lstEdad.append(int(input("Ingrese la edad del empleado: ")))
    lstSalario.append(float(input("Ingrese el salario del empleado: $")))
    i += 1


salarioMax = max(lstSalario)
indice = lstSalario.index(salarioMax)

print("\nEl empleado mejor pagado es " + lstNombres[indice] + "\n")
