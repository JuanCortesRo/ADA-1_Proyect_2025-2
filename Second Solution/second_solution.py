"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

Problema: Asociación de Deportes 
Archivo: second_solution.py
Descripción: Desarrollo de la Segunda solución utilizando Merge Sort para 
jugadores e Insertion Sort para equipos y sedes según los criterios del enunciado.

Diciembre 2025
"""

# ========================================================================================
# MERGE SORT PARA JUGADORES
# Utiliza el algoritmo merge sort visto en clase para ordenar jugadores
# ========================================================================================

def merge_sort_jugadores(A, p, r):
    """
    Ordena jugadores usando Merge Sort 
    
    Args:
        A: Lista de jugadores a ordenar (se modifica in-place)
        p: Índice inicial del subarreglo (0-indexed)
        r: Índice final del subarreglo (0-indexed)
    
    Returns:
        None: Porque la lista A se ordena in-place
    """
    if p < r:
        q = (p + r) // 2
        merge_sort_jugadores(A, p, q)
        merge_sort_jugadores(A, q + 1, r)
        merge_jugadores(A, p, q, r)


def merge_jugadores(A, p, q, r):
    """
    Implementación del procedimiento MERGE 
    
    Args:
        A: Lista de jugadores
        p: Índice inicial del primer subarreglo
        q: Índice final del primer subarreglo
        r: Índice final del segundo subarreglo

    Returns: 
        None: Porque la lista A se modifica in-place
    """
    
    n1 = q - p + 1
    n2 = r - q
    
    L = [None] * (n1+1)
    R = [None] * (n2+1)
    
    for i in range(n1):
        L[i] = A[p + i]
    
    for j in range(n2):
        R[j] = A[q + 1 + j]
    
    L[n1] = {'id': float('inf'), 'rendimiento': float('inf'), 'edad': -1, 'nombre': 'SENTINEL'}
    R[n2] = {'id': float('inf'), 'rendimiento': float('inf'), 'edad': -1, 'nombre': 'SENTINEL'}
    
    i = 0
    j = 0

    for k in range(p, r + 1):
        if comparar_jugadores(L[i], R[j]) <= 0:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def comparar_jugadores(j1, j2):
    """
    Función de comparación para jugadores

    Args:
        j1: Diccionario del jugador 1
        j2: Diccionario del jugador 2
    
    Returns:
        int: -1 si j1 debe ir antes que j2, 0 si son equivalentes en el ordenamiento, 1 si j2 debe ir antes que j1
    """
    # comparar rendimiento
    if j1['rendimiento'] < j2['rendimiento']:
        return -1
    elif j1['rendimiento'] > j2['rendimiento']:
        return 1
    
    # si hay empate por rendimiento, dejar el de mayor edad primero
    if j1['edad'] > j2['edad']:
        return -1
    elif j1['edad'] < j2['edad']:
        return 1
    
    # si incluso hay empate por edad, dejar primero el de menor ID
    if j1['id'] < j2['id']:
        return -1
    elif j1['id'] > j2['id']:
        return 1
    
    return 0

# ========================================================================================
# INSERTION SORT PARA EQUIPOS
# utilicé el algoritmo insertion sort del curso para ordenar los equipos
# ========================================================================================

def insertion_sort_equipos(lista_equipos):
    """
    Ordena equipos usando Insertion Sort.
    
    Args:
        lista_equipos: Lista de equipos a ordenar (se modifica in-place)

    Returns:
        list: Lista de equipos ordenada según los criterios dados
    """
    n = len(lista_equipos)
    
    if n <= 1:
        return lista_equipos
    
    #insertion sort
    for j in range(1, n):
        key = lista_equipos[j]
        
        i = j - 1
        
        while i >= 0 and comparar_equipos(lista_equipos[i], key) > 0:
            lista_equipos[i + 1] = lista_equipos[i]

            i = i - 1
        
        lista_equipos[i + 1] = key
    
    return lista_equipos


def comparar_equipos(eq1, eq2):
    """
    Compara dos equipos según los criterios de desempate.
    
    Args:
        eq1: Diccionario del equipo 1
        eq2: Diccionario del equipo 2  

    Returns:    
        int: -1 si eq1 debe ir antes que eq2, 0 si son equivalentes, 1 si eq2 debe ir antes que eq1
    """
    #promedio rendimiento ascendente
    if eq1['promedio_rendimiento'] < eq2['promedio_rendimiento']:
        return -1
    elif eq1['promedio_rendimiento'] > eq2['promedio_rendimiento']:
        return 1
    
    #si hay empate de rendimiento criterio 2: cantidad de jugadores descendiente
    if eq1['cantidad_jugadores'] > eq2['cantidad_jugadores']:
        return -1
    elif eq1['cantidad_jugadores'] < eq2['cantidad_jugadores']:
        return 1
    
    return 0

def crear_equipo(nombre_deporte, jugadores_dict, ids_jugadores):
    """
    Crea un equipo con jugadores ordenados gracias al mergesort
    
    Args:
        nombre_deporte: Nombre del deporte 
        jugadores_dict: Diccionario global de jugadores
        ids_jugadores: Lista de cuales jugadores hacen parte del equipo (sus IDs)
    
    Returns:
        dict: Diccionario con información del equipo y jugadores ordenados
    """
    #obtiene la lista de jugadores del equipo
    jugadores_equipo = [jugadores_dict[id_jug] for id_jug in ids_jugadores]
    
    if len(jugadores_equipo) > 0:
        merge_sort_jugadores(jugadores_equipo, 0, len(jugadores_equipo) - 1)
    
    #calcula el promedio de rendimiento
    suma_rendimientos = sum(j['rendimiento'] for j in jugadores_equipo)
    promedio = suma_rendimientos / len(jugadores_equipo) if jugadores_equipo else 0
    
    return {
        'nombre': nombre_deporte,
        'promedio_rendimiento': promedio,
        'cantidad_jugadores': len(jugadores_equipo),
        'jugadores': jugadores_equipo  # Ya está ordenada in-place
    }

# ========================================================================================
# INSERTION SORT PARA SEDES
# Al igual que para los equipos, se utiliza interionsort para ordenar las sedes
# ========================================================================================

def insertion_sort_sedes(lista_sedes):
    """
    Ordena sedes usando Insertion Sort

    Args:
        lista_sedes: Lista de sedes a ordenar (se modifica in-place)

    Returns:
        list: Lista de sedes ordenada según los criterios dados
    """
    n = len(lista_sedes)
    
    if n <= 1:
        return lista_sedes
    
    # insertion sort
    for j in range(1, n):

        key = lista_sedes[j]
        
        i = j - 1
        
        while i >= 0 and comparar_sedes(lista_sedes[i], key) > 0:
            lista_sedes[i + 1] = lista_sedes[i]
            
            i = i - 1
        
        lista_sedes[i + 1] = key
    
    return lista_sedes

def comparar_sedes(sede1, sede2):
    """
    Compara dos sedes según los criterios del enunciado.
    
    Args:
        sede1: Diccionario de la sede 1
        sede2: Diccionario de la sede 2

    Returns:
        int: -1 si sede1 debe ir antes que sede2, 0 si son equivalentes, 1 si sede2 debe ir antes que sede1
    """
    # Criterio 1: Promedio rendimiento ASCENDENTE
    if sede1['promedio_rendimiento'] < sede2['promedio_rendimiento']:
        return -1
    elif sede1['promedio_rendimiento'] > sede2['promedio_rendimiento']:
        return 1
    
    # Empate en promedio: Criterio 2: Total jugadores DESCENDENTE
    if sede1['total_jugadores'] > sede2['total_jugadores']:
        return -1
    elif sede1['total_jugadores'] < sede2['total_jugadores']:
        return 1
    
    return 0

def crear_sede(nombre_sede, jugadores_dict, equipos_data):
    """
    Crea una sede con equipos ordenados usando Insertion Sort.
    
    Args:
        nombre_sede: Nombre de la sede
        jugadores_dict: Diccionario global
        equipos_data: Lista de tuplas (nombre_deporte, ids_jugadores)
    
    Returns:
        dict: Diccionario con información de la sede y equipos ordenados
    """
    #crea la lista de equipos inicialmente vacía
    equipos = []
    #creamos variables para el total de jugadores y suma de promedios
    total_jugadores = 0
    suma_promedios = 0
    
    for nombre_deporte, ids_jugadores in equipos_data:
        equipo = crear_equipo(nombre_deporte, jugadores_dict, ids_jugadores)
        equipos.append(equipo)
        total_jugadores += equipo['cantidad_jugadores']
        suma_promedios += equipo['promedio_rendimiento']
    
    equipos_ordenados = insertion_sort_equipos(equipos)
    
    promedio_sede = suma_promedios

    return {
        'nombre': nombre_sede,
        'promedio_rendimiento': promedio_sede,
        'total_jugadores': total_jugadores,
        'equipos': equipos_ordenados
    }

# Función de prueba antes de usar las input
# Esta funcion me sirvió para ir probando la implementación antes de utilizar los inputs...
def prueba():
    # Datos de prueba del enunciado
    jugadores_data = [
        {"id": 1, "nombre": "Sofía García", "edad": 21, "rendimiento": 66},
        {"id": 2, "nombre": "Alejandro Torres", "edad": 27, "rendimiento": 24},
        {"id": 3, "nombre": "Valentina Rodríguez", "edad": 19, "rendimiento": 15},
        {"id": 4, "nombre": "Juan López", "edad": 22, "rendimiento": 78},
        {"id": 5, "nombre": "Martina Martínez", "edad": 30, "rendimiento": 55},
        {"id": 6, "nombre": "Sebastián Pérez", "edad": 25, "rendimiento": 42},
        {"id": 7, "nombre": "Camila Fernández", "edad": 24, "rendimiento": 36},
        {"id": 8, "nombre": "Mateo González", "edad": 29, "rendimiento": 89},
        {"id": 9, "nombre": "Isabella Díaz", "edad": 21, "rendimiento": 92},
        {"id": 10, "nombre": "Daniel Ruiz", "edad": 17, "rendimiento": 57},
        {"id": 11, "nombre": "Luciana Sánchez", "edad": 18, "rendimiento": 89},
        {"id": 12, "nombre": "Lucas Vásquez", "edad": 26, "rendimiento": 82}
    ]

    #parte de los equipos
    jugadores_dict = {j['id']: j for j in jugadores_data}

    sede_cali = crear_sede("Sede Cali", jugadores_dict, [("Futbol", [2, 10]), ("Volleyball", [1, 9, 12, 6])])
    
    sede_medellin = crear_sede("Sede Medellin", jugadores_dict, [("Futbol", [11, 8, 7]), ("Volleyball", [3, 4, 5])])

    sedes = [sede_medellin, sede_cali]  # Desordenadas a propósito
    sedes_ordenadas = insertion_sort_sedes(sedes)

    for sede in sedes_ordenadas:
        print(f"\n\n{sede['nombre']}, Rendimiento: {sede['promedio_rendimiento']}")
        
        for equipo in sede['equipos']:
            print(f"\n{equipo['nombre']}, Rendimiento: {equipo['promedio_rendimiento']}")
            ids = [j['id'] for j in equipo['jugadores']]
            print("{" + ", ".join(map(str, ids)) + "}")

    #parte del ranking
    merge_sort_jugadores(jugadores_data, 0, len(jugadores_data) - 1)

    print("\n\nRanking Jugadores:")
    ranking_ids = [j['id'] for j in jugadores_data]
    print("{" + ", ".join(map(str, ranking_ids)) + "}")
    print()


if __name__ == "__main__":
    prueba()
