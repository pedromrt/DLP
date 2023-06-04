import re

def no_spaces (entrada):
    while True:
        check = str(entrada).replace(" ", "")       
        if len(check) == 0:
            entrada = input("No se permiten entradas vacias, intente de nuevo: ")
            continue
        else:
            verdadero = True
            return entrada,verdadero

def value_int_input (entrada):
    verdadero = False
    while True:
        try:
            entrada = int(entrada)
            verdadero = True
            return entrada,verdadero
        except ValueError:
            entrada, _ = no_spaces(input("Tipo de entrada no valida, intente de nuevo: "))

def value_float_input(entrada):
    verdadero = False
    while True:
        try:
            entrada = float(entrada)
            verdadero = True
            return entrada,verdadero
        except ValueError:
            entrada, _ = no_spaces(input("Tipo de entrada no valida, intente de nuevo: "))

def range_options(entrada, lower, bigger):
    while True:
        if entrada < lower or entrada > bigger:
            entrada, _ = value_int_input(no_spaces(input("Entrada fuera del rango de opciones, intente de nuevo: ")))
            continue
        else:
            verdadero = True
            return entrada,verdadero

def input_limitado(entrada,limite):
    while True:
        entrada = str(entrada)
        if len(entrada) > limite:
            entrada, _ = no_spaces(input(f"La entrada debe tener máximo {limite} caracteres, intente de nuevo: "))
        else:
            verdadero = True
            return entrada,verdadero

def no_numbers_in_str (entrada):
    while True:
        entrada = str(entrada)
        if entrada.isdigit():
            entrada = no_spaces(input("El ingreso de numeros no esta permitido en esta entrada, intente de nuevo: "))
            continue
        else:
            verdadero = True
            return entrada,verdadero

def no_special_character (entrada, caracteres_permitidos = None):
    while True:
        entrada = str(entrada)
        patron = r'^[a-zA-Z0-9{}]+$'.format(re.escape(caracteres_permitidos))        
        if re.match(patron, entrada):
            verdadero = True
            return entrada,verdadero
        else:
            entrada, _ = no_spaces(input("Entrada no valida, intete de nuevo: "))


# Tpos de entrada

# Entrada int simple

def entrada_int_simple(mensaje):
    entrada = input(mensaje)
    while True:
        entrada, check1 = no_spaces(entrada)
        entrada, check2 = value_int_input(entrada)

        if check1 and check2:
            return entrada

# while True:
#     valido = entrada_int_simple("Entrada 1: ")
#     print ("Entrada valida................ ", valido)



# Entrada int con rango de opciones

def entrada_int_rango(mensaje,lower,bigger):
    entrada = input(mensaje)
    while True:
        entrada, check1 = no_spaces(entrada)
        entrada, check2 = value_int_input(entrada)
        entrada, check3 = range_options(entrada, lower, bigger)

        if check1 and check2 and check3:
            return entrada

# while True:
#     valido = entrada_int_rango("Entrada 1: ",1,5)
#     print ("Entrada valida................ ", valido)



# Entrada int con limite de caracteres

def entrada_int_limite(mensaje,limite):
    entrada = input(mensaje)
    while True:
        entrada, check1 = no_spaces(entrada)

        entrada, check2 = value_int_input(entrada)
        entrada, check3 = input_limitado(entrada, limite)

        if check1 and check2 and check3:
            return entrada

while True:
    valido = entrada_int_limite("Entrada 1: ",5)
    print ("Entrada valida................ ", valido)














# # Entrada simple str

# variable = no_special_character(no_spaces(input("Range mensaje: ")),"")

# print(type(variable))



# # Entrada str con limite de caracteres
    
# variable = str(input_limitado(no_special_character(no_spaces(input("Range mensaje: ")),""),5))

# print(type(variable))



# # Entrada str no permite entrada de numeros

# variable = no_special_character(no_numbers_in_str(no_special_character(no_spaces(input("Limite mensaje: ")),"")),"")

# print(type(variable))



# # Entrada str con limite de caracteres, no permite entrada de numeros 

# variable = no_numbers_in_str(str(input_limitado(str(no_special_character(no_spaces(input("Limite mensaje: ")),"")),5)))

# print(type(variable))