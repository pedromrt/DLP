import re
import json
route_DB = "Proyecto Final/BaseDatos.txt"



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

# Valida que la entrada sea de tipo float:
def value_float_input(entrada):
    try:
        entrada = float(entrada)
        return entrada, True
    except ValueError:
        return entrada, False

# Valida que la entrada se encuentre dentro de un rango de numeros donde lower es el mas bajo y bigger el mas alto permitido
def range_options(entrada, lower, bigger):
    if entrada < lower or entrada > bigger:
        return entrada, False
    else:
        return entrada, True

# Valida que la entrada contenga un minimo o un maximo de caracteres donde limite_bot es el minimo y limite_top es el maximo
def input_limitado(entrada, limite_top, limite_bot):
    entrada = str(entrada)
    if len(entrada) > limite_top or len(entrada) < limite_bot:
        return entrada, False
    else:
        return entrada, True

# Valida que la entrada no contenga numeros
def no_numbers_in_str(entrada):
    entrada = str(entrada)
    if entrada.isdigit():
        return entrada, False
    else:
        return entrada, True

# Valida que la entrada no contenga caracteres especiales
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

# Verifica unicamente que la entrada no contenga solo espacios y que sea de tipo entero
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

# Verifica que la entrada no contenga solo espacios, que sea de tipo entero y que este dentro de un rango de numeros
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

# Verifica que la entrada no contenga solo espacios, que sea de tipo entero y que tenga un minimo y maximo de caracteres
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

# Verifica que la entrada no contenga solo espacios, que sea de tipo entero, que este dentro de un rango de numeros y que tenga un minimo y maximo de caracteres
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

# Verifica unicamente que la entrada no contenga solo espacios y que sea de tipo float
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

# Verifica que la entrada no contenga solo espacios, que sea de tipo float y que este dentro de un rango de numeros
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

# Verifica que la entrada no contenga solo espacios, que sea de tipo float y que tenga un minimo y maximo de caracteres
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

# Verifica que la entrada no contenga solo espacios, que sea de tipo float, que este dentro de un rango de numeros y que tenga un minimo y maximo de caracteres
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



# Entradas str con validacion no_special_character

# Verifica que la entrada no contenga solo espacios y que no contenga caracteres especiales
def entrada_str_simple_nc(mensaje):
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

# Verifica que la entrada no contenga solo espacios, que no contenga caracteres especiales y que tenga un minimo y un maximo de caracters
def entrada_str_limite_nc(mensaje,limite_bot,limite_top):
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

# Verifica que la entrada no contenga solo espacios, que no contenga caracteres especiales y que no contenga numeros
def entrada_str_no_numbers_nc(mensaje):
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

# Verifica que la entrada no contenga solo espacios, que no contenga caracteres especiales, que tenga un minimo y un maximo de caracters y que no contenga numeros
def entrada_str_limite_no_numbers_nc(mensaje,limite_bot,limite_top):
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



# Entradas str sin validacion no_special_character

# Verifica que la entrada no contenga solo espacios
def entrada_str_simple_(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        return entrada

# Verifica que la entrada no contenga solo espacios y que tenga un minimo y un maximo de caracters
def entrada_str_limite(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue

        entrada, check2 = input_limitado(entrada,limite_top, limite_bot)
        if check2 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        return entrada    

# Verifica que la entrada no contenga solo espacios y que no contenga numeros    
def entrada_str_no_numbers(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_numbers_in_str(entrada)
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        return entrada 

# Verifica que la entrada no contenga solo espacios, que tenga un minimo y un maximo de caracters y que no contenga numeros
def entrada_str_limite_no_numbers(mensaje,limite_bot,limite_top):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        entrada, check2 = input_limitado(entrada, limite_top, limite_bot)
        if check2 == False:
            print("\nLa entrada debe tener un minimo de",limite_bot,"caracteres y un máximo de",limite_top,"caracteres, intente de nuevo")
            continue

        entrada, check3 = no_numbers_in_str(entrada)
        if check3 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        return entrada 



# FUNCIONES DE GUARDADO

# Lee el archivo base de datos y si este contiene informacion la guarda en data_base
def readBD ():
    global data_base
    with open(route_DB, "r") as archivo:
        if archivo.readline().strip():
            with open(route_DB,"r") as archivo:
                data_base = json.load(archivo)

# Borra todos los datos del archivo base de datos y lo sobreescribe con los nuevos datos modificados
def writeBD():
    global data_base
    with open(route_DB, "w") as archivo:
        json.dump(data_base, archivo)



# PRINT MENUS

# Imprime el menu principal
def print_main_menu():
    print ('\n\nCENTRO ESCOLAR "LOS MEJORES"')
    print ("\n1. Agregar alumno")
    print ("2. Agregar notas de alumno")
    print ("3. Modificar notas de alumno")
    print ("4. Eliminar alumno")
    print ("5. Mostrar lista de aprobados")
    print ("6. Mostrar lista de reprobados")
    print ("7. Mostrar toda la lista de alumnos")
    print ("8. Salir del programa")

# Imprime el menu de la opcion 3
def print_menu_2 ():
    print ("\n\nSeleccione la nota que desea modificar: ")
    print ("\n1. Tarea 1")
    print ("2. Tarea 2")
    print ("3. Actividad 1")
    print ("4. Actividad 2")
    print ("5. Examen Final")
    print ("6. Volver al menu principal")

# Imprime un menu con opciones de si o no donde question es la pregunta que desea realizar
def print_yes_no(question):
    print ("\n" + str(question))
    print ("\n1. Si")
    print ("2. No")



# FUNCIONES EXTRAS

# Por arreglar ----------------------------------------------------------------

def duplicate_id ():
    carnet = value_int_input("\nIngrese el carnet del alumno: ", "\nTipo de entrada no válida. Ingrese un número de carnet valido: ")

    for i in range (len(data_base["carnets"])):
        while data_base["carnets"][i] == carnet:    
            carnet = value_int_input("\nCarnet duplicado, ingrese el carnet del alumno: ", "\nTipo de entrada no válida. Ingrese un número de carnet valido: ")
    return carnet

def new_search (menu,option):
    again = value_int_input("\nIngrese el número de la opción que desea seleccionar: ", "\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: ")
    again = range_options(again, 1, 2,"\nOpcion no valida, Ingrese el número de la opción que desea seleccionar: ", "\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: ")
    if again == 1:
        n = option
    else:
        n = 0 
    return n

def search_id ():
    
    carnet = value_int_input("\nIngrese el número de carnet del alumno: ", "\nTipo de entrada no válida. Ingrese un número de carnet valido: ")
    for i in range (len(data_base["carnets"])):
        if data_base["carnets"][i] == carnet:
            encontrado = True
            break
        else:
            encontrado = False
    
    return encontrado, i

def add_score (msj1, msj2, msj3):
    score = value_float_input(msj1, msj2)
    score = range_options(score, 0, 10, msj3, msj2)
    return score

def average (index):
    data_base["notas_promedios"][index] = (data_base["notas_examen_final"][index]*(EXAMENFINAL/100) + data_base["notas_actividad_1"][index]*(ACTIVIDAD1/100) + data_base["notas_actividad_2"][index]*(ACTIVIDAD2/100) + data_base["notas_tarea_1"][index]*(TAREA1/100) + data_base["notas_tarea_2"][index]*(TAREA2/100))
    
    return data_base["notas_promedios"][index]