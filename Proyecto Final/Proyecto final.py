import json

#Este diccionario almacena todos los datos que se registren basados en su tipo de dato y en su indice

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
}

# Este bloque de codigo abre el archivo BaseDatos.txt 
# Luego verifica si el documento esta vacio o contiene informacion
# Si el archivo contiene informacion, este la copia y la guarda dentro del diccionario baseDatos
# Si el archivo esta vacio, este salta este paso y continua con el codigo 

with open("Proyecto Final/BaseDatos.txt", "r") as archivo:
    if archivo.readline().strip():
        with open("Proyecto Final/BaseDatos.txt","r") as archivo:
            baseDatos = json.load(archivo)



# Este bloque de codigo establece el porcentaje al cual equivale cada actividad correspondiente

EXAMENFINAL = 40
ACTIVIDAD1 = 20
ACTIVIDAD2 = 20
TAREA1 = 10
TAREA2 = 10

# Declaramos n para utilizarla en el bucle while del menu principal

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

    #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

    try:
        n = int(input("\nIngrese el número de la opción que desea seleccionar: "))

    except ValueError:
        while True:
            try:
                n = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                break
            except ValueError:
                continue

    #Este bloque de codigo verifica que el numero que ingrese el usuario este dentro del rango de opciones que se muestran en el menu
    #Si el usuario ingresa un numero fuera del rango de opciones, este vuelve a imprimir el menu de opciones y solicita una entrada valida dentro del rango de opciones marcada

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
        
        #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

        try:
            n = int(input("\nOpcion no valida, Ingrese el número de la opción que desea seleccionar: "))

        except ValueError:
            while True:
                try:
                    n = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                    break
                except ValueError:
                    continue

    #OPCION 1 AGREGAR ALUMNO

    if n == 1:
        
        #Este bloque de codigo permite añadir un nuevo elemento a las listas de "nombre", "carnet" y "grado"
        #Ademas crea un valor en cero para las notas y promedio de las actividades a evaluar
        #Esto para que se registre un elemento en cada lista con el mismo indice que los añadidos en las listas anterior mente mencionadas

        print ("\n\n\nAGREGAR ALUMNO")
        baseDatos["nombre"].append(input("\nIngrese el nombre del alumno: "))
        
        #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

        try:
            carnet = int(input("\nIngrese el carnet del alumno: "))

        except ValueError:
            while True:
                try:
                    carnet = int(input("\nTipo de entrada no válida. Ingrese un número de carnet valido: "))
                    break
                except ValueError:
                    continue

        # Este bloque de codigo verifica que el carnet ingresado para el nuevo estudiante no exista dentro de la base de datos
        # Esto para que no se duplique un mismo valor de carnet para 2 estudiantes
        # Este bloque recorre y compara todos los carnets dentro de la base de datos y si encuentra una coincidencia,
        # Vuelve a solicitar al usuario que ingrese otro carnet, repitiendo el proceso de verificacion

        for i in range (len(baseDatos["carnet"])):
            while baseDatos["carnet"][i] == carnet:
        
                #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                try:
                    carnet = int(input("\nCarnet duplicado, ingrese el carnet del alumno: "))

                except ValueError:
                    while True:
                        try:
                            carnet = int(input("\nTipo de entrada no válida. Ingrese un número de carnet valido: "))
                            break
                        except ValueError:
                            continue

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
        
 
        
        # Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

        try:
            carnet = int(input("\nIngrese el número de carnet del alumno: "))
        except ValueError:
            while True:
                try:
                    carnet = int(input("\nTipo de entrada no válida. Ingrese un número de carnet valido: "))
                    break
                except ValueError:
                    continue        
        
        # Este bloque de codigo solicita un la entrada de un numero de carnet, posterior a eso, verifica si el carnet se encuentra en la base de datos
        # Si el carnet se encuentra, este crea la variable encontrado y le asigna el valor True, ademas de esto, guarda el indice donde se encontro el canet, por ultimo rompe el bucle
        # Si no se encuentra, unicamente cambia el valor de la variable encontrado a False
            
        for i in range (len(baseDatos["carnet"])):
            if baseDatos["carnet"][i] == carnet:
                encontrado = True
                break
            else:
                encontrado = False

        # Si el carnet fue encontrado, este solicita la entada de las notas las cuales se guardan en el mismo indice donde fue encontrado el carnet
        # Siempe en sus listas correspondientes


        if encontrado == True: 

            # TAREA 1

            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

            try:
                tarea1 = int(input("\n\nIngrese la nota de la tarea #1: "))
            except ValueError:
                while True:
                    try:
                        tarea1 = int(input("\nTipo de entrada no válida. Ingrese la nota de la tarea #1: "))
                        break
                    except ValueError:
                        continue

            # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
            # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
            
            while tarea1 < 0 or tarea1 > 10:

                # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                try:
                    tarea1 = float(input("\nNota no valida, ingrese la nota de la tarea #1: "))
                except ValueError:
                    while True:
                        try:
                            tarea1 = int(input("\nTipo de entrada no válida. Ingrese la nota de la tarea #1: "))
                            break
                        except ValueError:
                            continue

            baseDatos["tarea1"][i] = tarea1

            # TAREA 2

            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

            try:
                tarea2 = int(input("\n\nIngrese la nota de la tarea #2: "))
            except ValueError:
                while True:
                    try:
                        tarea2 = int(input("\nTipo de entrada no válida. Ingrese la nota de la tarea #2: "))
                        break
                    except ValueError:
                        continue

            # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
            # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
            
            while tarea2 < 0 or tarea2 > 10:

                # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                try:
                    tarea2 = float(input("\nNota no valida, Ingrese la nota de la tarea #2: "))
                except ValueError:
                    while True:
                        try:
                            tarea2 = int(input("\nTipo de entrada no válida. Ingrese la nota de la tarea #2: "))
                            break
                        except ValueError:
                            continue

            baseDatos["tarea2"][i] = tarea2


            # Actividad 1

            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

            try:
                actividad1 = int(input("\n\nIngrese la nota de la actividad #1: "))
            except ValueError:
                while True:
                    try:
                        actividad1 = int(input("\nTipo de entrada no válida. Ingrese la nota de la actividad #1: "))
                        break
                    except ValueError:
                        continue

            # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
            # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
            
            while actividad1 < 0 or actividad1 > 10:

                # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                try:
                    actividad1 = float(input("\nNota no valida, Ingrese la nota de la actividad #1: "))
                except ValueError:
                    while True:
                        try:
                            actividad1 = int(input("\nTipo de entrada no válida. Ingrese la nota de la actividad #1: "))
                            break
                        except ValueError:
                            continue

            baseDatos["actividad1"][i] = actividad1
           

            # Actividad 2

            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

            try:
                actividad2 = int(input("\n\nIngrese la nota de la actividad #2: "))
            except ValueError:
                while True:
                    try:
                        actividad2 = int(input("\nTipo de entrada no válida. Ingrese la nota de la actividad #2: "))
                        break
                    except ValueError:
                        continue

            # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
            # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
            
            while actividad2 < 0 or actividad2 > 10:

                # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                try:
                    actividad2 = float(input("\nNota no valida, Ingrese la nota de la actividad #2: "))
                except ValueError:
                    while True:
                        try:
                            actividad2 = int(input("\nTipo de entrada no válida. Ingrese la nota de la actividad #2: "))
                            break
                        except ValueError:
                            continue

            baseDatos["actividad2"][i] = actividad2


            # Examen Final

            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

            try:
                examenFinal = int(input("\n\nIngrese la nota del examen final: "))
            except ValueError:
                while True:
                    try:
                        examenFinal = int(input("\nTipo de entrada no válida. Ingrese la nota del examen final: "))
                        break
                    except ValueError:
                        continue

            # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
            # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
            
            while examenFinal < 0 or examenFinal > 10:

                # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                try:
                    examenFinal = float(input("\nNota no valida, Ingrese la nota del examen final: "))
                except ValueError:
                    while True:
                        try:
                            examenFinal = int(input("\nTipo de entrada no válida. Ingrese la nota del examen final: "))
                            break
                        except ValueError:
                            continue

            baseDatos["ExamenFinal"][i] = examenFinal
            
            # Este bloque de codigo calcula el promedio del alumno del carnet seleccionado

            baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))

            n = 0
        
        # Si el carnet no fue encontrado, el siguiente codigo consulta si desea realizar otra busqueda por carnet
        # Si el usuario ingresa un 1 = si, el codigo regresa al inicio del while donde vuelve a consultar el carnet a buscar
        # Si ingresa 2 = no el bucle se rompe y regresa al menu principal

        else:
            
            print ("\n\n\nCarnet no encontrado, desea realizar otra busqueda?")
            print ("\n1. Si")
            print ("2. No")
            
            #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

            try:
                again = int(input("\nIngrese el número de la opción que desea seleccionar: "))

            except ValueError:
                while True:
                    try:
                        again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                        break
                    except ValueError:
                        continue

            #Este bloque de codigo verifica que el numero que ingrese el usuario este dentro del rango de opciones que se muestran en el menu
            #Si el usuario ingresa un numero fuera del rango de opciones, este vuelve a imprimir el menu de opciones y solicita una entrada valida dentro del rango de opciones marcada

            while again != 1 and again != 2:
                print ("\n\n\nDesea realizar otra busqueda?")
                print ("\n1. Si")
                print ("2. No")

                #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero
                
                try:
                    again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))

                except ValueError:
                    while True:
                        try:
                            again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                            break
                        except ValueError:
                            continue

            if again == 1:
                n = 2
            else:
                n = 0

    
    #OPCION 3 MODIFICAR NOTAS DE ALUMNO

    while n == 3:

        print ("\n\n\nMODIFICAR NOTAS DE ALUMNO")
        


        # Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

        try:
            carnet = int(input("\nIngrese el número de carnet del alumno: "))
        except ValueError:
            while True:
                try:
                    carnet = int(input("\nTipo de entrada no válida. Ingrese un número de carnet valido: "))
                    break
                except ValueError:
                    continue


        # Este bloque de codigo solicita un la entrada de un numero de carnet, posterior a eso, verifica si el carnet se encuentra en la base de datos
        # Si el carnet se encuentra, este crea la variable encontrado y le asigna el valor True, ademas de esto, guarda el indice donde se encontro el canet, por ultimo rompe el bucle
        # Si no se encuentra, unicamente cambia el valor de la variable encontrado a False

        for i in range (len(baseDatos["carnet"])):
            if baseDatos["carnet"][i] == carnet:
                encontrado = True
                break
            else:
                encontrado = False

        if encontrado == True:        
            x = 1
            while x == 1:
                
                #Este bloque de codigo despliega un menu para selaccionar que nota desea modificar
                #Posterior a eso verifica si el tipo de entrada es correcta y si esta dentro del rango de opciones desplegadas
                #Despues en base a la opcion seleccionada, este permite modificar la nota seleccionada anteriormente
                #Por ultimo consulta si desea modificar otra nota

                f = True
                while f == True:
    
                    print ('\n\nSeleccione la nota que desea modificar:"')
                    print ("\n1. Tarea 1")
                    print ("2. Tarea 2")
                    print ("3. Actividad 1")
                    print ("4. Actividad 2")
                    print ("5. Examen Final")
                    print ("6. Volver al menu principal")
                 
                    #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                    try:
                        f = int(input("\nIngrese el número de la opción que desea seleccionar: "))

                    except ValueError:
                        while True:
                            try:
                                f = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                                break
                            except ValueError:
                                continue
                    
                    #Este bloque de codigo verifica que el numero que ingrese el usuario este dentro del rango de opciones que se muestran en el menu
                    #Si el usuario ingresa un numero fuera del rango de opciones, este vuelve a imprimir el menu de opciones y solicita una entrada valida dentro del rango de opciones marcada
                    
                    
                    while f != 1 and f != 2 and f != 3 and f != 4 and f != 5 and f != 6:
                        
                        print ('\n\nSeleccione la nota que desea modificar:"')
                        print ("\n1. Tarea 1")
                        print ("2. Tarea 2")
                        print ("3. Actividad 1")
                        print ("4. Actividad 2")
                        print ("5. Examen Final")
                        print ("6. Volver al menu principal")
                        
                        #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            f = int(input("\nOpcion no valida, Ingrese el número de la opción que desea seleccionar: "))

                        except ValueError:
                            while True:
                                try:
                                    f = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                                    break
                                except ValueError:
                                    continue

                    #Si el usuario selecciono la opcion 1 el siguiente codigo permite editar la nota de la tarea 1

                    if f == 1:
                      
                        # TAREA 1

                        # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            tarea1 = int(input("\n\nIngrese la nota de la tarea #1: "))
                        except ValueError:
                            while True:
                                try:
                                    tarea1 = int(input("\nTipo de entrada no válida. Ingrese la nota de la tarea #1: "))
                                    break
                                except ValueError:
                                    continue

                        # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
                        # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
                        
                        while tarea1 < 0 or tarea1 > 10:

                            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                            try:
                                tarea1 = float(input("\nNota no valida, ingrese la nota de la tarea #1: "))
                            except ValueError:
                                while True:
                                    try:
                                        tarea1 = int(input("\nTipo de entrada no válida. Ingrese la nota de la tarea #1: "))
                                        break
                                    except ValueError:
                                        continue

                        baseDatos["tarea1"][i] = tarea1

                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                        
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                                                    
                        #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            again = int(input("\nIngrese el número de la opción que desea seleccionar: "))

                        except ValueError:
                            while True:
                                try:
                                    again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                                    break
                                except ValueError:
                                    continue                        
                            
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

                        # TAREA 2

                        # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            tarea2 = int(input("\n\nIngrese la nota de la tarea #2: "))
                        except ValueError:
                            while True:
                                try:
                                    tarea2 = int(input("\nTipo de entrada no válida. Ingrese la nota de la tarea #2: "))
                                    break
                                except ValueError:
                                    continue

                        # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
                        # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
                        
                        while tarea2 < 0 or tarea2 > 10:

                            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                            try:
                                tarea2 = float(input("\nNota no valida, Ingrese la nota de la tarea #2: "))
                            except ValueError:
                                while True:
                                    try:
                                        tarea2 = int(input("\nTipo de entrada no válida. Ingrese la nota de la tarea #2: "))
                                        break
                                    except ValueError:
                                        continue

                        baseDatos["tarea2"][i] = tarea2

                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                        
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                                                    
                        #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            again = int(input("\nIngrese el número de la opción que desea seleccionar: "))

                        except ValueError:
                            while True:
                                try:
                                    again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                                    break
                                except ValueError:
                                    continue                        
                            
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

                        # Actividad 1

                        # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            actividad1 = int(input("\n\nIngrese la nota de la actividad #1: "))
                        except ValueError:
                            while True:
                                try:
                                    actividad1 = int(input("\nTipo de entrada no válida. Ingrese la nota de la actividad #1: "))
                                    break
                                except ValueError:
                                    continue

                        # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
                        # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
                        
                        while actividad1 < 0 or actividad1 > 10:

                            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                            try:
                                actividad1 = float(input("\nNota no valida, Ingrese la nota de la actividad #1: "))
                            except ValueError:
                                while True:
                                    try:
                                        actividad1 = int(input("\nTipo de entrada no válida. Ingrese la nota de la actividad #1: "))
                                        break
                                    except ValueError:
                                        continue

                        baseDatos["actividad1"][i] = actividad1

                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                        
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                                                    
                        #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            again = int(input("\nIngrese el número de la opción que desea seleccionar: "))

                        except ValueError:
                            while True:
                                try:
                                    again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                                    break
                                except ValueError:
                                    continue                        
                            
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
                        
                        # Actividad 2

                        # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            actividad2 = int(input("\n\nIngrese la nota de la actividad #2: "))
                        except ValueError:
                            while True:
                                try:
                                    actividad2 = int(input("\nTipo de entrada no válida. Ingrese la nota de la actividad #2: "))
                                    break
                                except ValueError:
                                    continue

                        # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
                        # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
                        
                        while actividad2 < 0 or actividad2 > 10:

                            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                            try:
                                actividad2 = float(input("\nNota no valida, Ingrese la nota de la actividad #2: "))
                            except ValueError:
                                while True:
                                    try:
                                        actividad2 = int(input("\nTipo de entrada no válida. Ingrese la nota de la actividad #2: "))
                                        break
                                    except ValueError:
                                        continue

                        baseDatos["actividad2"][i] = actividad2

                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                        
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                                                    
                        #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            again = int(input("\nIngrese el número de la opción que desea seleccionar: "))

                        except ValueError:
                            while True:
                                try:
                                    again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                                    break
                                except ValueError:
                                    continue                        
                            
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

                        # Examen Final

                        # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            examenFinal = int(input("\n\nIngrese la nota del examen final: "))
                        except ValueError:
                            while True:
                                try:
                                    examenFinal = int(input("\nTipo de entrada no válida. Ingrese la nota del examen final: "))
                                    break
                                except ValueError:
                                    continue

                        # Este bloque de codigo verifica que la nota ingresada este entre los valores de 0 y 10
                        # Si el usuario ingresa un valor fuera del rango establecido vuelve a solicitar el ingreso de la nota, hasta que el valor este dentro del rango
                        
                        while examenFinal < 0 or examenFinal > 10:

                            # Este bloque de codigo verifica que el tipo de entrada sea de tipo float, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                            try:
                                examenFinal = float(input("\nNota no valida, Ingrese la nota del examen final: "))
                            except ValueError:
                                while True:
                                    try:
                                        examenFinal = int(input("\nTipo de entrada no válida. Ingrese la nota del examen final: "))
                                        break
                                    except ValueError:
                                        continue

                        baseDatos["ExamenFinal"][i] = examenFinal

                        baseDatos["promedio"][i] = (baseDatos["ExamenFinal"][i]*(EXAMENFINAL/100) + baseDatos["actividad1"][i]*(ACTIVIDAD1/100) + baseDatos["actividad2"][i]*(ACTIVIDAD2/100) + baseDatos["tarea1"][i]*(TAREA1/100) + baseDatos["tarea2"][i]*(TAREA2/100))
                        
                        print ("\n\n\nNota guardada, desea realizar otra modificacion?")
                        print ("\n1. Si")
                        print ("2. No")
                                                    
                        #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

                        try:
                            again = int(input("\nIngrese el número de la opción que desea seleccionar: "))

                        except ValueError:
                            while True:
                                try:
                                    again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                                    break
                                except ValueError:
                                    continue                        
                            
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
        
        # Si el carnet no fue encontrado, el siguiente codigo consulta si desea realizar otra busqueda por carnet
        # Si el usuario ingresa un 1 = si, el codigo regresa al inicio del while donde vuelve a consultar el carnet a buscar
        # Si ingresa 2 = no el bucle se rompe y regresa al menu principal

        else:
            
            print ("\n\n\nCarnet no encontrado, desea realizar otra busqueda?")
            print ("\n1. Si")
            print ("2. No")
            
            #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

            try:
                again = int(input("\nIngrese el número de la opción que desea seleccionar: "))

            except ValueError:
                while True:
                    try:
                        again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                        break
                    except ValueError:
                        continue

            #Este bloque de codigo verifica que el numero que ingrese el usuario este dentro del rango de opciones que se muestran en el menu
            #Si el usuario ingresa un numero fuera del rango de opciones, este vuelve a imprimir el menu de opciones y solicita una entrada valida dentro del rango de opciones marcada

            while again != 1 and again != 2:
                print ("\n\n\nDesea realizar otra busqueda?")
                print ("\n1. Si")
                print ("2. No")

                #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero
                
                try:
                    again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))

                except ValueError:
                    while True:
                        try:
                            again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                            break
                        except ValueError:
                            continue

            if again == 1:
                n = 3
            else:
                n = 0

    #OPCION 4 ELIMINAR ALUMNO

    while n == 4:
        
        print ("\n\n\nELIMINAR ALUMNO")

        # Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

        try:
            carnet = int(input("\nIngrese el número de carnet del alumno: "))
        except ValueError:
            while True:
                try:
                    carnet = int(input("\nTipo de entrada no válida. Ingrese un número de carnet valido: "))
                    break
                except ValueError:
                    continue        
 
        # Este bloque de codigo solicita un la entrada de un numero de carnet, posterior a eso, verifica si el carnet se encuentra en la base de datos
        # Si el carnet se encuentra, este crea la variable encontrado y le asigna el valor True, ademas de esto, guarda el indice donde se encontro el canet, por ultimo rompe el bucle
        # Si no se encuentra, unicamente cambia el valor de la variable encontrado a False       
        
        for i in range (len(baseDatos["carnet"])):
            if baseDatos["carnet"][i] == carnet:
                encontrado = True
                indice = i
                break
            else:
                encontrado = False

        # Si el carnet fue encontrado elimina todos los elementos ubicados en el indice "i" de todas las listas dentro del diccionario baseDatos

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

        # Si el carnet no fue encontrado, el siguiente codigo consulta si desea realizar otra busqueda por carnet
        # Si el usuario ingresa un 1 = si, el codigo regresa al inicio del while donde vuelve a consultar el carnet a buscar
        # Si ingresa 2 = no el bucle se rompe y regresa al menu principal

        else:
            
            print ("\n\n\nCarnet no encontrado, desea realizar otra busqueda?")
            print ("\n1. Si")
            print ("2. No")
            
            #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero

            try:
                again = int(input("\nIngrese el número de la opción que desea seleccionar: "))

            except ValueError:
                while True:
                    try:
                        again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                        break
                    except ValueError:
                        continue

            #Este bloque de codigo verifica que el numero que ingrese el usuario este dentro del rango de opciones que se muestran en el menu
            #Si el usuario ingresa un numero fuera del rango de opciones, este vuelve a imprimir el menu de opciones y solicita una entrada valida dentro del rango de opciones marcada

            while again != 1 and again != 2:
                print ("\n\n\nDesea realizar otra busqueda?")
                print ("\n1. Si")
                print ("2. No")

                #Este bloque de codigo verifica que el tipo de entrada sea de tipo entero, esto por si el usuario ingresa un dato tipo string en lugar de un numero
                
                try:
                    again = int(input("\nOpcion no valida, ingrese el número de la opción que desea seleccionar: "))

                except ValueError:
                    while True:
                        try:
                            again = int(input("\nTipo de entrada no válida. Ingrese el número de la opción que desea seleccionar: "))
                            break
                        except ValueError:
                            continue

            if again == 1:
                n = 4
            else:
                n = 0


    #OPCION 5 MOSTRA LISTA DE APROVADOS

    if n == 5:

        print ("\n\n\nLISTA DE APROBADOS\n")

        # Este bloque de codigo recorre e imprime todos los elementos de la lista "promedio" y verifica que cada uno sea mayor o igual a 7
        # Si esto se cumple este imprimira el nombre junto al promedio en el indice "i" el cual hace referencia al elemento evaluado en promedio

        for i in range (len(baseDatos["promedio"])):
            if baseDatos["promedio"][i] >= 7:
                print(baseDatos["nombre"][i], round(baseDatos["promedio"][i],2))
                
    #OPCION 6 MOSTRA LISTA DE REPROVADOS

    if n == 6:

        print ("\n\n\nLISTA DE APROBADOS\n")

        # Este bloque de codigo recorre e imprime todos los elementos de la lista "promedio" y verifica que cada uno sea menor a 7
        # Si esto se cumple este imprimira el nombre junto al promedio en el indice "i" el cual hace referencia al elemento evaluado en promedio
        # Si el primer valor de nombre es igual a 0 este salta ese valor y pasa al siguiente
        # Este 0 nos ayuda a que las listas nunca esten vacias, de esta manera podemos evitar errores al recorrer algunas listas


        for i in range (len(baseDatos["promedio"])):
            if baseDatos["nombre"][i] == 0:
                continue
            if baseDatos["promedio"][i] < 7:
                print(baseDatos["nombre"][i], round(baseDatos["promedio"][i],2))

    #OPCION 7 MOSTRAR LISTA COMPLETA DE ESTUDIANTES

    if n == 7:

        print ("\n\n\nLISTA DE NOTAS\n")

        # Este bloque de codigo recorre e imprime todos los elementos de la lista "promedio" y verifica si es o no mayor o igual a 7
        # Si esto se cumple este almacena su estado en una variable como "Aprovado"
        # Si no, este almacena el estado "Reprobado"
        # Despues de verificar su estado, imprime el elemento en el indice "i" de las listas "nombre", "promedio" y al final imprime su estado como aprobado o reprobado
        # Asi sucesibamente con cada elemento en la lista promedio
        # Si el primer valor de nombre es igual a 0 este salta ese valor y pasa al siguiente
        # Este 0 nos ayuda a que las listas nunca esten vacias, de esta manera podemos evitar errores al recorrer algunas listas


        for i in range (len(baseDatos["promedio"])):
            if baseDatos["nombre"][i] == 0:
                continue
            if baseDatos["promedio"][i] >= 7:
                estado = "Aprobado"
            else:
                estado = "Reprobado"
            print(baseDatos["nombre"][i], round(baseDatos["promedio"][i],2),estado)

print("\nGuardando datos...")

# este codigo guarda en el archivo BaseDatos.txt el diccionario donde se almacenan los registros para poder leerlo al volver a ejecutar el codigo

with open("Proyecto Final/BaseDatos.txt", "w") as archivo:
    json.dump(baseDatos, archivo)



print ("\nPrograma Finalizado...\n")