"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

Problema: Asociación de Deportes 
Archivo: main.py

Diciembre 2025
"""
import sys
import os

print("=" * 70)
print("PROYECTO: ASOCIACIÓN DE DEPORTES")
print("Juan José Cortés Rodríguez - 2325109")
print("=" * 70)

# PRIMERA SOLUCIÓN: 
print("\n" + "=" * 70)
print("EJECUTANDO PRIMERA SOLUCIÓN - Árboles Rojinegros")
print("=" * 70)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'First Solution'))

import processor_first as processor_primera
import importlib

procesar_primera = processor_primera.procesar_todos_los_inputs

# Procesar archivos
procesar_primera(
    carpeta_inputs=os.path.join(os.path.dirname(__file__), "inputs"),
    carpeta_outputs=os.path.join(os.path.dirname(__file__), "First Solution", "outputs")
)
print("\nSalidas de la primera solución almacenadas en: 'First Solution/outputs'")

# Eliminar módulos de la primera solución del caché
modulos_a_eliminar = [mod for mod in sys.modules.keys() 
                      if 'processor' in mod or 'first_solution' in mod or 'loader' in mod]
for mod in modulos_a_eliminar:
    del sys.modules[mod]

# Limpiar path de primera solución
sys.path = [p for p in sys.path if 'First Solution' not in p]


# SEGUNDA SOLUCIÓN: 
print("\n" + "=" * 70)
print("EJECUTANDO SEGUNDA SOLUCIÓN - Merge Sort + Insertion Sort")
print("=" * 70)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Second Solution'))

import processor_second as processor_segunda
importlib.reload(processor_segunda)  

procesar_segunda = processor_segunda.procesar_todos_los_inputs

procesar_segunda(
    carpeta_inputs=os.path.join(os.path.dirname(__file__), "inputs"),
    carpeta_outputs=os.path.join(os.path.dirname(__file__), "Second Solution", "outputs")
)
print("\nSalidas de la segunda solución almacenadas en: 'Second Solution/outputs'")
