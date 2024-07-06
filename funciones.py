import random
import csv


def asignar_Creditos_aleatorios(alumnos):
    """
    Función es asignar créditos aleatorios entre 50 y 200 a cada alumno
    Devuelve un diccionario con los créditos asignados
    """
    creditos_alumnos = {}
    #iterar sobre cada alumno en la lista alumnos
    for alumno in alumnos:
        # generar un numero entero aleatorio entre 50 y 200 para cada alumno
        credito = random.randint(50,200)
        #asignar al credito generado al alumno correspondiente en el diccionario
        creditos_alumnos[alumno] = credito

    print("creditos aletorios asignados correctamente")
    print(creditos_alumnos)

    return creditos_alumnos

def clasificar_creditos(creditos_alumnos):
    menor_100 = {}
    entre_100_150 = {}
    mayor_150 = {}

    for alumno,credito in creditos_alumnos.items():
        if credito < 100:
            menor_100[alumno] = credito
        elif credito <= 150:
            entre_100_150[alumno] = credito
        else:
            mayor_150[alumno] = credito

    # mostrar resultados de la clasificiación
    print("Créditos menores a 100 TOTAL",len(menor_100))
    for alumno,credito in menor_100.items():
        print(alumno,": $",credito)

    print("Créditos entre 100 y 150 TOTAL",len(entre_100_150))
    for alumno,credito in entre_100_150.items():
        print(alumno,": $",credito)

    print("Créditos mayores a 150 TOTAL",len(mayor_150))
    for alumno,credito in mayor_150.items():
        print(alumno,": $",credito)
    
def calcular_estadisticas(creditos_alumnos):
    '''
    maximo, minimo y promedio
    '''
    creditos = list(creditos_alumnos.values()) #creditos = [120,50,67,70.....]

    if not creditos:
        print("No se han asignado créditos aún")
        return None,None,None
    
    max_credito = max(creditos) # 120
    min_credito = min(creditos) # 50
    promedio_credito = sum(creditos) / len(creditos)

    return max_credito,min_credito,promedio_credito

def generar_reporte(creditos_alumnos):
    '''
    generar un reporte en formato csv con los créditos de los alumnos.
    '''
    with open('reportes_creditos.csv','w',newline='') as archivo :
        escritor = csv.writer(archivo,delimiter=',')

        #escribir encabezados
        escritor.writerow(['Nombre alumno','Crédito'])

        #escribir cada línea de datos
        for alumno,credito in creditos_alumnos.items():
            escritor.writerow([alumno,credito])
    print("Reporte generado correctamente en reportes_creditos.csv")
    



