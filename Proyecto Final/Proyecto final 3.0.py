import json
import funciones

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


# FUNCIONES EXTRAS

# Valida que el carnet ingresado no este dentro de la base de datos
def duplicate_id ():
    carnet = funciones.entrada_int_rango("\nIngrese el carnet del alumno: ", 1, 99999)
    for i in range (len(data_base["carnets"])):
        while data_base["carnets"][i] == carnet:    
            carnet = funciones.entrada_int_rango("\nCarnet duplicado, ingrese el carnet del alumno: ", 1, 99999)
    return carnet

# Consulta que opcion desea seleccionar (si o no)
def new_search (question,option):
    print ("\n" + str(question))
    print ("\n1. Si")
    print ("2. No")
    again = funciones.entrada_int_rango("\nIngrese el número de la opción que desea seleccionar: ", 1, 2)
    if again == 1:
        n = option
    else:
        n = 0 
    return n

# Busca un carnet dentro de la base de datos, si lo encuentra retorna un True y el indice si no devuelve un False
def search_id ():
    carnet = funciones.entrada_int_rango("\nIngrese el carnet del alumno: ", 1, 99999)
    for i in range (len(data_base["carnets"])):
        if data_base["carnets"][i] == carnet:
            encontrado = True
            break
        else:
            encontrado = False
    
    return encontrado, i

# Añadir una nueva nota
def add_score (mensaje):
    score = funciones.entrada_int_rango(mensaje, 0, 10)
    return score

# Calcula el promedio de notas de un alumno en base al indice del carnet
def average (index):
    data_base["notas_promedios"][index] = (data_base["notas_examen_final"][index]*(EXAMENFINAL/100) + data_base["notas_actividad_1"][index]*(ACTIVIDAD1/100) + data_base["notas_actividad_2"][index]*(ACTIVIDAD2/100) + data_base["notas_tarea_1"][index]*(TAREA1/100) + data_base["notas_tarea_2"][index]*(TAREA2/100))  
    return data_base["notas_promedios"][index]    


readBD ()

# MAIN MENU

while n != 8:
    funciones.print_main_menu()
    n = funciones.entrada_int_rango("\nIngrese el número de la opción que desea seleccionar: ", 1, 8)

    while n == 1:
        print ("\n\n1. AGREGAR ALUMNO")
        
        data_base["nombres"].append(funciones.entrada_str_no_numbers_nc("\nIngrese el nombre del alumno: "))
        data_base["carnets"].append(duplicate_id())
        data_base["grados"].append(funciones.entrada_int_simple("\nIngrese el grado del alumno: "))
        data_base["notas_examen_final"].append(0)
        data_base["notas_actividad_1"].append(0)
        data_base["notas_actividad_2"].append(0)
        data_base["notas_tarea_1"].append(0)
        data_base["notas_tarea_2"].append(0)
        data_base["notas_promedios"].append(0)

        writeBD()

        n = new_search("\nEstudiante archivado, desea realizar otro registro?", 1)

    while n == 2:

        print ("\n\n2. AGREGAR NOTAS DE ALUMNO")

        encontrado, indice = search_id()
        
        if encontrado == True:
            
            data_base["notas_tarea_1"][indice] = add_score("\nIngrese la nota de la tarea #1: ")

            data_base["notas_tarea_2"][indice] = add_score("\n\nIngrese la nota de la tarea #2: ")
            
            data_base["notas_actividad_1"][indice] = add_score("\n\nIngrese la nota de la actividad #1: ")

            data_base["notas_actividad_2"][indice] = add_score("\n\nIngrese la nota de la actividad #2: ")

            data_base["notas_examen_final"][indice] = add_score("\n\nIngrese la nota del examen final: ")

            data_base["notas_promedios"][indice] = average(indice)
        
            writeBD()

            n = new_search("\nNotas guardadas, desea realizar otro registro?", 2)
        
        else:

            n = new_search("\nEl carnet no existe, desea realizar otra busqueda?", 2)

    while n == 3:
        
        print ("\n\n3. MODIFICAR NOTAS DE ALUMNO")

        encontrado, indice = search_id()

        if encontrado == True:
            
            while True:
                funciones.print_menu_2()
                
                f = funciones.entrada_int_rango("\nIngrese el número de la opción que desea seleccionar: ", 1, 6) 
                
                if f == 1:
                    data_base["notas_tarea_1"][indice] = add_score("\nIngrese la nota de la tarea #1: ")
                    
                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()

                elif f == 2:
                    data_base["notas_tarea_2"][indice] = add_score("\nIngrese la nota de la tarea #2: ")

                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()
                
                elif f == 3:
                    data_base["notas_actividad_1"][indice] = add_score("\nIngrese la nota de la actividad #1: ")

                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()
                
                elif f == 4:
                    data_base["notas_actividad_2"][indice] = add_score("\nIngrese la nota de la actividad #2: ")

                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()
                
                elif f == 5:
                    data_base["notas_examen_final"][indice] = add_score("\nIngrese la nota del examen final: ")

                    data_base["notas_promedios"][indice] = average(indice)
                    writeBD()
                
                elif f == 6:
                    break
                
                writeBD()

            n = new_search("\nNotas guardadas, desea realizar modificar las notas de otro alumno?", 3)
        
        else:
            
            n = new_search("\nEl carnet no existe, desea realizar otra busqueda?", 3) 

    while n == 4:
        print ("\n\n4. ELIMINAR ALUMNO")
        
        encontrado, indice = search_id()

        if encontrado == True:
            
            f = new_search("\nSeguro que desea eliminar al estudiante con el carnet 0" + str(data_base["carnets"][indice]) + " ?", 2)
                
            if f == 0:
                n = new_search("\nDesea eliminar otro alumno?", 4)
                   
            else:

                print("\nEl estudiante con el carnet 0" + str(data_base["carnets"][indice]) + " ha sido eliminado")  
            
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
                
                n = new_search("\nDesea eliminar otro alumno?", 4)
                
        else:
            n = new_search("\nEl carnet no existe, desea realizar otra busqueda?", 4)

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