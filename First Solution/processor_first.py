"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

Problema: Asociación de Deportes 
Archivo: processor_first.py
Descripción: Procesador de la primera solución que maneja la carga de datos,
ejecución de algoritmos con Árboles Rojinegros y generación de archivos de salida.

Diciembre 2025
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from loader import cargar_desde_archivo

from first_solution import (
    construir_arbol_jugadores,
    crear_sede,
    ArbolSedes,
    imprimir_estadisticas
)


def procesar_archivo(path_input, path_output=None):
    """
    Procesa un archivo de input y genera la salida.
    Si se proporciona path_output, guarda el resultado en ese archivo.
    Si no, imprime en consola.
    
    Args:
        path_input: Ruta al archivo de input (.py)
        path_output: Ruta al archivo de salida (.txt) o None para consola
    """
    # Cargar datos
    jugadores_data, equipos_objs, sedes_objs = cargar_desde_archivo(path_input)
    
    # Crear diccionario de los jugadores para acceder más fácil
    jugadores_dict_global = {j["id"]: j for j in jugadores_data}
    
    # Crear árbol de sedes
    arbol_sedes = ArbolSedes()
    
    # Procesar cada sede
    for sede_obj in sedes_objs:
        equipos_data = [] 
        
        for equipo_obj in sede_obj.equipos:
            ids_jugadores = []
            
            for jugador_obj in equipo_obj.jugadores:
                id_global = next((jd["id"] for jd in jugadores_data 
                                if jd["nombre"] == jugador_obj.nombre), None)
                
                if id_global:
                    ids_jugadores.append(id_global)
                    
            equipos_data.append((equipo_obj.deporte, ids_jugadores))

        nodo_sede = crear_sede(sede_obj.nombre, jugadores_dict_global, equipos_data)
        arbol_sedes.insertar(nodo_sede)

    # Obtener sedes 
    sedes_ordenadas = []
    arbol_sedes.recorrido_inorden(arbol_sedes.raiz, sedes_ordenadas)
    
    # Configurar salida
    original_stdout = sys.stdout
    if path_output:
        os.makedirs(os.path.dirname(path_output), exist_ok=True)
        sys.stdout = open(path_output, 'w', encoding='utf-8')
    
    try:
        print ("PRIMERA SOLUCIÓN")
        #resultados de las sedes y equipos ordenados
        for sede in sedes_ordenadas:
            print(f"\n\n{sede.nombre}, Rendimiento: {sede.promedio_rendimiento}")
            
            equipos_ordenados = []
            sede.arbol_equipos.recorrido_inorden(sede.arbol_equipos.raiz, equipos_ordenados)
            
            for equipo in equipos_ordenados:
                print(f"\n{equipo.nombre}, Rendimiento: {equipo.promedio_rendimiento}")
                jugador_ids = [j.id for j in equipo.jugadores]
                print("{" + ", ".join(map(str, jugador_ids)) + "}")

        #ranking
        print("\n\nRanking Jugadores:")
        ranking_jugadores = construir_arbol_jugadores(jugadores_data)
        ranking_ids = [node.id for node in ranking_jugadores]
        print("{" + ", ".join(map(str, ranking_ids)) + "}")

        #estadisticas
        imprimir_estadisticas(jugadores_data, sedes_ordenadas, ranking_jugadores)
        
        print() 
        
    finally:
        if path_output:
            sys.stdout.close()
            sys.stdout = original_stdout


def procesar_todos_los_inputs(carpeta_inputs="inputs", carpeta_outputs="outputs"):
    """
    Procesa todos los archivos .py en la carpeta de inputs y genera 
    los archivos de salida correspondientes en la carpeta outputs.
    
    Args:
        carpeta_inputs: Carpeta donde están los archivos input.py
        carpeta_outputs: Carpeta donde se guardarán los archivos output.txt
    """

    archivos_input = []
    if os.path.exists(carpeta_inputs):
        archivos_input = sorted([f for f in os.listdir(carpeta_inputs) 
                                if f.startswith("input") and f.endswith(".py")])
    
    if not archivos_input:
        raise FileNotFoundError(f"No se encontraron archivos de input en {carpeta_inputs}")
    
    for archivo in archivos_input:
        numero = archivo.replace("input", "").replace(".py", "")
        path_input = os.path.join(carpeta_inputs, archivo)
        path_output = os.path.join(carpeta_outputs, f"output{numero}.txt")
        
        procesar_archivo(path_input, path_output)
