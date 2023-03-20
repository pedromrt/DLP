salarioMens = float (input("\nIngrese su salario mensual: $"))
antiguedad = int (input("\nIngrese la cantidad de meses que a estado en la compañia: "))

años = antiguedad // 12
mesesExtr = antiguedad % 12


if años < 1 :
    
    UTILIDAD = 0.05
    porcentajeUTL = int(UTILIDAD * 100)
    utilidad = salarioMens * UTILIDAD
    print ("\n\nSu salario mensual es de $",format(salarioMens,'.2f'))
    print ("Usted a trabajado",mesesExtr,"meses para esta compañia")
    print ("Su utilidad anual es del %",porcentajeUTL,"lo cual representa $",utilidad,"\n\n")

elif años >= 1 and años < 2:
    
    UTILIDAD = 0.07
    porcentajeUTL = int(UTILIDAD * 100)
    utilidad = salarioMens * UTILIDAD
    print ("\n\nSu salario mensual es de $",format(salarioMens,'.2f'))
    print ("Usted a trabajado",años,"año y",mesesExtr,"meses para esta compañia")
    print ("Su utilidad anual es del %",porcentajeUTL,"lo cual representa $",utilidad,"\n\n")

elif años >= 2 and años < 5:
    
    UTILIDAD = 0.10
    porcentajeUTL = int(UTILIDAD * 100)
    utilidad = salarioMens * UTILIDAD
    print ("\n\nSu salario mensual es de $",format(salarioMens,'.2f'))
    print ("Usted a trabajado",años,"años y",mesesExtr,"meses para esta compañia")
    print ("Su utilidad anual es del %",porcentajeUTL,"lo cual representa $",utilidad,"\n\n")

elif años >= 5 and años < 10:
    
    UTILIDAD = 0.15
    porcentajeUTL = int(UTILIDAD * 100)
    utilidad = salarioMens * UTILIDAD
    print ("\n\nSu salario mensual es de $",format(salarioMens,'.2f'))
    print ("Usted a trabajado",años,"años y",mesesExtr,"meses para esta compañia")
    print ("Su utilidad anual es del %",porcentajeUTL,"lo cual representa $",utilidad,"\n\n")

elif años >= 10:
    
    UTILIDAD = 0.20
    porcentajeUTL = int(UTILIDAD * 100)
    utilidad = salarioMens * UTILIDAD
    print ("\n\nSu salario mensual es de $",format(salarioMens,'.2f'))
    print ("Usted a trabajado",años,"años y",mesesExtr,"meses para esta compañia")
    print ("Su utilidad anual es del %",porcentajeUTL,"lo cual representa $",utilidad,"\n\n")