cantidadLlantas = int(input("Ingrese la cantidad de llantas que desea comprar: "))
precioUnidad = float(input("Ingrese el precio por unidad: $"))

if cantidadLlantas == 1:
    DESCUENTO = 0
elif cantidadLlantas == 2:
    DESCUENTO = 20
elif cantidadLlantas == 3:
    DESCUENTO = 50
elif cantidadLlantas == 4:
    DESCUENTO = 100

llantaDescuento = DESCUENTO / 100 * precioUnidad 
totalCompra = cantidadLlantas * precioUnidad
totalPagar = totalCompra - llantaDescuento

print ("\nLa cantidad de llantas a comprar son: " + str(cantidadLlantas))
print ("El total de la compra fue de: $" + str(totalCompra))
print ("El descuento aplicado fue de un " + str(DESCUENTO) +"% el cual equivale a $" + str(llantaDescuento))
print ("El total a pagar es de $" + str(totalPagar))