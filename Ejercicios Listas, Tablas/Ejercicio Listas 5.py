n = 1
porcentajeDescuento = 0.10
totalNoDescuento = 0

lstProducto = []
lstCantidad = []
lstPrecio = []
lstCanPrecio = [] 

while n == 1:
    lstProducto.append(input("\nNombre del producto: "))
    lstCantidad.append(int(input("Cantidad: ")))
    lstPrecio.append(float(input("Ingrese el precio por unidad: $")))
    n = int(input("\n¿Desea añadir otro producto? (Escriba 1 para si y 2 para no): "))
    while n != 1 and n != 2:
        n = int(input("\nValor no valido ¿Desea añadir otro producto? (Escriba 1 para si y 2 para no): "))    

for i in range(len(lstProducto)):
    lstCanPrecio.append(lstCantidad[i]*lstPrecio[i])
    totalNoDescuento += lstCanPrecio[i]

desuento = porcentajeDescuento * totalNoDescuento
totalFinal = totalNoDescuento - desuento

print("\n\nFACTURA")
for i in range (len(lstProducto)):
    print ("\n" + str(lstProducto[i]), "      ", lstCantidad[i], "Unidades        $" + str(lstPrecio[i]), "\nSubtotal           $" + str(lstCanPrecio[i]))

print ("\nDescuento del " + str(int(100*porcentajeDescuento)) + "% por renta igual a $" + str(desuento))
print ("\nTOTAL:    $" + str(totalFinal) + "\n")