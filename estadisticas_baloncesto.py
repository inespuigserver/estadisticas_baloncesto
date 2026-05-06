# Utilizar estructuras de datos como listas y diccionarios para gestionar las estadísticas de un equipo de baloncesto. Los estudiantes aprenderán a almacenar,organizar y buscar información sobre jugadores y sus rendimientos durante lospartidos.
jugadores = [
    {"nombre": "Juan", "puntos": 15, "rebotes": 7, "asistencias": 4,
     "robos": 2, "bloqueos": 1},

    {"nombre": "Pedro", "puntos": 10, "rebotes": 5, "asistencias": 7,
     "robos": 1, "bloqueos": 0},

    {"nombre": "Luis", "puntos": 20, "rebotes": 10, "asistencias": 2,
     "robos": 3, "bloqueos": 2},

    {"nombre": "Carlos", "puntos": 8, "rebotes": 3, "asistencias": 1,
     "robos": 0, "bloqueos": 1},

    {"nombre": "Miguel", "puntos": 18, "rebotes": 6, "asistencias": 5,
     "robos": 2, "bloqueos": 1},

    {"nombre": "Sergio", "puntos": 12, "rebotes": 8, "asistencias": 3,
     "robos": 1, "bloqueos": 2},

    {"nombre": "David", "puntos": 25, "rebotes": 11, "asistencias": 6,
     "robos": 4, "bloqueos": 3},

    {"nombre": "Javier", "puntos": 9, "rebotes": 4, "asistencias": 8,
     "robos": 2, "bloqueos": 0},

    {"nombre": "Andrés", "puntos": 14, "rebotes": 9, "asistencias": 2,
     "robos": 1, "bloqueos": 2},

    {"nombre": "Raúl", "puntos": 17, "rebotes": 5, "asistencias": 7,
     "robos": 3, "bloqueos": 1},

    {"nombre": "Álvaro", "puntos": 11, "rebotes": 6, "asistencias": 4,
     "robos": 2, "bloqueos": 1},

    {"nombre": "Fernando", "puntos": 22, "rebotes": 12, "asistencias": 3,
     "robos": 2, "bloqueos": 4}
]

def mostrar_estadisticas(nombre):

    for jugador in jugadores:

        if jugador["nombre"].lower() == nombre.lower():

            print("\nEstadísticas del jugador:")
            print("Nombre:", jugador["nombre"])
            print("Puntos:", jugador["puntos"])
            print("Rebotes:", jugador["rebotes"])
            print("Asistencias:", jugador["asistencias"])
            print("Robos:", jugador["robos"])
            print("Bloqueos:", jugador["bloqueos"])

            return

    print("Jugador no encontrado")


nombre_jugador = input("Introduce el nombre del jugador: ")

mostrar_estadisticas(nombre_jugador)

def actualizar_estadisticas(nombre, estadistica, valor):
    for jugador in jugadores:
        if jugador["nombre"].lower() == nombre.lower():
            if estadistica in jugador:
                jugador[estadistica] = valor
                print(f"\nEstadística actualizada correctamente:")
                print(f"{jugador['nombre']} → {estadistica} = {valor}")
                return
            else:
                print("Esa estadística no existe.")
                return

    print("Jugador no encontrado.")

