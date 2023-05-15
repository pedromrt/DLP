precioBase = float(input("\nIngrese el precio de la computadora: $"))
marca = int(input("\nSeleccione la marca:\n\n1.HP\n2.DELL\n3.SONY\n4.TOSHIBA\n\nIngrese el numero que desea seleccionar: "))

IVA = 13

iva = IVA / 100 * precioBase

precioIVA = precioBase + iva

if marca == 1:
    IMPUESTO = 12
    DESCUENTO = 20
    marca = "HP"

elif marca == 2:
    IMPUESTO = 10
    DESCUENTO = 10
    marca = "DELL"


elif marca == 3:
    IMPUESTO = 13
    DESCUENTO = 15
    marca = "SONY"

elif marca == 4:
    IMPUESTO = 7
    DESCUENTO = 10
    marca = "TOSHIBA"

impuesto = IMPUESTO / 100 * precioIVA
descuento = DESCUENTO / 100 * precioIVA

precioFinal = precioIVA + impuesto - descuento

print ("\nLa marca de computadora es : " + marca)
print ("\nEl precio original es de " + str(precioBase))
print ("\nLos impuestos aplicados fueron:\n\n    IVA" + str(IVA) + "% el cual representa " + str(iva) + "\n    Impuestos" + str(IMPUESTO) + "% el cual representa " + str(impuesto))
print ("\nLos descuentos aplicados fueron:\n\n    Descuentos" + str(DESCUENTO) + "% el cual representa " + str(descuento))
print ("\nEl precio final es de $" + str(precioFinal) + "\n")