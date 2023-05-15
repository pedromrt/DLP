n = int(input("Ingrese el numero de estudiantes a evaluar: "))

aprobados = 0
reprobados = 0
sumaNotas = 0
sumaAprovados = 0

for i in range (n):
    nota = float(input("\nIngrese la nota del estudiante " + str(i+1) + ": "))
    
    if nota >= 7 and nota <=10:
        aprobados += 1
        sumaAprovados += nota
    else:
        reprobados += 1
    
    sumaNotas += nota

promedioNotas = sumaNotas / n
promedioAprovados = sumaAprovados / aprobados

print ("\nSe registro un total de " + str(n) + " estudiantes.")
print ("De estos " + str(aprobados) + " fueron aprobados")
print ("Y " + str(reprobados) + " fueron reprobados")
print ("La nota promedio de los estudiantes aprovados fue " + str(promedioAprovados))
print ("La nota promedio de los estudiantes en general fue " + str(promedioNotas))