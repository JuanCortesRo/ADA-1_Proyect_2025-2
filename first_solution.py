"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

PRIMERA SOLUCIÓN
Problema: Asociación de Deportes 
Estructura de datos utilizada: Arboles Rojinegros
Archivo: first_solution.py

Diciembre 2025
"""

# ========================================================================================
# CLASES BASE PARA JUGADORES
# ========================================================================================

class NodoJugador:
    """Nodo del árbol rojinegro para los jugadores"""
    def __init__(self, id_jugador, edad, rendimiento, nombre):
        self.id = id_jugador
        self.edad = edad
        self.rendimiento = rendimiento
        self.nombre = nombre
        self.color = 'R'  # 'R' para rojo, 'B' para negro
        self.izq = None
        self.der = None
        self.padre = None
    
    def __str__(self):
        return f"Jugador(ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}, Rendimiento: {self.rendimiento}, Color: {self.color})"

#Funcion temporal para probar la estructura de nodos
def ejecutar_prueba():
    print("=== PRUEBA: Estructura de Nodos para Jugadores ===\n")
    
    # el orden de los parametros es id, edad, rendimiento, nombre
    j1 = NodoJugador(1, 21, 66, "Sofía García")
    j2 = NodoJugador(2, 27, 24, "Alejandro Torres")
    j3 = NodoJugador(3, 19, 15, "Valentina Rodríguez")
    
    print("Jugadores creados:")
    print(j1)
    print(j2)
    print(j3)
    
    print("\n✅ Estructura básica de nodos funcionando correctamente")

if __name__ == "__main__":
    ejecutar_prueba()