n = int(input("\nIngrese el número de empleados: "))

suma = 0
cont = 0

while cont < n:
    monto = float(input("\nIngrese el monto de venta del empleado: $"))
    suma += monto
    cont += 1

promedio = suma / n

print ("\n\nEl promedio de ventas es:",promedio,"\n")