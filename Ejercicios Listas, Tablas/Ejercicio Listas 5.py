n = int(input("\nIngrese la cantidad de productos en la compra: "))
print("")
porcentajeDescuento = 0.10
totalNoImpuestos = 0

lstProducto = []
lstCantidad = []
lstPrecio = []
lstCanPrecio = [] 

for i in range (0,n,1):
    lstProducto.append(input("\nNombre del producto: "))
    lstCantidad.append(int(input("Cantidad: ")))
    lstPrecio.append(float(input("Ingrese el precio por unidad: $")))
    lstCanPrecio.append(lstCantidad[i]*lstPrecio[i])
    totalNoImpuestos += lstCanPrecio[i]

desuento = porcentajeDescuento * totalNoImpuestos
totalFinal = totalNoImpuestos - desuento

print("\n\nFACTURA")
for i in range (0,n,1):
    print ("\n" + str(lstProducto[i]), "      ", lstCantidad[i], "Unidades        $" + str(lstPrecio[i]), "\nSubtotal           $" + str(lstCanPrecio[i]))

print ("\nDescuento del " + str(int((100*porcentajeDescuento))) + "% por renta igual a $" + str(desuento))
print ("\nTOTAL:    $" + str(totalFinal) + "\n")   