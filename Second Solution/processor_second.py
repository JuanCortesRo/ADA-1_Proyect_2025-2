"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

Problema: Asociación de Deportes 
Archivo: processor_second.py
Descripción: Procesador de la segunda solución que maneja la carga de datos,
ejecución de algoritmos con Merge Sort + Insertion Sort y generación de archivos de salida.

Diciembre 2025
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from loader import cargar_desde_archivo

from second_solution import (
    merge_sort_jugadores,
    crear_sede,
    insertion_sort_sedes
)

#estadísticas de la primera solución ya que son reutilizables
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'First Solution'))
from first_solution import (
    imprimir_estadisticas,
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
    
    # Crear lista de sedes
    sedes = []
    
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
        
        sede_dict = crear_sede(sede_obj.nombre, jugadores_dict_global, equipos_data)
        sedes.append(sede_dict)

    # Ordenar sedes usando Insertion Sort
    sedes_ordenadas = insertion_sort_sedes(sedes)
    
    # Configurar salida
    original_stdout = sys.stdout
    if path_output:
        os.makedirs(os.path.dirname(path_output), exist_ok=True)
        sys.stdout = open(path_output, 'w', encoding='utf-8')
    
    try:
        print ("SEGUNDA SOLUCIÓN")
        #resultados de las sedes y equipos ordenados
        for sede in sedes_ordenadas:
            print(f"\n\n{sede['nombre']}, Rendimiento: {sede['promedio_rendimiento']}")
            
            for equipo in sede['equipos']:
                print(f"\n{equipo['nombre']}, Rendimiento: {equipo['promedio_rendimiento']}")
                jugador_ids = [j['id'] for j in equipo['jugadores']]
                print("{" + ", ".join(map(str, jugador_ids)) + "}")

        #ranking
        print("\n\nRanking Jugadores:")
        jugadores_ranking = jugadores_data.copy()
        merge_sort_jugadores(jugadores_ranking, 0, len(jugadores_ranking) - 1)
        ranking_ids = [j['id'] for j in jugadores_ranking]
        print("{" + ", ".join(map(str, ranking_ids)) + "}")

        # Toca adaptar las sedes_ordenadas para estadísticas ya que las
        # estadísticas esperan objetos con atributos, no diccionarios,
        # entonces creamos objetos auxiliares
        class SedeAux:
            def __init__(self, sede_dict):
                self.nombre = sede_dict['nombre']
                self.promedio_rendimiento = sede_dict['promedio_rendimiento']
                self.equipos_ordenados = []
                for eq in sede_dict['equipos']:
                    equipo_aux = EquipoAux(eq)
                    self.equipos_ordenados.append(equipo_aux)
                # Crear un objeto con método recorrido_inorden simulado
                self.arbol_equipos = type('obj', (object,), {
                    'raiz': None,
                    'NIL': None,
                    'recorrido_inorden': lambda self, nodo, resultado: resultado.extend(self_sede.equipos_ordenados)
                })()
                self_sede = self
        
        class EquipoAux:
            def __init__(self, equipo_dict):
                self.nombre = equipo_dict['nombre']
                self.promedio_rendimiento = equipo_dict['promedio_rendimiento']
                self.cantidad_jugadores = equipo_dict['cantidad_jugadores']
        
        class JugadorAux:
            def __init__(self, jugador_dict):
                self.id = jugador_dict['id']
                self.nombre = jugador_dict['nombre']
                self.dato1 = jugador_dict['edad']
                self.dato2 = jugador_dict['rendimiento']
        
        # Convertir sedes y jugadores para estadísticas
        sedes_aux = [SedeAux(s) for s in sedes_ordenadas]
        jugadores_aux = [JugadorAux(j) for j in jugadores_ranking]
        
        # Imprimir estadísticas (reutilizando función de primera solución)
        imprimir_estadisticas(jugadores_data, sedes_aux, jugadores_aux)
        
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
