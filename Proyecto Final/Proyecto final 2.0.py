import json

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

def print_yes_no(msj1):
    print (msj1)
    print ("\n1. Si")
    print ("2. No")

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

def print_menu_2 ():
    print ("\n\nSeleccione la nota que desea modificar: ")
    print ("\n1. Tarea 1")
    print ("2. Tarea 2")
    print ("3. Actividad 1")
    print ("4. Actividad 2")
    print ("5. Examen Final")
    print ("6. Volver al menu principal")


readBD ()


# Main Menu

while n != 8:
    print_main_menu()
    n = value_int_input("\nIngrese el número de la opción que desea seleccionar: ","\nTipo de entrada no válida, ingrese el número de la opción que desea seleccionar: ")
    n = range_options(n,1,8,"\nOpcion no valida, Ingrese el número de la opción que desea seleccionar: ", "\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: ")

    while n == 1:
        
        print ("\n\n1. AGREGAR ALUMNO")

        data_base["nombres"].append(input("\nIngrese el nombre del alumno: "))
        data_base["carnets"].append(duplicate_id())
        data_base["grados"].append(input("\nIngrese el grado del alumno: "))
        data_base["notas_examen_final"].append(0)
        data_base["notas_actividad_1"].append(0)
        data_base["notas_actividad_2"].append(0)
        data_base["notas_tarea_1"].append(0)
        data_base["notas_tarea_2"].append(0)
        data_base["notas_promedios"].append(0)

        writeBD()

        n = new_search(print_yes_no("\n\nEstudiante archivado, desea realizar otro registro?"), 1)

    while n == 2:

        print ("\n\n2. AGREGAR NOTAS DE ALUMNO")

        encontrado, indice = search_id()
        
        if encontrado == True:
            
            data_base["notas_tarea_1"][indice] = add_score("\n\nIngrese la nota de la tarea #1: ", "\nTipo de entrada no válida. Ingrese la nota de la tarea #1: ", "\nNota no valida, ingrese la nota de la tarea #1: ")
            
            data_base["notas_tarea_2"][indice] = add_score("\n\nIngrese la nota de la tarea #2: ", "\nTipo de entrada no válida. Ingrese la nota de la tarea #2: ", "\nNota no valida, ingrese la nota de la tarea #2: ")
            
            data_base["notas_actividad_1"][indice] = add_score("\n\nIngrese la nota de la actividad #1: ", "\nTipo de entrada no válida. Ingrese la nota de la actividad #1: ", "\nNota no valida, ingrese la nota de la actividad #1: ")

            data_base["notas_actividad_2"][indice] = add_score("\n\nIngrese la nota de la actividad #2: ", "\nTipo de entrada no válida. Ingrese la nota de la actividad #2: ", "\nNota no valida, ingrese la nota de la actividad #2: ")

            data_base["notas_examen_final"][indice] = add_score("\n\nIngrese la nota del examen final: ", "\nTipo de entrada no válida. Ingrese la nota del examen final: ", "\nNota no valida, ingrese la nota del examen final: ")

            data_base["notas_promedios"][indice] = average(indice)
        
            writeBD()

            n = new_search(print_yes_no("\n\nNotas guardadas, desea realizar otro registro?"), 2)
        
        else:
            n = new_search(print_yes_no("\n\nEl carnet no existe, desea realizar otra busqueda?"), 2)

    while n == 3:
        print ("\n\n3. MODIFICAR NOTAS DE ALUMNO")

        encontrado, indice = search_id()

        if encontrado == True:
            while True:
                print_menu_2()
                
                f = value_int_input("\nIngrese el número de la opción que desea seleccionar: ", "\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: ")
                f = range_options(f, 1, 6, "\nOpcion no valida, Ingrese el número de la opción que desea seleccionar: ", "\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: ")
                
                if f == 1:
                    data_base["notas_tarea_1"][indice] = add_score("\n\nIngrese la nota de la tarea #1: ", "\nTipo de entrada no válida. Ingrese la nota de la tarea #1: ", "\nNota no valida, ingrese la nota de la tarea #1: ")
                    
                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()

                elif f == 2:
                    data_base["notas_tarea_2"][indice] = add_score("\n\nIngrese la nota de la tarea #2: ", "\nTipo de entrada no válida. Ingrese la nota de la tarea #2: ", "\nNota no valida, ingrese la nota de la tarea #2: ")

                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()
                
                elif f == 3:
                    data_base["notas_actividad_1"][indice] = add_score("\n\nIngrese la nota de la actividad #1: ", "\nTipo de entrada no válida. Ingrese la nota de la actividad #1: ", "\nNota no valida, ingrese la nota de la actividad #1: ")

                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()
                
                elif f == 4:
                    data_base["notas_actividad_2"][indice] = add_score("\n\nIngrese la nota de la actividad #2: ", "\nTipo de entrada no válida. Ingrese la nota de la actividad #2: ", "\nNota no valida, ingrese la nota de la actividad #2: ")

                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()
                
                elif f == 5:
                    data_base["notas_examen_final"][indice] = add_score("\n\nIngrese la nota del examen final: ", "\nTipo de entrada no válida. Ingrese la nota del examen final: ", "\nNota no valida, ingrese la nota del examen final: ")

                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()
                
                elif f == 6:
                    break
                
                writeBD()

            n = new_search(print_yes_no("\n\nNotas guardadas, desea realizar modificar las notas de otro alumno?"), 3)
        else:
            
            n = new_search(print_yes_no("\n\nEl carnet no existe, desea realizar otra busqueda?"), 3) 

    while n == 4:
        print ("\n\n4. ELIMINAR ALUMNO")
        
        encontrado, indice = search_id()

        if encontrado == True:
            
            print_yes_no("\n\nSeguro que desea eliminar al estudiante con el carnet 0" + str(data_base["carnets"][indice]) + " ?")
            f = value_int_input("\nIngrese el número de la opción que desea seleccionar: ","\nTipo de entrada no válida, ingrese el número de la opción que desea seleccionar: ")
            f = range_options(f, 1, 2, "\nOpcion no valida, Ingrese el número de la opción que desea seleccionar: ", "\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: ")
                
            if f == 2:
                n = new_search(print_yes_no("\n\nDesea eliminar otro alumno?"), 4)
                   
            else:

                print("\n\nEl estudiante con el carnet 0" + str(data_base["carnets"][indice]) + " ha sido eliminado")  
            
                data_base["nombres"].pop(indice)
                data_base["carnets"].pop(indice)
                data_base["grados"].pop(indice)
                data_base["notas_examen_final"].pop(indice)
                data_base["notas_actividad_1"].pop(indice)
                data_base["notas_actividad_2"].pop(indice)
                data_base["notas_tarea_1"].pop(indice)
                data_base["notas_tarea_2"].pop(indice)
                data_base["notas_promedios"].pop(indice)

                writeBD()
                
                n = new_search(print_yes_no("\n\nDesea eliminar otro alumno?"), 4)
                
        else:
            n = new_search(print_yes_no("\n\nEl carnet no existe, desea realizar otra busqueda?"), 4)

    if n == 5:
        print ("\n\nLISTA DE APROBADOS\n")
        
        for i in range (len(data_base["notas_promedios"])):
            if data_base["nombres"][i] == 0:
                continue
            if data_base["notas_promedios"][i] >= 7:
                print(data_base["nombres"][i], round(data_base["notas_promedios"][i],2))

    if n == 6:
        print ("\n\nLISTA DE REPROBADOS\n")
        
        for i in range (len(data_base["notas_promedios"])):
            if data_base["nombres"][i] == 0:
                continue
            if data_base["notas_promedios"][i] < 7:
                print(data_base["nombres"][i], round(data_base["notas_promedios"][i],2))

    if n == 7:
        print ("\n\nLISTA DE NOTAS\n")
        
        for i in range (len(data_base["notas_promedios"])):
            if data_base["nombres"][i] == 0:
                continue
            if data_base["notas_promedios"][i] >= 7:
                estado = "Aprobado"
            else:
                estado = "Reprobado"
            print(data_base["nombres"][i], round(data_base["notas_promedios"][i],2),estado)

print("\nGuardando datos...")

writeBD()

print ("\nPrograma Finalizado...\n")