# TIPOS DE VADIACION: cada validacion devuelve un true o un false si esta se cumple o no

# Valida que la entrada no contenga unicamente espacios vacios:
def no_spaces(entrada):
    check = entrada.replace(" ", "")
    if len(check) == 0:
        return entrada, False
    else:
        return entrada, True

# Valida que la entrada sea de tipo entero: 
def value_int_input(entrada):
    try:
        entrada = int(entrada)
        return entrada, True
    except ValueError:
        return entrada, False

# ENTRADAS

# Verifica que la entrada no contenga solo espacios y que sea de tipo entero
def entrada_int_simple(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_int_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        return entrada

