"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

Problema: Asociación de Deportes 
Archivo: benchmark.py
Descripción: Mide tiempos de ejecución COMPLETOS de ambas soluciones 
(ordenamiento + estadísticas) con instancias de tamaños crecientes.

Diciembre 2025
"""

import time
import sys
import os
import random

# Importar primera solución
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'First Solution'))
from first_solution import (
    construir_arbol_jugadores, 
    crear_sede, 
    ArbolSedes,
    encontrar_equipo_mayor_menor_rendimiento,
    encontrar_jugador_mayor_menor_rendimiento,
    encontrar_jugador_mas_joven_veterano,
    calcular_promedio_edad_rendimiento
)

# Limpiar y cargar segunda solución
sys.path = [p for p in sys.path if 'First Solution' not in p]
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Second Solution'))
from second_solution import (
    merge_sort_jugadores, 
    crear_sede as crear_sede_segunda, 
    insertion_sort_sedes
)


def generar_instancia_conocida(n):
    """
    Genera una instancia CONOCIDA (no aleatoria) con n jugadores.
    
    Los datos son determinísticos basados en el índice:
    - Edad: 20 + (i % 30) → Edades entre 20 y 49
    - Rendimiento: 10 + (i % 90) → Rendimientos entre 10 y 99
    
    Args:
        n (int): Número de jugadores
        
    Returns:
        tuple: (jugadores, equipos_data, num_sedes)
    """
    jugadores = []
    for i in range(1, n + 1):
        jugadores.append({
            'id': i,
            'nombre': f"Jugador{i}",
            'edad': 20 + (i % 30),
            'rendimiento': 10 + (i % 90)
        })
    
    num_equipos = max(1, n // 4)
    equipos_data = []
    deportes = ["Futbol", "Volleyball", "Basketball", "Tenis", "Natacion"]
    
    for i in range(num_equipos):
        deporte = deportes[i % len(deportes)]
        start_id = i * 4 + 1
        end_id = min(start_id + 4, n + 1)
        ids_equipo = list(range(start_id, end_id))
        equipos_data.append((deporte, ids_equipo))
    
    num_sedes = max(1, num_equipos // 2)
    
    return jugadores, equipos_data, num_sedes

def generar_instancia_peor_caso(n):
    """
    Genera una instancia PEOR CASO (completamente desordenada) con n jugadores.
    
    Los datos se generan aleatoriamente para garantizar que no estén ordenados.
    Se utiliza una seed para garantizar reproducibilidad.
    
    Args:
        n (int): Número de jugadores
        seed (int): Seed para garantizar reproducibilidad
        
    Returns:
        tuple: (jugadores, equipos_data, num_sedes)
    """
    random.seed(123)  # Establecer la seed para reproducibilidad
    
    jugadores = []
    for i in range(1, n + 1):
        jugadores.append({
            'id': i,
            'nombre': f"Jugador{i}",
            'edad': random.randint(20, 49),  # Edades aleatorias entre 20 y 49
            'rendimiento': random.randint(10, 99)  # Rendimientos aleatorios entre 10 y 99
        })
    
    
    num_equipos = max(1, n // 4)
    equipos_data = []
    deportes = ["Futbol", "Volleyball", "Basketball", "Tenis", "Natacion"]
    
    for i in range(num_equipos):
        deporte = deportes[i % len(deportes)]
        start_id = i * 4 + 1
        end_id = min(start_id + 4, n + 1)
        ids_equipo = list(range(start_id, end_id))
        equipos_data.append((deporte, ids_equipo))
    
    num_sedes = max(1, num_equipos // 2)
    
    return jugadores, equipos_data, num_sedes


def medir_tiempo_primera_solucion(jugadores, equipos_data, num_sedes):
    """
    Mide el tiempo COMPLETO de la primera solución:
    - Ordenamiento de jugadores, equipos y sedes
    - Cálculo de todas las estadísticas
    
    Args:
        jugadores (list): Lista de jugadores
        equipos_data (list): Lista de equipos
        num_sedes (int): Número de sedes
        
    Returns:
        float: Tiempo total en segundos
    """
    jugadores_dict = {j['id']: j for j in jugadores}
    equipos_por_sede = len(equipos_data) // num_sedes
    
    inicio = time.perf_counter()
    
    # 1. Crear y ordenar sedes
    arbol_sedes = ArbolSedes()
    
    for i in range(num_sedes):
        start = i * equipos_por_sede
        end = start + equipos_por_sede if i < num_sedes - 1 else len(equipos_data)
        equipos_sede = equipos_data[start:end]
        
        nodo_sede = crear_sede(f"Sede{i+1}", jugadores_dict, equipos_sede)
        arbol_sedes.insertar(nodo_sede)
    
    sedes_ordenadas = []
    arbol_sedes.recorrido_inorden(arbol_sedes.raiz, sedes_ordenadas)
    
    # 2. Crear ranking de jugadores
    ranking = construir_arbol_jugadores(jugadores)
    
    # 3. Calcular estadísticas (como en el output real)
    (eq_mayor, sede_mayor), (eq_menor, sede_menor) = encontrar_equipo_mayor_menor_rendimiento(sedes_ordenadas)
    jug_mayor, jug_menor = encontrar_jugador_mayor_menor_rendimiento(ranking)
    mas_joven, mas_veterano = encontrar_jugador_mas_joven_veterano(jugadores)
    prom_edad, prom_rend = calcular_promedio_edad_rendimiento(jugadores)
    
    fin = time.perf_counter()
    
    return fin - inicio


def medir_tiempo_segunda_solucion(jugadores, equipos_data, num_sedes):
    """
    Mide el tiempo COMPLETO de la segunda solución:
    - Ordenamiento de jugadores, equipos y sedes
    - Cálculo de todas las estadísticas
    
    Args:
        jugadores (list): Lista de jugadores
        equipos_data (list): Lista de equipos
        num_sedes (int): Número de sedes
        
    Returns:
        float: Tiempo total en segundos
    """
    jugadores_dict = {j['id']: j for j in jugadores}
    equipos_por_sede = len(equipos_data) // num_sedes
    
    inicio = time.perf_counter()
    
    # 1. Crear y ordenar sedes
    sedes = []
    for i in range(num_sedes):
        start = i * equipos_por_sede
        end = start + equipos_por_sede if i < num_sedes - 1 else len(equipos_data)
        equipos_sede = equipos_data[start:end]
        
        sede_dict = crear_sede_segunda(f"Sede{i+1}", jugadores_dict, equipos_sede)
        sedes.append(sede_dict)
    
    sedes_ordenadas = insertion_sort_sedes(sedes)
    
    # 2. Crear ranking de jugadores
    jugadores_ranking = jugadores.copy()
    merge_sort_jugadores(jugadores_ranking, 0, len(jugadores_ranking) - 1)
    
    # 3. Calcular estadísticas (misma lógica que primera solución)
    # Equipo con mayor/menor rendimiento
    eq_mayor_rend = -1
    eq_menor_rend = float('inf')
    eq_mayor_obj = None
    eq_menor_obj = None
    
    for sede in sedes_ordenadas:
        for equipo in sede['equipos']:
            if equipo['promedio_rendimiento'] > eq_mayor_rend:
                eq_mayor_rend = equipo['promedio_rendimiento']
                eq_mayor_obj = equipo
            if equipo['promedio_rendimiento'] < eq_menor_rend:
                eq_menor_rend = equipo['promedio_rendimiento']
                eq_menor_obj = equipo
    
    # Jugador con mayor/menor rendimiento
    jug_mayor_rend = max(jugadores_ranking, key=lambda j: j['rendimiento'])
    jug_menor_rend = min(jugadores_ranking, key=lambda j: j['rendimiento'])
    
    # Jugador más joven/veterano
    mas_joven = min(jugadores, key=lambda j: (j['edad'], j['id']))
    mas_veterano = max(jugadores, key=lambda j: (j['edad'], -j['id']))
    
    # Promedios
    suma_edades = sum(j['edad'] for j in jugadores)
    suma_rendimientos = sum(j['rendimiento'] for j in jugadores)
    prom_edad = suma_edades / len(jugadores)
    prom_rend = suma_rendimientos / len(jugadores)
    
    fin = time.perf_counter()
    
    return fin - inicio


def ejecutar_benchmarks():
    """
    Ejecuta benchmarks con instancias conocidas de tamaños crecientes.
    Mide tiempos COMPLETOS (ordenamiento + estadísticas).
    """
    print("=" * 70)
    print("BENCHMARK - ANÁLISIS DE COMPLEJIDAD TEMPORAL COMPLETO")
    print("=" * 70)
    
    tamanios = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 100000]
    resultados = []
    
    for n in tamanios:
        print(f"\n{'='*70}")
        print(f"Probando con n = {n} jugadores")
        print(f"{'='*70}")
        
        # jugadores, equipos_data, num_sedes = generar_instancia_conocida(n)
        jugadores, equipos_data, num_sedes = generar_instancia_peor_caso(n)

        print(f"    - Jugadores: {len(jugadores)}")
        print(f"    - Equipos: {len(equipos_data)}")
        print(f"    - Sedes: {num_sedes}")
        
        # Medir primera solución (promedio de 5 ejecuciones)
        tiempos_primera = []
        for _ in range(5):
            t = medir_tiempo_primera_solucion(jugadores.copy(), equipos_data.copy(), num_sedes)
            tiempos_primera.append(t)
        tiempo_primera = sum(tiempos_primera) / len(tiempos_primera)
        
        # Medir segunda solución (promedio de 5 ejecuciones)
        tiempos_segunda = []
        for _ in range(5):
            t = medir_tiempo_segunda_solucion(jugadores.copy(), equipos_data.copy(), num_sedes)
            tiempos_segunda.append(t)
        tiempo_segunda = sum(tiempos_segunda) / len(tiempos_segunda)
        
        resultados.append({
            'n': n,
            'primera': tiempo_primera,
            'segunda': tiempo_segunda
        })
        
        print(f"\n  Resultados (promedio de 5 ejecuciones):")
        print(f"    Primera solución:  {tiempo_primera*1000:.4f} ms")
        print(f"    Segunda solución:  {tiempo_segunda*1000:.4f} ms")
        
        if tiempo_primera < tiempo_segunda:
            diferencia_pct = ((tiempo_segunda - tiempo_primera) / tiempo_primera) * 100
            print(f"La primera solución es {diferencia_pct:.2f}% más rápida")
        else:
            diferencia_pct = ((tiempo_primera - tiempo_segunda) / tiempo_segunda) * 100
            print(f"La segunda solución es {diferencia_pct:.2f}% más rápida")
    
    # Guardar resultados
    output_dir = os.path.dirname(__file__) 
    output_file = os.path.join(output_dir, "benchmark_results.csv")
    with open(output_file, "w", encoding='utf-8') as f:
        f.write("n,tiempo_primera_ms,tiempo_segunda_ms\n")
        for r in resultados:
            f.write(f"{r['n']},{r['primera']*1000},{r['segunda']*1000}\n")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    ejecutar_benchmarks()