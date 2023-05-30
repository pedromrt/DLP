while True:

    try:
        centi = float(input("\n\nIngrese los grados centigrados a convertir: "))

    except ValueError:
        while True:
            try:
                centi = float(input("Tipo de dato no valido, ingrese los grados centigrados a convertir: "))
                break
            except ValueError:
                continue
    
    fahrenheit = 9/5 * centi + 32

    print("\n" + str(centi) + " grados centigrados es igual a " + str(round(fahrenheit,2)) + " grados fahrenheit")
    
    print("\n\n¿Desea calcular otra temperatura?\n\n1. Si\n2. No")
    try:
        i = int(input("\nEscriba el numeral de la opcion que desea seleccionar: "))

    except ValueError:
        while True:
            try:
                i = int(input("Tipo de dato no valido, escriba el numeral de la opcion que desea seleccionar: "))
                break
            except ValueError:
                continue

    if i == 2:
        break

print ("\n\nPrograma finalizado...\n")