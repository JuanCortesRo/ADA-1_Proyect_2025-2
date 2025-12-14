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

from loader import cargar_desde_archivo

# ========================================================================================
# CLASES BASE 
# Estas se utilizarán para construir los árboles rojinegros específicos de cada caso
# ========================================================================================

class NodoRB:
    """Nodo del árbol rojinegro para los jugadores"""
    def __init__(self, id_elemento, dato1, dato2, nombre):
        self.id = id_elemento
        self.dato1 = dato1
        self.dato2 = dato2
        self.nombre = nombre
        self.color = 'R'  # 'R' para rojo, 'B' para negro
        self.izq = None
        self.der = None
        self.padre = None
    
    def __str__(self):
        return f"Jugador(ID: {self.id}, Nombre: {self.nombre}, Edad: {self.dato1}, Rendimiento: {self.dato2}, Color: {self.color})"


class ArbolRojiNegro:
    """Árbol Rojinegro base con operaciones de inserción y balanceo"""
    def __init__(self):
        self.NIL = NodoRB(None, None, None, None)
        self.NIL.color = 'B'
        self.raiz = self.NIL

    def rotar_izquierda(self, x):
        """Rotación izquierda para balance del árbol"""
        y = x.der
        x.der = y.izq
        if y.izq != self.NIL:
            y.izq.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.izq:
            x.padre.izq = y
        else:
            x.padre.der = y
        y.izq = x
        x.padre = y

    def rotar_derecha(self, x):
        """Rotación derecha para balance del árbol"""
        y = x.izq
        x.izq = y.der
        if y.der != self.NIL:
            y.der.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.der:
            x.padre.der = y
        else:
            x.padre.izq = y
        y.der = x
        x.padre = y

    def insertar_fixup(self, z):
        """Corrige propiedades del árbol después de insertar"""
        while z.padre and z.padre.color == 'R':
            if z.padre == z.padre.padre.izq:
                y = z.padre.padre.der
                if y and y.color == 'R':
                    z.padre.color = 'B'
                    y.color = 'B'
                    z.padre.padre.color = 'R'
                    z = z.padre.padre
                else:
                    if z == z.padre.der:
                        z = z.padre
                        self.rotar_izquierda(z)
                    z.padre.color = 'B'
                    z.padre.padre.color = 'R'
                    self.rotar_derecha(z.padre.padre)
            else:
                y = z.padre.padre.izq
                if y and y.color == 'R':
                    z.padre.color = 'B'
                    y.color = 'B'
                    z.padre.padre.color = 'R'
                    z = z.padre.padre
                else:
                    if z == z.padre.izq:
                        z = z.padre
                        self.rotar_derecha(z)
                    z.padre.color = 'B'
                    z.padre.padre.color = 'R'
                    self.rotar_izquierda(z.padre.padre)
        self.raiz.color = 'B'


# ========================================================================================
# JUGADORES
# Se crea una clase ArbolJugadores que extiende de ArbolRojiNegro 
# En este caso no se crea un nodo especial porque los datos ya están en NodoRB
# ========================================================================================

class ArbolJugadores(ArbolRojiNegro):
    """
    Árbol que ordena jugadores por:
    1. dato2 (rendimiento) ASCENDENTE
    2. dato1 (edad) DESCENDENTE
    3. id ASCENDENTE
    """
    def insertar(self, jugador):
        """Inserta un jugador como NodoRB"""
        nodo = NodoRB(
            jugador['id'],
            jugador['edad'],      # dato1 = edad
            jugador['rendimiento'], # dato2 = rendimiento
            jugador['nombre']
        )
        nodo.izq = self.NIL
        nodo.der = self.NIL
        nodo.padre = None

        y = None
        x = self.raiz

        while x != self.NIL:
            y = x

            if (nodo.dato2 < x.dato2 or 
                (nodo.dato2 == x.dato2 and nodo.dato1 > x.dato1) or
                (nodo.dato2 == x.dato2 and nodo.dato1 == x.dato1 and nodo.id < x.id)):
                x = x.izq
            else:
                x = x.der

        nodo.padre = y
        if y is None:
            self.raiz = nodo
        elif (nodo.dato2 < y.dato2 or 
              (nodo.dato2 == y.dato2 and nodo.dato1 > y.dato1) or
              (nodo.dato2 == y.dato2 and nodo.dato1 == y.dato1 and nodo.id < y.id)):
            y.izq = nodo
        else:
            y.der = nodo

        nodo.color = 'R'
        self.insertar_fixup(nodo)

    def recorrido_inorden(self, nodo, resultado):
        """Recorrido in-orden: devuelve jugadores ordenados"""
        if nodo != self.NIL:
            self.recorrido_inorden(nodo.izq, resultado)
            resultado.append(nodo)
            self.recorrido_inorden(nodo.der, resultado)

# ========================================================================================
# Equipos
# Se crea una clase NodoEquipoRB para equipos, que hereda de NodoRB
# y se crea un arbol especial para equipos que hereda de ArbolRojiNegro
# ========================================================================================

class NodoEquipoRB(NodoRB):
    """
    Nodo especial para equipos que extiende NodoRB.
    """
    def __init__(self, nombre_deporte, promedio_rendimiento, cantidad_jugadores, jugadores_ordenados):
        super().__init__(
            id_elemento=None,
            dato1=promedio_rendimiento, 
            dato2=cantidad_jugadores,    
            nombre=nombre_deporte
        )
        self.promedio_rendimiento = promedio_rendimiento
        self.cantidad_jugadores = cantidad_jugadores
        self.jugadores = jugadores_ordenados 

class ArbolEquipos(ArbolRojiNegro):
    """
    Árbol que ordena equipos en orden 
    """
    def __init__(self):
        super().__init__()
        self.NIL = NodoEquipoRB(None, 0, 0, None)
        self.NIL.color = 'B'
        self.raiz = self.NIL

    def insertar(self, nodo_equipo):
        nodo_equipo.izq = self.NIL
        nodo_equipo.der = self.NIL
        nodo_equipo.padre = None
        y = None
        x = self.raiz

        while x != self.NIL:
            y = x
            """El orden de los equipos es en funcion al enunciado "los equipos se ordenan ascendentemente por promedio de rendimiento,
            en caso de empate, descendentemente por cantidad de jugadores,"""
            if (nodo_equipo.dato1 < x.dato1 or
                (nodo_equipo.dato1 == x.dato1 and nodo_equipo.dato2 > x.dato2) or
                (nodo_equipo.dato1 == x.dato1 and nodo_equipo.dato2 == x.dato2 and nodo_equipo.nombre < x.nombre)):
                x = x.izq
            else:
                x = x.der

        nodo_equipo.padre = y
        if y is None:
            self.raiz = nodo_equipo
        elif (nodo_equipo.dato1 < y.dato1 or
              (nodo_equipo.dato1 == y.dato1 and nodo_equipo.dato2 > y.dato2) or
              (nodo_equipo.dato1 == y.dato1 and nodo_equipo.dato2 == y.dato2 and nodo_equipo.nombre < y.nombre)):
            y.izq = nodo_equipo
        else:
            y.der = nodo_equipo

        nodo_equipo.color = 'R'
        self.insertar_fixup(nodo_equipo)

    def recorrido_inorden(self, nodo, resultado):
        """Recorrido in-orden: devuelve equipos ordenados de acuerdo a los criterios"""
        if nodo != self.NIL:
            self.recorrido_inorden(nodo.izq, resultado)
            resultado.append(nodo)
            self.recorrido_inorden(nodo.der, resultado)


# ========================================================================================
# FUNCIONES AUXILIARES
# ========================================================================================

def construir_arbol_jugadores(lista_jugadores):
    """Construye árbol de jugadores y devuelve nodos ordenados"""
    arbol = ArbolJugadores()
    for j in lista_jugadores:
        arbol.insertar(j)
    
    resultado = []
    arbol.recorrido_inorden(arbol.raiz, resultado)
    return resultado


def crear_equipo(nombre_deporte, jugadores_dict, ids_jugadores):
    """
    Crea un NodoEquipoRB con jugadores ordenados.
    Similar a cómo se crean los NodoPreguntaRB en alternativa_uno.py
    """

    jugadores_equipo = [jugadores_dict[id] for id in ids_jugadores]
    
    jugadores_ordenados = construir_arbol_jugadores(jugadores_equipo)
    
    suma_rendimientos = sum(j.dato2 for j in jugadores_ordenados)  # dato2 = rendimiento
    promedio = suma_rendimientos / len(jugadores_ordenados)
    
    nodo_equipo = NodoEquipoRB(
        nombre_deporte,
        promedio,
        len(jugadores_ordenados),
        jugadores_ordenados
    )
    
    return nodo_equipo

# ============================================
# FUNCIONES PARA PROBAR
# ============================================

# Nueva función para ejecutar prueba desde archivo de input, para que se parezca a la salida esperada
def ejecutar_prueba_desde_input(path):
    jugadores_data, equipos_objs = cargar_desde_archivo(path)
    
    jugadores_dict_global = {j["id"]: j for j in jugadores_data}

    arbol_eq = ArbolEquipos()
    for eq in equipos_objs:
        ids_globales = []
        tmp_dict = {}
        for j in eq.jugadores:
            id_global = next((jd["id"] for jd in jugadores_data if jd["nombre"] == j.nombre), None)
            if id_global:
                ids_globales.append(id_global)
                tmp_dict[id_global] = jugadores_dict_global[id_global]
        
        nodo_eq = crear_equipo(eq.deporte, tmp_dict, ids_globales)
        arbol_eq.insertar(nodo_eq)

    equipos_ordenados = []
    arbol_eq.recorrido_inorden(arbol_eq.raiz, equipos_ordenados)
    for equipo in equipos_ordenados:
        print(f"\n{equipo.nombre}, Rendimiento: {equipo.promedio_rendimiento}")
        jugador_ids = [j.id for j in equipo.jugadores]
        print("{" + ", ".join(map(str, jugador_ids)) + "}")

    ranking_jugadores = [node.id for node in construir_arbol_jugadores(jugadores_data)]
    print("\n{" + ", ".join(map(str, ranking_jugadores)) + "}")
