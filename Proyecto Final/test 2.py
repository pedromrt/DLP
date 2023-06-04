import re

def no_spaces(entrada):
    check = entrada.replace(" ", "")
    if len(check) == 0:
        return entrada, False
    else:
        return entrada, True

def value_int_input(entrada):
    try:
        entrada = int(entrada)
        return entrada, True
    except ValueError:
        return entrada, False

def value_float_input(entrada):
    try:
        entrada = float(entrada)
        return entrada, True
    except ValueError:
        return entrada, False

def range_options(entrada, lower, bigger):
    if entrada < lower or entrada > bigger:
        return entrada, False
    else:
        return entrada, True

def input_limitado(entrada, limite_top, limite_bot):
    entrada = str(entrada)
    if len(entrada) > limite_top or len(entrada) < limite_bot:
        return entrada, False
    else:
        return entrada, True

def no_numbers_in_str(entrada):
    entrada = str(entrada)
    if entrada.isdigit():
        return entrada, False
    else:
        return entrada, True

def no_special_character(entrada, caracteres_permitidos=None):
    entrada = str(entrada)
    if caracteres_permitidos is None:
        patron = r'^[a-zA-Z0-9]+$'
    else:
        patron = r'^[a-zA-Z0-9{}]+$'.format(re.escape(caracteres_permitidos))
    if re.match(patron, entrada):
        return entrada, True
    else:
        return entrada, False



# TIPOS DE ENTRADAS

# Entradas int

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

def entrada_int_rango(mensaje,lower,bigger):
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

        entrada, check3 = range_options(entrada, lower, bigger)
        if check3 == False:
            print("\nEntrada fuera del rango de opciones, intente de nuevo")
            continue
        
        return entrada    

def entrada_int_limite(mensaje,limite_bot,limite_top):
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

        entrada, check3 = input_limitado(entrada, limite_top, limite_bot)
        if check3 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue
        
        return entrada

def entrada_int_rango_limite(mensaje,lower,bigger,limite_bot,limite_top):
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

        entrada, check3 = range_options(entrada, lower, bigger)
        if check3 == False:
            print("\nEntrada fuera del rango de opciones, intente de nuevo")
            continue    
        
        entrada, check4 = input_limitado(entrada, limite_top, limite_bot)
        if check4 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        return entrada    

# Entradas float

def entrada_float_simple(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_float_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        return entrada

def entrada_float_rango(mensaje,lower,bigger):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_float_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = range_options(entrada, lower, bigger)
        if check3 == False:
            print("\nEntrada fuera del rango de opciones, intente de nuevo")
            continue
        
        return entrada    

def entrada_float_limite(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_float_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = input_limitado(entrada, limite_top, limite_bot)
        if check3 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue
        
        return entrada

def entrada_float_rango_limite(mensaje,lower,bigger,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = value_float_input(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = range_options(entrada, lower, bigger)
        if check3 == False:
            print("\nEntrada fuera del rango de opciones, intente de nuevo")
            continue    
        
        entrada, check4 = input_limitado(entrada, limite_top, limite_bot)
        if check4 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        return entrada    

# Entradas str

def entrada_str_simple(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_special_character(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        return entrada

def entrada_str_limite(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_special_character(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        entrada, check3 = input_limitado(entrada,limite_top, limite_bot)
        if check3 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        return entrada    
    
def entrada_str_no_numbers(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_special_character(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = no_numbers_in_str(entrada)
        if check3 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        return entrada 

def entrada_str_limite_no_numbers(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_special_character(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue
        
        entrada, check3 = input_limitado(entrada, limite_top, limite_bot)
        if check3 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        entrada, check4 = no_numbers_in_str(entrada)
        if check4 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        return entrada 


# Tests:

while True:

    #int

    print("\n",entrada_int_simple("\nEntrada int simple: "))

    print("\n",entrada_int_rango("\nEntrada int rango: ", 1, 5))

    print("\n",entrada_int_limite("\nEntrada int limite: ", 1, 6))

    print("\n",entrada_int_rango_limite("\nEntrada int rango limite: ", 1, 5000, 2, 3))

    #float
    
    print("\n",entrada_float_simple("\nEntrada int simple: "))

    print("\n",entrada_float_rango("\nEntrada int rango: ", 1, 5))

    print("\n",entrada_float_limite("\nEntrada int limite: ", 1, 6))

    print("\n",entrada_float_rango_limite("\nEntrada int rango limite: ", 1, 5000, 2, 3))

    #str

    print("\n",entrada_str_simple("\nEntrada str simple: "))

    print("\n",entrada_str_limite("\nEntrada str limite: ", 1, 6))

    print("\n",entrada_str_no_numbers("\nEntrada str no numbers: "))

    print("\n",entrada_str_limite_no_numbers("\nEntrada str limite no numbers: ", 1, 6))