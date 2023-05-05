n = 1
plantilla = 0

while n != 2:
    n = int(input("\n\nSeleccione una opcion:\n\n1.Añadir un empleado\n2.Finalizar programa\n\n"))
    
    if n == 1:
        s = float(input("\nIngrese el salario del empleado: $"))
        if s < 350:
            aumento = 0.11
        elif s >= 350 and s<600:
            aumento = 0.09
        elif s >= 600:
            aumento = 0.04
               
        aumento *= s
        salariofinal = s + aumento
        plantilla += salariofinal

        print("\nEl salario base es de $" + str(s) + "\nEl aumento es igual a $" + str(aumento) + "\n\nEl salario final es igual a $" + str(salariofinal) + "\n")
    
    elif n == 2:
        if plantilla == 0:
            print("\nPrograma Finalizado\n")
        else:
            print("\nEl total de la plantilla es igual a: $" + str(plantilla)+"\n")
    else:
        n = int(input("\n\nOpcion no valida seleccione otra opcion:\n1.Añadir un empleado\n2.Finalizar programa\n\n"))
