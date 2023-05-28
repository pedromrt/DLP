
#nota: agregar exception value error a cada input

import json

baseDatos = {
    
    "nombre" : [0],
    "carnet" : [0],
    "grado" : [0],
    "ExamenFinal" : [0],
    "actividad1" : [0],
    "actividad2" : [0],
    "tarea1" : [0],
    "tarea2" : [0],
    "promedio" : [0]

# primero abre el archivo Base de datos
# despues verifica con un if si la primera linea esta vacia  o no
# si no esta vacia lee los datos del archivo y los sustituye con los anteriormente guardados
# si esta vacia salta este paso y solo ejecuta el diccionario como se muestra en el codigo


}
with open("Proyecto Final/BaseDatos.txt", "r") as archivo:
    if archivo.readline().strip():
        with open("Proyecto Final/BaseDatos.txt","r") as archivo:
            baseDatos = json.load(archivo)


EXAMENFINAL = 40
ACTIVIDAD1 = 20
ACTIVIDAD2 = 20
TAREA1 = 10
TAREA2 = 10


n =  0

#MAIN MENU

while n != 8:
    
    print ('\n\nCENTRO ESCOLAR "LOS MEJORES"')
    print ("\n1. Agregar alumno")
    print ("2. Agregar notas de alumno")
    print ("3. Modificar notas de alumno")
    print ("4. Eliminar alumno")
    print ("5. Mostrar lista de aprobados")
    print ("6. Mostrar lista de reprobados")
    print ("7. Mostrar toda la lista de alumnos")
    print ("8. Salir del programa")

    n = int(input("\nIngrese el número de la opción que desea seleccionar: "))
    
    while n != 1 and n != 2 and n != 3 and n != 4 and n != 5 and n != 6 and n != 7 and n != 8:
        
        print ('\n\nCENTRO ESCOLAR "LOS MEJORES"')
        print ("\n1. Agregar alumno")
        print ("2. Agregar notas de alumno")
        print ("3. Modificar notas de alumno")
        print ("4. Eliminar alumno")
        print ("5. Mostrar lista de aprobados")
        print ("6. Mostrar lista de reprobados")
        print ("7. Mostrar toda la lista de alumnos")
        print ("8. Salir del programa")
        
        n = int(input("\nOpcion no valida, Ingrese el número de la opción que desea seleccionar: "))

    #OPCION 1 AGREGAR ALUMNO

    if n == 1:
        
        print ("\n\n\nAGREGAR ALUMNO")
        baseDatos["nombre"].append(input("\nIngrese el nombre del alumno: "))
        carnet = input("\nIngrese el carnet del alumno: ")
        for i in range (len(baseDatos["carnet"])):
            while baseDatos["carnet"][i] == carnet:
                carnet = input("\nCarnet duplicado, ingrese el carnet del alumno: ")
                i = 0
        baseDatos["carnet"].append(carnet)
        baseDatos["grado"].append(input("\nIngrese el grado del alumno: "))
        baseDatos["ExamenFinal"].append(0)
        baseDatos["actividad1"].append(0)
        baseDatos["actividad2"].append(0)
        baseDatos["tarea1"].append(0)
        baseDatos["tarea2"].append(0)
        baseDatos["promedio"].append(0) 

    #OPCION 2 AGREGAR NOTAS DE ALUMNO

    while n == 2:
        print ("\n\n\nAGREGAR NOTAS DE ALUMNO")
        carnet = input("\nIngrese el número de carnet del alumno: ")
        
        for i in range (len(baseDatos["carnet"])):
            if baseDatos["carnet"][i] == carnet:
                encontrado = True
                break
            else:
                encontrado = False

        if encontrado == True:        
            
            tarea1 = float(input("\n\nIngrese la nota de la tarea #1: "))
            while tarea1 < 0 or tarea1 > 10:
                tarea1 = float(input("\nNota no valida, ingrese la nota de la tarea #1: "))
            baseDatos["tarea1"][i] = tarea1
            
            tarea2 = float(input("\n\nIngrese la nota de la tarea #2: "))
            while tarea2 < 0 or tarea2 > 10:
                actividad2 = float(input("\nNota no valida, ingrese la nota de la tarea #2: "))
            baseDatos["tarea2"][i] = tarea2

            actividad1 = float(input("\n\nIngrese la nota de la actividad 1: "))
            while actividad1 < 0 or actividad1 > 10:
                actividad1 = float(input("\nNota no valida, ingrese la nota de la actividad 1: "))
            baseDatos["actividad1"][i] = actividad1

            actividad2 = float(input("\n\nIngrese la nota de la actividad 2: "))
            while actividad2 < 0 or actividad2 > 10:
                actividad2 = float(input("\nNota no valida, ingrese la nota de la actividad 2: "))
            baseDatos["actividad2"][i] = actividad2

            ExamenFinal = float(input("\n\nIngrese la nota del examen final: "))
            while ExamenFinal < 0 or ExamenFinal > 10:
                ExamenFinal = float(input("\nNota no valida, ingrese la nota del examen final: "))
            baseDatos["ExamenFinal"][i] = ExamenFinal
            
            
            baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))

            n = 0
        
        else:
            
            print ("\n\n\nCarnet no encontrado, desea realizar otra busqueda?")
            print ("\n1. Si")
            print ("2. No")
            again = int(input("\nIngrese el número de la opción que desea seleccionar: "))
            while again != 1 and again != 2:
                print ("\n\n\nDesea realizar otra busqueda?")
                print ("\n1. Si")
                print ("2. No")
                again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))
            
            if again == 1:
                n = 2
            else:
                n = 0

    #OPCION 3 MODIFICAR NOTAS DE ALUMNO

    while n == 3:

        print ("\n\n\nMODIFICAR NOTAS DE ALUMNO")
        carnet = input("\nIngrese el número de carnet del alumno: ")
        
        for i in range (len(baseDatos["carnet"])):
            if baseDatos["carnet"][i] == carnet:
                encontrado = True
                break
            else:
                encontrado = False

        if encontrado == True:        
            x = 1
            while x == 1:
                
                #agregar un seleccionador para ingresar que nota desea cambiar
                f = True
                while f == True:
    
                    print ('\n\nSeleccione la nota que desea modificar:"')
                    print ("\n1. Tarea 1")
                    print ("2. Tarea 2")
                    print ("3. Actividad 1")
                    print ("4. Actividad 2")
                    print ("5. Examen Final")
                    print ("6. Volver al menu principal")

                    f = int(input("\nIngrese el número de la opción que desea seleccionar: "))
                    
                    while f != 1 and f != 2 and f != 3 and f != 4 and f != 5 and f != 6:
                        
                        print ('\n\nSeleccione la nota que desea modificar:"')
                        print ("\n1. Tarea 1")
                        print ("2. Tarea 2")
                        print ("3. Actividad 1")
                        print ("4. Actividad 2")
                        print ("5. Examen Final")
                        print ("6. Volver al menu principal")
                        
                        f = int(input("\nOpcion no valida, Ingrese el número de la opción que desea seleccionar: "))
                
                    if f == 1:
                    
                        tarea1 = float(input("\n\nIngrese la modificacion de la nota de la tarea #1: "))
                        while tarea1 < 0 or tarea1 > 10:
                            tarea1 = float(input("\nNota no valida, ingrese la modificacion de la nota de la tarea #1: "))
                        baseDatos["tarea1"][i] = tarea1

                        
                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                    
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                        again = int(input("\nIngrese el número de la opción que desea seleccionar: "))
                        while again != 1 and again != 2:
                            print ("\n\n\nDesea realizar otra modificacion?")
                            print ("\n1. Si")
                            print ("2. No")
                            again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))
                        
                        if again == 1:
                            x = 1
                        else:
                            x = 2
                            n = 0
                            break
                   
                    elif f == 2:

                        tarea2 = float(input("\n\nIngrese la modificacion de la nota de la tarea #2: "))
                        while tarea2 < 0 or tarea2 > 10:
                            actividad2 = float(input("\nNota no valida, ingrese la modificacion de la nota de la tarea #2: "))
                        baseDatos["tarea2"][i] = tarea2

                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                    
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                        again = int(input("\nIngrese el número de la opción que desea seleccionar: "))
                        while again != 1 and again != 2:
                            print ("\n\n\nDesea realizar otra modificacion?")
                            print ("\n1. Si")
                            print ("2. No")
                            again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))
                        
                        if again == 1:
                            x = 1
                        else:
                            x = 2
                            n = 0
                            break
                        
                    elif f == 3:

                        actividad1 = float(input("\n\nIngrese la modificacion de la nota de la actividad 1: "))
                        while actividad1 < 0 or actividad1 > 10:
                            actividad1 = float(input("\nNota no valida, ingrese la modificacion de la nota de la actividad 1: "))
                        baseDatos["actividad1"][i] = actividad1

                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                    
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                        again = int(input("\nIngrese el número de la opción que desea seleccionar: "))
                        while again != 1 and again != 2:
                            print ("\n\n\nDesea realizar otra modificacion?")
                            print ("\n1. Si")
                            print ("2. No")
                            again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))
                        
                        if again == 1:
                            x = 1
                        else:
                            x = 2
                            n = 0
                            break
                        
                    elif f == 4:
                        
                        actividad2 = float(input("\n\nIngrese la modificacion de la nota de la actividad 2: "))
                        while actividad2 < 0 or actividad2 > 10:
                            actividad2 = float(input("\nNota no valida, ingrese la modificacion de la nota de la actividad 2: "))
                        baseDatos["actividad2"][i] = actividad2

                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                    
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                        again = int(input("\nIngrese el número de la opción que desea seleccionar: "))
                        while again != 1 and again != 2:
                            print ("\n\n\nDesea realizar otra modificacion?")
                            print ("\n1. Si")
                            print ("2. No")
                            again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))
                        
                        if again == 1:
                            x = 1
                        else:
                            x = 2
                            n = 0
                            break
                   
                    elif f == 5:

                        ExamenFinal = float(input("\n\nIngrese la modificacion de la nota del examen final: "))
                        while ExamenFinal < 0 or ExamenFinal > 10:
                            ExamenFinal = float(input("\nNota no valida, ingrese la modificacion de la nota del examen final: "))
                        baseDatos["ExamenFinal"][i] = ExamenFinal
                        
                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                    
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                        again = int(input("\nIngrese el número de la opción que desea seleccionar: "))
                        while again != 1 and again != 2:
                            print ("\n\n\nDesea realizar otra modificacion?")
                            print ("\n1. Si")
                            print ("2. No")
                            again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))
                        
                        if again == 1:
                            x = 1
                        else:
                            x = 2
                            n = 0
                            break

                    elif f == 6: 
                        
                        f = False
                        n = 0
                        x = 2

        
        else:
            
            print ("\n\n\nCarnet no encontrado, desea realizar otra busqueda?")
            print ("\n1. Si")
            print ("2. No")
            again = int(input("\nIngrese el número de la opción que desea seleccionar: "))
            while again != 1 and again != 2:
                print ("\n\n\nDesea realizar otra busqueda?")
                print ("\n1. Si")
                print ("2. No")
                again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))
            
            if again == 1:
                n = 2
            else:
                n = 0

    #OPCION 4 ELIMINAR ALUMNO

    while n == 4:
        
        print ("\n\n\nELIMINAR ALUMNO")
        carnet = input("\nIngrese el número de carnet del alumno: ")
        
        for i in range (len(baseDatos["carnet"])):
            if baseDatos["carnet"][i] == carnet:
                encontrado = True
                indice = i
                break
            else:
                encontrado = False

        if encontrado == True:        
            baseDatos["nombre"].pop(indice)
            baseDatos["carnet"].pop(indice)
            baseDatos["grado"].pop(indice)
            baseDatos["ExamenFinal"].pop(indice)
            baseDatos["actividad1"].pop(indice)
            baseDatos["actividad2"].pop(indice)
            baseDatos["tarea1"].pop(indice)
            baseDatos["tarea2"].pop(indice)
            baseDatos["promedio"].pop(indice)
            
            n = 0
        
        else:
            
            print ("\n\n\nCarnet no encontrado, desea realizar otra busqueda?")
            print ("\n1. Si")
            print ("2. No")
            again = int(input("\nIngrese el número de la opción que desea seleccionar: "))
            while again != 1 and again != 2:
                print ("\n\n\nDesea realizar otra busqueda?")
                print ("\n1. Si")
                print ("2. No")
                again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))
            
            if again == 1:
                n = 4
            else:
                n = 0

    #OPCION 5 MOSTRA LISTA DE APROVADOS

    if n == 5:

        print ("\n\n\nLISTA DE APROBADOS\n")

        for i in range (len(baseDatos["promedio"])):
            if baseDatos["promedio"][i] >= 7:
                print(baseDatos["nombre"][i], round(baseDatos["promedio"][i],2))
                
    #OPCION 6 MOSTRA LISTA DE REPROVADOS

    if n == 6:

        print ("\n\n\nLISTA DE APROBADOS\n")

        for i in range (len(baseDatos["promedio"])):
            if baseDatos["nombre"][i] == 0:
                continue
            if baseDatos["promedio"][i] < 7:
                print(baseDatos["nombre"][i], round(baseDatos["promedio"][i],2))

    #OPCION 7 MOSTRAR LISTA COMPLETA DE ESTUDIANTES

    if n == 7:

        print ("\n\n\nLISTA DE NOTAS\n")
        for i in range (len(baseDatos["promedio"])):
            if baseDatos["nombre"][i] == 0:
                continue
            if baseDatos["promedio"][i] >= 7:
                estado = "Aprovado"
            else:
                estado = "Reprobado"
            print(baseDatos["nombre"][i], round(baseDatos["promedio"][i],2),estado)

print("\nGuardando datos...")

# este codigo guarda en el archivo base de datos el diccionario donde se almacenan los registros para poder leerlo al volver a ejecutar el codigo

with open("Proyecto Final/BaseDatos.txt", "w") as archivo:
    json.dump(baseDatos, archivo)

print ("\nPrograma Finalizado...\n")

#27 de mayo 2023