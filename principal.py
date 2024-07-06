import funciones as fn
alumnos = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
    "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
    ]

creditos_alumnos = {} # indicar que es un diccionario de creditos

while True:
    print("------MENU-----")
    print("0. Inicializar Créditos")
    print("1. Asignar Créditos aleatorios")
    print("2. Clasificar Créditos")
    print("3. Calcular Estadísticas")
    print("4. Generar Reporte en csv")
    print("5. Salir")

    opcion = int(input("Ingrese su opción: "))
    if opcion == 0:
        creditos_alumnos = {alumno : 0 for alumno in alumnos} # inicializar el diccionario en 0
        print("Créditos inicializados correctamente")
    elif opcion == 1 :
        if not creditos_alumnos:
            print("Primero debe inicializar los créditos")
        else:
            creditos_alumnos = fn.asignar_Creditos_aleatorios(alumnos)
    elif opcion == 2:
        if creditos_alumnos :
            fn.clasificar_creditos(creditos_alumnos)
        else:
            print("Primero debe asignar créditos")
    elif opcion == 3:
        if creditos_alumnos:
            max_credito,min_credito,promedio_credito = fn.calcular_estadisticas(creditos_alumnos)
            if max_credito is not None:
                print("Credito máximo: $",max_credito)
                print("Credito mínimo: $",min_credito)
                print("Promedio de Créditos: $",promedio_credito)
            else:
                print("Primero debe asignar créditos")

    elif opcion == 4:
        if creditos_alumnos:
            fn.generar_reporte(creditos_alumnos)
        else:
            print("Primero debe asignar créditos")

    elif opcion == 5:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, por favor ingrese una opción entre 0 y 5")

