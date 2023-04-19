horas = float (input("\nIngrese la cantidad de horas trabajadas: "))

VALORH1 = 4
VALORH2 = 6
HORASBASE = 40

horasext = horas - HORASBASE
salario1 = horas * VALORH1

if horas <= HORASBASE:
    salario = salario1
    print ("\n\nUstd trabajo un total de",horas,"horas")
    print("\nSu salario total sera de $",salario,"\n")
else:
    pagoext = horasext * VALORH2
    salario = salario1 + pagoext
    print ("\n\nUstd trabajo un total de",horas,"horas")
    print ("\nDe las cuales",horasext,", siendo estas horas extras, seran pagadas a $",VALORH2,"la hora")
    print ("\nSu salario total sera de $",salario,"\n")