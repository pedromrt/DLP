# FUNCIONES
import re

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

# Valida que la entrada se encuentre dentro de un rango de numeros donde lower es el mas bajo y bigger el mas alto permitido
def range_options(entrada, lower, bigger):
    if entrada < lower or entrada > bigger:
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

# Verifica que la entrada no contenga solo espacios, que no contenga caracteres especiales y que no contenga numeros
def entrada_str_no_numbers_nc(mensaje):
    while True:
        entrada = input(mensaje)
        
        entrada, check1 = no_spaces(entrada)
        if check1 == False:
            print("\nNo se permiten entradas vacias, intente de nuevo")
            continue
        
        entrada, check2 = no_special_character(entrada," ")
        if check2 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        entrada, check3 = no_numbers_in_str(entrada)
        if check3 == False:
            print("\nTipo de entrada no valida, intente de nuevo")
            continue

        return entrada 


# Listas

nombre = []

sexo = []

edad = []

# Contadores y acomuladores

kid_count = 0
women_count = 0
men_count = 0
women_acom = 0
men_acom = 0

#MAIN MENU
while True:

    print ("\n----- HOSPITAL ROSALES -----")
    print ("\n===== Añadir paciente ===== ")

    nombre.append(entrada_str_no_numbers_nc("\nIngrese el nombre del paciente: "))
    
    print("\nSeleccione el genero del paciente: ")
    print("\n1.Femenino")
    print("2.Masculino")
    sexo.append(entrada_int_rango("\nIngrese la opcion que desea seleccionar: ",1,2))
    
    edad.append(entrada_int_simple("\nIngrese la edad del paciente: "))

    print("\n\nDesea agregar otro paciente: ")
    print("\n1.Si")
    print("2.No")
    again = entrada_int_rango("\nIngrese la opcion que desea seleccionar: ",1,2)

    if again == 2:
        break
    else:
        continue

print("\n\nDespues de realizar todos los registros, los datos quedaron organizados de la siguiente manera: ")

# Cuantos pacientes son niños (Niño >=6 or <=12)
for i in range (len(edad)):
    if edad[i] >= 6 and edad[i] <= 12:
        kid_count += 1

if kid_count > 0:
    print("\n- Se registraron un total de " + str(kid_count) + " niños y niñas de entre 6 a 12 años")
else: 
    print("\n-No se registro ningun niño o niña")


# Cuantas mujeres hay excluyendo niñas
for i in range (len(edad)):
    if edad[i] > 12 and sexo[i] == 1:
        women_count += 1


# Cuantos hombres hay excluyendo niños
for i in range (len(edad)):
    if edad[i] > 12 and sexo[i] == 2:
        men_count += 1


# Calcular la edad promedio de las mujeres
if women_count > 0:
    print("- Se registraron un total de " + str(women_count) + " mujeres")
    for i in range (len(edad)):
        if edad[i] > 12 and sexo[i] == 1:
            women_acom += edad[i]

    average_women = women_acom / women_count

    print("- La edad promedio de las mujeres registradas fue de " + str(average_women))
else:
    print("- No se registro ninguna mujer")


# Calcular la edad promedio de los hombres
if men_count > 0:
    print("- Se registraron un total de " + str(men_count) + " hombres")
    for i in range (len(edad)):
        if edad[i] > 12 and sexo[i] == 2:
            men_acom += edad[i]

    average_men = men_acom / men_count

    print("- La edad promedio de los hombres registrados fue de " + str(average_men))
else:
    print("- No se registro ningun hombre")

# Calcular promedio general de edad entre hombres y mujeres
if men_count > 0 or women_count > 0:
    total_average = (men_acom + women_acom) / (men_count + women_count)

    print("- Por ultimo la edad promedio general de los hombres y mujeres registrados fue de " + str(total_average))
else:
    print("- No se registro ningun hombre ni ninguna una mujer")

print()