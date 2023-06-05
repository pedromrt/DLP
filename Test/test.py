import json
from Funciones import *

route_DB = "Proyecto Final/BaseDatos.txt"
n = 0
f = 1
EXAMENFINAL = 40
ACTIVIDAD1 = 20
ACTIVIDAD2 = 20
TAREA1 = 10
TAREA2 = 10

data_base = {    
    "nombres" : [0],
    "carnets" : [0],
    "grados" : [0],
    "notas_examen_final" : [0],
    "notas_actividad_1" : [0],
    "notas_actividad_2" : [0],
    "notas_tarea_1" : [0],
    "notas_tarea_2" : [0],
    "notas_promedios" : [0]
}


def readBD ():
    global data_base
    with open(route_DB, "r") as archivo:
        if archivo.readline().strip():
            with open(route_DB,"r") as archivo:
                data_base = json.load(archivo)

def writeBD():
    global data_base
    with open(route_DB, "w") as archivo:
        json.dump(data_base, archivo)



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

def print_menu_2 ():
    print ("\n\nSeleccione la nota que desea modificar: ")
    print ("\n1. Tarea 1")
    print ("2. Tarea 2")
    print ("3. Actividad 1")
    print ("4. Actividad 2")
    print ("5. Examen Final")
    print ("6. Volver al menu principal")

def print_yes_no(question):
    print ("\n" + str(question))
    print ("\n1. Si")
    print ("2. No")



def value_int_input(msj1, msj2):
    error_message = msj1
    while True:
        try:
            input_value = int(input(error_message))
            return input_value
        except ValueError:
            error_message = msj2

def value_float_input(msj1, msj2):
    error_message = msj1
    while True:
        try:
            input_value = float(input(error_message))
            return input_value
        except ValueError:
            error_message = msj2

def range_options(input_value, lower, bigger, msj1, msj2):
    while input_value < lower or input_value > bigger:
        input_value = value_int_input(msj1,msj2)
    return input_value





def duplicate_id ():
    carnet = value_int_input("\nIngrese el carnet del alumno: ", "\nTipo de entrada no válida. Ingrese un número de carnet valido: ")

    for i in range (len(data_base["carnets"])):
        while data_base["carnets"][i] == carnet:    
            carnet = value_int_input("\nCarnet duplicado, ingrese el carnet del alumno: ", "\nTipo de entrada no válida. Ingrese un número de carnet valido: ")
    return carnet

def new_search (option):
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


print_yes_no("hola")
new_search(1)