"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

SEGUNDA SOLUCIÓN
Problema: Asociación de Deportes 
Estructura de datos utilizada: Listas nativas + Merge Sort + Insertion Sort
Archivo: second_solution.py

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
        NAda porque la lista A se ordena in-place
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
        Nada porque la lista A se modifica in-place
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
        -1 si j1 debe ir antes que j2
         0 si son equivalentes en el ordenamiento
         1 si j2 debe ir antes que j1
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


# Función de prueba antes de usar las input
def prueba_merge_jugadores():
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

    merge_sort_jugadores(jugadores_data, 0, len(jugadores_data) - 1)
    # print((len(jugadores_data)-1)//2)
    # print((0 + (len(jugadores_data) - 1))//2)
    
    #resultado
    print("\nJugadores ordenados:")
    for j in jugadores_data:
        print(f"ID: {j['id']}, {j['nombre']}, Edad: {j['edad']}, Rendimiento: {j['rendimiento']}")
    
    print("\nRanking:")
    ranking_ids = [j['id'] for j in jugadores_data]
    print("{" + ", ".join(map(str, ranking_ids)) + "}")
    print()


if __name__ == "__main__":
    prueba_merge_jugadores()