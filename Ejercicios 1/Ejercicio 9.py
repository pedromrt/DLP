nombreVen = input ("\n\nIngrese el nombre del vendedor: ")
nombreClie = input ("Ingrese el nombre del cliente: ")
factuacionFech = input ("Ingrese la fecha de facturacion: ")
facturaNum = int (input ("Ingrese el numero de la factura: "))
sumaVent = float(input ("Ingrese la suma de las ventas realidas: "))

if sumaVent > 0 and sumaVent <100:
    
    DESCUENTO = 0.0
    descuentoPorcen = int(round(DESCUENTO * 100))
    descuento = sumaVent * DESCUENTO
    sumaTotal = sumaVent - descuento
    print ("\nNombre del vendedor:", nombreVen)
    print ("Nombre del cliente:",nombreClie)
    print ("Fecha de la factura:",factuacionFech)
    print ("Numero de factura",facturaNum)
    print ("Total en ventas $",format(sumaVent,'.2f'))
    print ("No se a aplicado ningun descuento a la compra")
    print ("\nEl total a pagar es de $",format(sumaTotal,'.2f'),"\n\n")

elif sumaVent >= 100 and sumaVent <=500:
    
    DESCUENTO = 0.15
    descuentoPorcen = int(round(DESCUENTO * 100))
    descuento = sumaVent * DESCUENTO
    sumaTotal = sumaVent - descuento
    print ("\nNombre del vendedor:", nombreVen)
    print ("Nombre del cliente:",nombreClie)
    print ("Fecha de la factura:",factuacionFech)
    print ("Numero de factura",facturaNum)
    print ("Total en ventas $",format(sumaVent,'.2f'))
    print ("Descuento aplicado del %",descuentoPorcen,"el cual equivale a $",format(descuento,'.2f'))
    print ("\nEl total a pagar con los descuentos aplicados es de $",format(sumaTotal,'.2f'),"\n\n")

elif sumaVent > 500 and sumaVent <= 1000:
    
    DESCUENTO = 0.20
    descuentoPorcen = int(round(DESCUENTO * 100))
    descuento = sumaVent * DESCUENTO
    sumaTotal = sumaVent - descuento
    print ("\nNombre del vendedor:", nombreVen)
    print ("Nombre del cliente:",nombreClie)
    print ("Fecha de la factura:",factuacionFech)
    print ("Numero de factura",facturaNum)
    print ("Total en ventas $",format(sumaVent,'.2f'))
    print ("Descuento aplicado del %",descuentoPorcen,"el cual equivale a $",format(descuento,'.2f'))
    print ("\nEl total a pagar con los descuentos aplicados es de $",format(sumaTotal,'.2f'),"\n\n")

elif sumaVent > 1000:
    
    DESCUENTO = 0.30
    descuentoPorcen = int(round(DESCUENTO * 100))
    descuento = sumaVent * DESCUENTO
    sumaTotal = sumaVent - descuento
    print ("\nNombre del vendedor:", nombreVen)
    print ("Nombre del cliente:",nombreClie)
    print ("Fecha de la factura:",factuacionFech)
    print ("Numero de factura",facturaNum)
    print ("Total en ventas $",format(sumaVent,'.2f'))
    print ("Descuento aplicado del %",descuentoPorcen,"el cual equivale a $",format(descuento,'.2f'))
    print ("\nEl total a pagar con los descuentos aplicados es de $",format(sumaTotal,'.2f'),"\n\n")
