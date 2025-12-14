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


def cargar_desde_archivo(path):
    ns = {"Jugador": Jugador, "Equipo": Equipo}
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()
    exec(code, ns)

    jugadores = [v for v in ns.values() if isinstance(v, Jugador)]
    equipos = [v for v in ns.values() if isinstance(v, Equipo)]

    jug_dicts = []
    for idx, j in enumerate(jugadores, 1):
        jug_dicts.append({
            "id": idx,
            "nombre": j.nombre,
            "edad": j.edad,
            "rendimiento": j.rendimiento,
        })

    return jug_dicts, equipos