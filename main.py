"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

PRIMERA SOLUCIÓN
Problema: Asociación de Deportes 
Archivo: main.py

Diciembre 2025
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'First Solution'))

from processor import procesar_todos_los_inputs

print("=" * 70)
print("PROYECTO: ASOCIACIÓN DE DEPORTES")
print("Juan José Cortés Rodríguez - 2325109")
print("Primera Solución - Árboles Rojinegros")
print("=" * 70)

# Procesar todos los archivos input*.py y generar output*.txt
procesar_todos_los_inputs(
    carpeta_inputs=os.path.join(os.path.dirname(__file__), "inputs"),
    carpeta_outputs=os.path.join(os.path.dirname(__file__), "First Solution", "outputs")
)

print("\n✅ Todas las pruebas completadas exitosamente")
