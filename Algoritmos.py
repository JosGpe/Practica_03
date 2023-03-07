#Funcion para procesar el archivo 
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as nom_arch:
        lineas = nom_arch.readlines()
    procesos = []
    for linea in lineas:
        nombre, tiempo, prioridad = linea.strip().split(',')
        proceso = {'Nombre': nombre, 'Tiempo': int(tiempo), 'Prioridad': int(prioridad)}
        procesos.append(proceso)

    return procesos

nombre_archivo = 'E:/SSPSO/procesos.txt'
procesos = leer_archivo(nombre_archivo)

#Funcion: algoritmo Round Robin
def round_robin(procesos):
    procesos_restantes = len(procesos)
    tiempo_transcurrido = 0
    quantum = 3
    proceso_actual = 0
    #Selecciona el proceso actual 
    while procesos_restantes > 0:
        proceso = procesos[proceso_actual]
        #Verifica el proceso si tiene tiempo restante para ejecutarse 
        if proceso["Tiempo"] > 0:
            print(f"{proceso['Nombre']} corriendo por {min(quantum, proceso['Tiempo'])} segundos...")
            tiempo_ejecucion = min(quantum, proceso['Tiempo'])
            proceso["Tiempo"] -= tiempo_ejecucion
            tiempo_transcurrido += tiempo_ejecucion
            #Si el proceso termina durante este tiempo, disminuye contador de procesos restantes y se elimina
            if proceso["Tiempo"] == 0:
                procesos_restantes -= 1
                procesos.pop(proceso_actual)
                #Establece indice y continua con el siguiente proceso
                if proceso_actual == len(procesos):
                    proceso_actual = 0
            #Si no termina durante este tiempo, se mueve cola y continua con el siguiente proceso
            else:
                proceso_actual = (proceso_actual + 1) % len(procesos)
        #Si el proceso actual no tiene tiempo , disminuye contador y se elimina 
        else:
            procesos_restantes -= 1
            procesos.pop(proceso_actual)
            #Establece indice y continua con el siguiente proceso
            if proceso_actual == len(procesos):
                proceso_actual = 0
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos") 

#Funcion: algoritmo SJF
def sjf(procesos):
    tiempo_transcurrido = 0
    #Ordena los procesos en orden ascendente 
    procesos_ordenados = sorted(procesos, key=lambda p: p["Tiempo"])
    for proceso in procesos_ordenados:
        print(f"{proceso['Nombre']} corriendo por {proceso['Tiempo']} segundos...")
        #Mide el tiempo total trancurrido de cada proceso
        tiempo_transcurrido += proceso["Tiempo"]
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

#Funcion: algoritmo FIFO
def fifo(procesos):
    tiempo_transcurrido = 0
    for proceso in procesos:
        print(f"{proceso['Nombre']} corriendo por {proceso['Tiempo']} segundos...")
        #Mide el tiempo total trancurrido de cada proceso 
        tiempo_transcurrido += proceso["Tiempo"]
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

#Funcion: Prioridades
def prioridad(procesos):
    procesos_restantes = len(procesos)
    tiempo_transcurrido = 0
    while procesos_restantes > 0:
        # Ordenar los procesos por prioridad de forma ascendente
        procesos = sorted(procesos, key=lambda x: x['Prioridad'])
        # Ejecutar el proceso con mayor prioridad
        proceso = procesos[0]
        print(f"{proceso['Nombre']} corriendo por {proceso['Tiempo']} segundos...")
        #Mide el tiempo total trancurrido de cada proceso
        tiempo_transcurrido += proceso['Tiempo']
        procesos_restantes -= 1
        # Eliminar el proceso de la lista
        procesos.pop(0)
    print(f"Todos los procesos han terminado en {tiempo_transcurrido} segundos")

#Funcion para correr los algoritmos
def algoritmos(procesos):
    print("Corriendo algoritmo SJF:")
    sjf(procesos)
    print("\n")

    print("Corriendo algoritmo FIFO:")
    fifo(procesos)
    print("\n")

    print("Corriendo algoritmo Prioridades:")
    prioridad(procesos)
    print("\n")

    print("Corriendo algoritmo Round Robin:")
    round_robin(procesos)
    print("\n")
    
algoritmos(procesos)