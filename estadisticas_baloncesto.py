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


nombre_jugador = input("Introduce el nombre del jugador: ").lower().capitalize()

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

respuesta = input("\n¿Quieres actualizar estadísticas? (si/no): ").lower()

if respuesta == "si":

    estadistica = input("Qué estadística quieres actualizar: ").lower()
    valor = int(input("Nuevo valor: "))

    actualizar_estadisticas(nombre_jugador, estadistica, valor)

    print("\nEstadísticas actualizadas:\n")

    for jugador in jugadores:
        print(jugador)

else:
    print("No hay cambios en las estadísticas.")



#ii. Actualizar las Estadísticas: 
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


#iii. Calcular el Mejor Jugador: 
def mejor_jugador(estadistica):
    mejor_jugador = None
    mejor_valor = -1

    for jugador in jugadores:
        if estadistica in jugador and jugador[estadistica] > mejor_valor:
            mejor_valor = jugador[estadistica]
            mejor_jugador = jugador["nombre"]

    if mejor_jugador:
        print(f"\nEl mejor jugador en {estadistica} es {mejor_jugador} con {mejor_valor}.")
    else:
        print("Esa estadística no existe.")


estadistica_respuesta = input("\n Quieres encontrar el mejor jugador en alguna estadística? (si/no): ").lower()

if estadistica_respuesta == "si":
    
    estadistica_respuesta = input("\n En que estadistica quieres encontrar al mejor jugador? ").lower()
    mejor_jugador(estadistica_respuesta)

else:
    print("No se buscará al mejor jugador.")


def elegir_estadistica():
    estadisticas_validas = ["puntos", "rebotes", "asistencias", "robos", "bloqueos"]

    print("\nElige una estadística:")
    print("1. Puntos")
    print("2. Rebotes")
    print("3. Asistencias")
    print("4. Robos")
    print("5. Bloqueos")

    opcion = input("Introduce una opción del 1 al 5: ")

    if opcion == "1":
        return "puntos"
    elif opcion == "2":
        return "rebotes"
    elif opcion == "3":
        return "asistencias"
    elif opcion == "4":
        return "robos"
    elif opcion == "5":
        return "bloqueos"
    else:
        print("Opción no válida.")
        return None


def ordenar_jugadores():
    estadistica = elegir_estadistica()

    if estadistica is None:
        return

    jugadores_ordenados = sorted(
        jugadores,
        key=lambda jugador: jugador[estadistica],
        reverse=True
    )

    print(f"\nJugadores ordenados por {estadistica} de mayor a menor:\n")

    for posicion, jugador in enumerate(jugadores_ordenados, start=1):
        print(f"{posicion}. {jugador['nombre']} → {jugador[estadistica]} {estadistica}")


respuesta_ordenar = input("\n¿Quieres ordenar los jugadores por alguna estadística? (si/no): ").lower()

if respuesta_ordenar == "si":
    ordenar_jugadores()
else:
    print("No se ordenarán los jugadores.")


def promedio_puntos():
    total_puntos = 0

    for jugador in jugadores:
        total_puntos += jugador["puntos"]

    promedio = total_puntos / len(jugadores)

    print("\nAnálisis del rendimiento del equipo:")
    print(f"Total de puntos anotados: {total_puntos}")
    print(f"Número de jugadores: {len(jugadores)}")
    print(f"Promedio de puntos por jugador: {promedio:.2f}")

    return promedio


respuesta_promedio = input("\n¿Quieres calcular el promedio de puntos del equipo? (si/no): ").lower()

if respuesta_promedio == "si":
    promedio_puntos()
else:
    print("No se calculará el promedio de puntos.")