import json
import Funciones

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

# POR ARREGLAR -----------------------------------------

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