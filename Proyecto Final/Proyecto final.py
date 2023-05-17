baseDatos = {
    
    "nombre" : [0],
    "carnet" : [0],
    "grado" : [0],
    "nota1" : [0],
    "nota2" : [0],
    "nota3" : [0],
    "promedio" : [0]

}

notasCant = 3
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
        baseDatos["grado"].append(int(input("\nIngrese el grado del alumno: ")))
        baseDatos["nota1"].append(None)
        baseDatos["nota2"].append(None)
        baseDatos["nota3"].append(None)
        baseDatos["promedio"].append(None) 

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
            
            nota1 = float(input("\n\nIngrese la nota de la primera evaluacion: "))
            while nota1 < 0 or nota1 > 10:
                nota1 = float(input("\nNota no valida, ingrese la nota de la primera evaluacion: "))
            baseDatos["nota1"][i] = nota1
            
            nota2 = float(input("\n\nIngrese la nota de la segunda evaluacion: "))
            while nota2 < 0 or nota2 > 10:
                nota2 = float(input("\nNota no valida, ingrese la nota de la segunda evaluacion: "))
            baseDatos["nota2"][i] = nota2

            nota3 = float(input("\n\nIngrese la nota de la tercera evaluacion: "))
            while nota3 < 0 or nota3 > 10:
                nota3 = float(input("\nNota no valida, ingrese la nota de la tercera evaluacion: "))
            baseDatos["nota3"][i] = nota3
            
            baseDatos["promedio"][i] = (baseDatos["nota1"][i] + baseDatos["nota2"][i] + baseDatos["nota3"][i]) / notasCant 

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
            
            nota1 = float(input("\n\nIngrese la correccion de la primera evaluacion: "))
            while nota1 < 0 or nota1 > 10:
                nota1 = float(input("\nNota no valida, ingrese la correccion de la primera evaluacion: "))
            baseDatos["nota1"][i] = nota1
            
            nota2 = float(input("\n\nIngrese la correccion de la segunda evaluacion: "))
            while nota2 < 0 or nota2 > 10:
                nota2 = float(input("\nNota no valida, ingrese la correccion de la segunda evaluacion: "))
            baseDatos["nota2"][i] = nota2

            nota3 = float(input("\n\nIngrese la correccion de la tercera evaluacion: "))
            while nota3 < 0 or nota3 > 10:
                nota3 = float(input("\nNota no valida, ingrese la correccion de la tercera evaluacion: "))
            baseDatos["nota3"][i] = nota3
            
            for e in range (1,len(baseDatos["promedio"]),1):
                baseDatos["promedio"][e] = (baseDatos["nota1"][i] + baseDatos["nota2"][i] + baseDatos["nota3"][i]) / notasCant
            
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
            baseDatos["nota1"].pop(indice)
            baseDatos["nota2"].pop(indice)
            baseDatos["nota3"].pop(indice)
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
                print(baseDatos["nombre"][i], round(baseDatos["promedio"][i]),2)
                
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
            print(baseDatos["nombre"][i], round(baseDatos["promedio"][i],2))
        

print ("\nPrograma Finalizado...\n")