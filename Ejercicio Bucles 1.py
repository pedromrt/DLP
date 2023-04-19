trabas = 1
plantilla = 0
for trabas in range (1,11,1):
    sueldo = float(input("Ingrese el salario de el trabajador: $"))
    if sueldo < 800:
        aumento = 0.15
    else:
        aumento = 0

    sueldoFin = sueldo + sueldo * aumento
    plantilla = plantilla + sueldoFin
    print("Su sueldo final es de $"+ str(sueldoFin))

print ("\nEl sueldo total de la plantilla es de $" + str(plantilla))