compra = float (input("\nIngrese el total de su compra: $"))
randomNum = int (input("\nIngrese el numero aleatorio: $"))

DESCUENTOMEN = 0.15
DESCUENTOMAY = 0.20

if randomNum >= 74 :
    descuento = compra * DESCUENTOMAY
    
else:
    descuento = compra * DESCUENTOMEN

totalCom = compra - descuento
print ("\n\nEl total de su compra es de $",compra)
print ("\nSu descuento es de $",descuento)
print ("\nSu total a pagar es de $",totalCom,"\n")