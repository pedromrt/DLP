nombrePa = input("\nIngrese su nombre: ")
n = float(input("\nIngrese el numero de dias que estuvo ingresado: "))
operacion = input("\nEl paciente requiere operacion (Escriba SI o NO): ")

HONORARIOS = 0.20
OPERACION = 1000
VALORDIAS = 25

costoDiario = n * VALORDIAS

if operacion == "SI":
    pago = OPERACION + costoDiario
    honorarios = pago * HONORARIOS
    pagoTotal = pago + honorarios
    print ("\n\n\nSu nombre es:",nombrePa)
    print ("\nUsted estuvo un total de",n,"dias en este hospital")
    print ("\n\nSus gastos se dividen en:")
    print ("\nOperacion: $",OPERACION)
    print ("Costo de hospitalizacion por",n,"dias: $",costoDiario)
    print ("Honorarios del medico: $",honorarios)
    print ("\nSu total a pagar es de: $",pagoTotal,"\n")
else:
    pago = costoDiario
    honorarios = pago * HONORARIOS
    pagoTotal = pago + honorarios
    print ("\n\n\nSu nombre es:",nombrePa)
    print ("\nUsted estuvo un total de",n,"dias en este hospital")
    print ("\n\nSus gastos se dividen en:")
    print ("\nCosto de hospitalizacion por",n,"dias: $",costoDiario)
    print ("Honorarios del medico: $",honorarios)
    print ("\nSu total a pagar es de: $",pagoTotal,"\n")