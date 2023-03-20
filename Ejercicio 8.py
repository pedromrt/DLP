monto = float(input("\nIngrese el total a pagar: $"))

MAXIMOEXED = 50000
PRESTAMO = 0.30
prestamo = monto * PRESTAMO

if monto > MAXIMOEXED:
    
    EMPRESA = 0.55
    empresaPorcen = int(EMPRESA * 100)
    empresa = monto * EMPRESA
    
    PRESTAMO = 0.30
    prestamoPorcen = int(PRESTAMO * 100)
    prestamo = monto * PRESTAMO
    
    valorCred = 1 - (EMPRESA + PRESTAMO)
    creditoPorcen = int(round(valorCred * 100))
    credito = monto * valorCred
    
    INTERES = 0.20
    interesPorcen = int(INTERES * 100)
    intereses = credito * INTERES
    creditoPagar = credito + intereses
    
    print ("\nEl monto de la compra a realizar es de $",format(monto,'.2f'))
    print ("\nPor ende la empresa realizara una inversion de un %",empresaPorcen,"el cual equivale a $",format(empresa,'.2f'))
    print ("\nSe requerirá un prestamo al banco del %",prestamoPorcen,"el cual equivale a $",format(prestamo,'.2f'))
    print ("\nTambien se requerira un credito al fabricante del %",creditoPorcen,"el cual equivale a $",format(credito,'.2f'))
    print ("\nEste credito se realizara a una taza del %",interesPorcen,"el cual equivale a $",format(intereses,'.2f'))
    print ("\nPor tanto se acabará pagando un credito total de $",format(creditoPagar,'.2f'),"al fabricante")
    print ("\nEl valor total de la compra es de $",format((empresa + prestamo + creditoPagar),'.2f'),"iclyendo intereses.\n\n")

else:
    EMPRESA = 0.70
    empresa = monto * EMPRESA
    empresaPorcen = int(EMPRESA * 100)
    
    valorCred = 1 - EMPRESA
    creditoPorcen = int(round(valorCred * 100))
    credito = monto * valorCred
    
    INTERES = 0.20
    intereses = credito * INTERES
    interesPorcen = int(INTERES * 100)
    creditoPagar = credito + intereses

    print ("\nEl monto de la compra a realizar es de $",monto)
    print ("\nPor ende la empresa realizara una inversion de un %",empresaPorcen,"el cual equivale a $",format(empresa,'.2f'),)
    print ("\nTambien se requerira un credito al fabricante del %",creditoPorcen,"el cual equivale a $",format(credito,'.2f'))
    print ("\nEste credito se realizara a una taza del %",interesPorcen,"el cual equivale a $",format(intereses,'.2f'))
    print ("\nPor tanto se acabará pagando un credito total de $",format(creditoPagar,'.2f'),"al fabricante")
    print ("\nEl valor total de la compra es de $",format((empresa + creditoPagar),'.2f'),"iclyendo intereses.\n\n")