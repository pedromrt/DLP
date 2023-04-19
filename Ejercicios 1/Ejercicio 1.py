saldo = float(input("\nIngrese su saldo actual: $"))

INTERES = 0.03

intereses = saldo * INTERES

if intereses > 1500 :
    saldoFin = saldo + intereses
    print ("\nSu nuevo saldo es de: $",saldoFin)
    print ("Se añadieron $",intereses,"al saldo de su cuenta\n")

else:
    print ("\nSu saldo se mantiene en: $",saldo)
