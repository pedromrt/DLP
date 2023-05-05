montoCompra = float(input("\nIngrese el monto de la compra: $"))
tipoPago = int(input("\nMetodo de pago:\n\n1.Contado\n2.Cheque\n3.Credito\n4.Letras de cambio\n\nIngrese el indice del metodo a utilizar: "))

if tipoPago == 1:
    descuento = 0.2
    recargo = 0.02

elif tipoPago == 2:
    descuento = 0.12
    regargo = 0.07

elif tipoPago == 3:
    descuento = 0.15
    regargo = 0.11

elif tipoPago == 4:
    descuento = 0.10
    regargo = 0.08

descuento *= montoCompra
recargo *= montoCompra
totalPagar = montoCompra - descuento + recargo

print ("\n\nEl monto de la compra es de:\n   $" + str(montoCompra))
print ("\nEl descuento de la compra es de:\n   $" + str(descuento))
print ("\nEl recargo de la compra es de:\n   $" + str(recargo))
print ("\n\nEl total a pagar es de:\n   $" + str(totalPagar) + "\n")