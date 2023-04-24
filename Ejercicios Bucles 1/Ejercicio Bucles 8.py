n = int(input("\nIngrese el número de empleados: "))

suma = 0
i = 1

while i <= n:
    monto = float(input("\nIngrese el monto de venta del empleado: $"))
    suma += monto
    i += 1

promedio = suma / n

print ("\n\nEl promedio de ventas es:",promedio,"\n")