"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

Problema: Asociación de Deportes 
Archivo: classes.py
Descripción: Define las clases básicas Jugador, Equipo y Sede utilizadas 
para interpretar los archivos de entrada del proyecto.

Diciembre 2025
"""

# Clases para interpretar los inputs del proyecto
class Jugador:
    def __init__(self, nombre, edad, rendimiento):
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento


class Equipo:
    def __init__(self, deporte, jugadores):
        self.deporte = deporte
        self.jugadores = jugadores  

class Sede:
    def __init__(self, nombre, equipos):
        self.nombre = nombre
        self.equipos = equipos
