n = 1
porcentajeDescuento = 0.10
totalNoImpuestos = 0

lstProducto = []
lstCantidad = []
lstPrecio = []
lstCanPrecio = [] 

while n == 1:
    lstProducto.append(input("\nNombre del producto: "))
    lstCantidad.append(int(input("Cantidad: ")))
    lstPrecio.append(float(input("Ingrese el precio por unidad: $")))
    n = int(input("\n¿Desea añadir otro producto? (Escriba 1 para si y 2 para no)  "))       

for i in range(0,len(lstProducto),1):
    lstCanPrecio.append(lstCantidad[i]*lstPrecio[i])
    totalNoImpuestos += lstCanPrecio[i]

desuento = porcentajeDescuento * totalNoImpuestos
totalFinal = totalNoImpuestos - desuento

print("\n\nFACTURA")
for i in range (0,n,1):
    print ("\n" + str(lstProducto[i]), "      ", lstCantidad[i], "Unidades        $" + str(lstPrecio[i]), "\nSubtotal           $" + str(lstCanPrecio[i]))

print ("\nDescuento del " + str(int((100*porcentajeDescuento))) + "% por renta igual a $" + str(desuento))
print ("\nTOTAL:    $" + str(totalFinal) + "\n")   