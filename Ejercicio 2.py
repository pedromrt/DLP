sueldoTraba = float (input("\n Ingrese su sueldo: $"))

aumento= sueldoTraba * 0.15
if  sueldoTraba>=550:
    sueldoNuevo=sueldoTraba + aumento
    print ("\n Su sueldo es de: $", sueldoTraba)
    print ("\n El total de su aumento es: $", aumento)
    print ("\n El total de su nuevo sueldo es: $", sueldoNuevo,"\n")
else:
    sueldoNuevo=sueldoTraba
    print ("\n Su sueldo es de: $", sueldoTraba)
    print ("\n Usted no aplica para el aumento.\n") 
    