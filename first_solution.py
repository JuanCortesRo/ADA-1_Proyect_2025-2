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
    Árbol que ordena jugadores por su rendimiento de forma ascendente
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
# SEDES
# Se crea una clase NodoSedeRB para sedes, que hereda de NodoRB
# y se crea un arbol especial para sedes que hereda de ArbolRojiNegro
# ========================================================================================

class NodoSedeRB(NodoRB):
    """
    Nodo especial para sedes que extiende NodoRB.
    Almacena información de la sede y un árbol de equipos ordenado
    """
    def __init__(self, nombre_sede, promedio_rendimiento, total_jugadores, arbol_equipos):
        super().__init__(
            id_elemento=None,
            dato1=promedio_rendimiento,   # Para comparación
            dato2=total_jugadores,        # Para desempate
            nombre=nombre_sede
        )
        self.promedio_rendimiento = promedio_rendimiento
        self.total_jugadores = total_jugadores
        self.arbol_equipos = arbol_equipos  # ArbolEquipos con los equipos de la sede


class ArbolSedes(ArbolRojiNegro):
    """
    Árbol que ordena sedes por:
    """
    def __init__(self):
        super().__init__()
        self.NIL = NodoRB(None, 0, 0, None)
        self.NIL.color = 'B'
        self.raiz = self.NIL

    def insertar(self, nodo_sede):
        """Inserta un NodoSedeRB en el árbol"""
        nodo_sede.izq = self.NIL
        nodo_sede.der = self.NIL
        nodo_sede.padre = None
        
        y = None
        x = self.raiz

        while x != self.NIL:
            y = x
            # Orden: promedio ASC -> total_jugadores DESC -> nombre ASC
            if (nodo_sede.dato1 < x.dato1 or
                (nodo_sede.dato1 == x.dato1 and nodo_sede.dato2 > x.dato2) or
                (nodo_sede.dato1 == x.dato1 and nodo_sede.dato2 == x.dato2 and nodo_sede.nombre < x.nombre)):
                x = x.izq
            else:
                x = x.der

        nodo_sede.padre = y
        if y is None:
            self.raiz = nodo_sede
        elif (nodo_sede.dato1 < y.dato1 or
              (nodo_sede.dato1 == y.dato1 and nodo_sede.dato2 > y.dato2) or
              (nodo_sede.dato1 == y.dato1 and nodo_sede.dato2 == y.dato2 and nodo_sede.nombre < y.nombre)):
            y.izq = nodo_sede
        else:
            y.der = nodo_sede

        nodo_sede.color = 'R'
        self.insertar_fixup(nodo_sede)

    def recorrido_inorden(self, nodo, resultado):
        """Recorrido in-orden: devuelve sedes ordenadas"""
        if nodo != self.NIL:
            self.recorrido_inorden(nodo.izq, resultado)
            resultado.append(nodo)
            self.recorrido_inorden(nodo.der, resultado)

# ========================================================================================
# FUNCIONES PARA ESTADÍSTICAS
# ========================================================================================
def encontrar_equipo_mayor_menor_rendimiento(sedes_ordenadas):
    """
    Encuentra los equipos con mayor y menor rendimiento de todas las sedes.
    Retorna el par ordenado (equipo, sede) para mayor y menor rendimiento.
    """
    if not sedes_ordenadas:
        return None, None
    
    equipo_mayor = None
    sede_mayor = None
    rendimiento_mayor = -1
    
    equipo_menor = None
    sede_menor = None
    rendimiento_menor = float('inf')
    
    # Recorrer todas las sedes y sus equipos
    for sede in sedes_ordenadas:
        equipos_ordenados = []
        sede.arbol_equipos.recorrido_inorden(sede.arbol_equipos.raiz, equipos_ordenados)
        
        for equipo in equipos_ordenados:
            # Actualizar mayor rendimiento
            if equipo.promedio_rendimiento > rendimiento_mayor:
                rendimiento_mayor = equipo.promedio_rendimiento
                equipo_mayor = equipo
                sede_mayor = sede
            
            # Actualizar menor rendimiento
            if equipo.promedio_rendimiento < rendimiento_menor:
                rendimiento_menor = equipo.promedio_rendimiento
                equipo_menor = equipo
                sede_menor = sede
    
    return (equipo_mayor, sede_mayor), (equipo_menor, sede_menor)

def encontrar_jugador_mayor_menor_rendimiento(jugadores_ordenados):
    """
    Encuentra los jugadores con mayor y menor rendimiento.
    Los jugadores ya están ordenados ascendentemente por rendimiento.
    """
    if not jugadores_ordenados:
        return None, None
    
    #quien tenga el menor rendimiento estará de primero
    jugador_menor = jugadores_ordenados[0]
    #quien tenga el mayor rendimiento estará al final
    jugador_mayor = jugadores_ordenados[-1]
    
    return jugador_mayor, jugador_menor

def encontrar_jugador_mas_joven_veterano(jugadores_data):
    """
    Encuentra el jugador más joven (menor edad) y más veterano (mayor edad).
    """
    if not jugadores_data:
        return None, None
    
    mas_joven = min(jugadores_data, key=lambda j: (j['edad'], j['id']))
    mas_veterano = max(jugadores_data, key=lambda j: (j['edad'], -j['id']))
    
    return mas_joven, mas_veterano

def calcular_promedio_edad_rendimiento(jugadores_data):
    """
    Calcula el promedio de edad y rendimiento de todos los jugadores.
    """
    if not jugadores_data:
        return 0, 0
    
    suma_edades = sum(j['edad'] for j in jugadores_data)
    suma_rendimientos = sum(j['rendimiento'] for j in jugadores_data)
    total = len(jugadores_data)
    
    promedio_edad = suma_edades / total
    promedio_rendimiento = suma_rendimientos / total
    
    return promedio_edad, promedio_rendimiento

def imprimir_estadisticas (jugadores_data, sedes_ordenadas, ranking_jugadores):
    """
    Imprime todas las estadísticas que nos solicita el enunciado
    """
    # Equipo con mayor y menor rendimiento
    (eq_mayor, sede_mayor), (eq_menor, sede_menor) = encontrar_equipo_mayor_menor_rendimiento(sedes_ordenadas)
    if eq_mayor:
        print(f"\nEquipo con mayor rendimiento: {eq_mayor.nombre} {sede_mayor.nombre}")
    if eq_menor:
        print(f"\nEquipo con menor rendimiento: {eq_menor.nombre} {sede_menor.nombre}")
 
    # Jugador con mayor y menor rendimiento
    jug_mayor, jug_menor = encontrar_jugador_mayor_menor_rendimiento(ranking_jugadores)
    if jug_mayor:
        print(f"\nJugador con mayor rendimiento: {{ {jug_mayor.id} , {jug_mayor.nombre} , {jug_mayor.dato2} }}")
    if jug_menor:
        print(f"\nJugador con menor rendimiento: {{ {jug_menor.id} , {jug_menor.nombre} , {jug_menor.dato2} }}")

    # Jugador más joven y más veterano
    mas_joven, mas_veterano = encontrar_jugador_mas_joven_veterano(jugadores_data)
    if mas_joven:
        print(f"\njugador mas joven: {{ {mas_joven['id']} , {mas_joven['nombre']} , {mas_joven['edad']} }}")
    if mas_veterano:
        print(f"\njugador mas veterano: {{ {mas_veterano['id']} , {mas_veterano['nombre']} , {mas_veterano['edad']} }}")
    
    # Promedios
    prom_edad, prom_rend = calcular_promedio_edad_rendimiento(jugadores_data)
    print(f"\nPromedio de edad de los jugadores: {prom_edad:.2f}")
    print(f"\nPromedio de rendimiento de los jugadores: {prom_rend:.2f}")

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

def crear_sede(nombre_sede, jugadores_dict, equipos_data):
    """
    Crea un NodoSedeRB con equipos ordenados.
    """
    arbol_equipos = ArbolEquipos()
    total_jugadores = 0
    suma_rendimientos = 0
    
    for nombre_deporte, ids_jugadores in equipos_data:
        nodo_equipo = crear_equipo(nombre_deporte, jugadores_dict, ids_jugadores)
        arbol_equipos.insertar(nodo_equipo)
        total_jugadores += nodo_equipo.cantidad_jugadores
        suma_rendimientos += nodo_equipo.promedio_rendimiento
    
    # Calcular promedio de la sede
    rendimiento_sede = suma_rendimientos 
    
    nodo_sede = NodoSedeRB(
        nombre_sede,
        rendimiento_sede,
        total_jugadores,
        arbol_equipos
    )
    
    return nodo_sede

# ============================================
# FUNCIONES PARA PROBAR
# ============================================

# Nueva función para ejecutar prueba desde archivo de input, para que se parezca a la salida esperada
def ejecutar_prueba_desde_input(path):
    #cargar datos
    jugadores_data, equipos_objs, sedes_objs = cargar_desde_archivo(path)
    #crear diccionario de los jugadores para acceder más facil
    jugadores_dict_global = {j["id"]: j for j in jugadores_data}
    #crear arbol de sedes
    arbol_sedes = ArbolSedes()
    #procesar cada sede
    for sede_obj in sedes_objs:
        equipos_data = [] 
        
        for equipo_obj in sede_obj.equipos:
            ids_jugadores = []
            
            for jugador_obj in equipo_obj.jugadores:
                id_global = next((jd["id"] for jd in jugadores_data if jd["nombre"] == jugador_obj.nombre), None)
                
                if id_global:
                    ids_jugadores.append(id_global)
                    
            equipos_data.append((equipo_obj.deporte, ids_jugadores))

        nodo_sede = crear_sede(sede_obj.nombre, jugadores_dict_global, equipos_data)
        arbol_sedes.insertar(nodo_sede)

    sedes_ordenadas = []
    arbol_sedes.recorrido_inorden(arbol_sedes.raiz, sedes_ordenadas)
    
    for sede in sedes_ordenadas:

        print(f"\n{sede.nombre}, Rendimiento: {sede.promedio_rendimiento}")
        
        equipos_ordenados = []
        sede.arbol_equipos.recorrido_inorden(sede.arbol_equipos.raiz, equipos_ordenados)
        
        for equipo in equipos_ordenados:
            print(f"\n{equipo.nombre}, Rendimiento: {equipo.promedio_rendimiento}")
            jugador_ids = [j.id for j in equipo.jugadores]
            print("{" + ", ".join(map(str, jugador_ids)) + "}")

    ranking_jugadores = construir_arbol_jugadores(jugadores_data)
    ranking_ids = [node.id for node in ranking_jugadores]
    print("{" + ", ".join(map(str, ranking_ids)) + "}")

    imprimir_estadisticas(jugadores_data, sedes_ordenadas, ranking_jugadores)
