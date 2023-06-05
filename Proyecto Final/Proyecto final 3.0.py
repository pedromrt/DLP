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
    carnet = entrada_int_rango("\nIngrese el carnet del alumno: ", 1, 99999)
    for i in range (len(data_base["carnets"])):
        while data_base["carnets"][i] == carnet:    
            carnet = entrada_int_rango("\nCarnet duplicado, ingrese el carnet del alumno: ", 1, 99999)
    return carnet

# Consulta que opcion desea seleccionar (si o no)
def new_search (question,option):
    print ("\n" + str(question))
    print ("\n1. Si")
    print ("2. No")
    again = entrada_int_rango("\nIngrese el número de la opción que desea seleccionar: ", 1, 2)
    if again == 1:
        n = option
    else:
        n = 0 
    return n

# Busca un carnet dentro de la base de datos, si lo encuentra retorna un True y el indice si no devuelve un False
def search_id ():
    carnet = entrada_int_rango("\nIngrese el carnet del alumno: ", 1, 99999)
    for i in range (len(data_base["carnets"])):
        if data_base["carnets"][i] == carnet:
            encontrado = True
            break
        else:
            encontrado = False
    
    return encontrado, i

# Añadir una nueva nota
def add_score (mensaje):
    score = entrada_int_rango(mensaje, 0, 10)
    return score

# Calcula el promedio de notas de un alumno en base al indice del carnet
def average (index):
    data_base["notas_promedios"][index] = (data_base["notas_examen_final"][index]*(EXAMENFINAL/100) + data_base["notas_actividad_1"][index]*(ACTIVIDAD1/100) + data_base["notas_actividad_2"][index]*(ACTIVIDAD2/100) + data_base["notas_tarea_1"][index]*(TAREA1/100) + data_base["notas_tarea_2"][index]*(TAREA2/100))  
    return data_base["notas_promedios"][index]    


readBD ()

# MAIN MENU



print("\nGuardando datos...")

writeBD()

print ("\nPrograma Finalizado...\n")