import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox


jugadores = [
    {"nombre": "Juan", "puntos": 15, "rebotes": 7, "asistencias": 4, "robos": 2, "bloqueos": 1},
    {"nombre": "Pedro", "puntos": 10, "rebotes": 5, "asistencias": 7, "robos": 1, "bloqueos": 0},
    {"nombre": "Luis", "puntos": 20, "rebotes": 10, "asistencias": 2, "robos": 3, "bloqueos": 2},
    {"nombre": "Carlos", "puntos": 8, "rebotes": 3, "asistencias": 1, "robos": 0, "bloqueos": 1},
    {"nombre": "Miguel", "puntos": 18, "rebotes": 6, "asistencias": 5, "robos": 2, "bloqueos": 1},
    {"nombre": "Sergio", "puntos": 12, "rebotes": 8, "asistencias": 3, "robos": 1, "bloqueos": 2},
    {"nombre": "David", "puntos": 25, "rebotes": 11, "asistencias": 6, "robos": 4, "bloqueos": 3},
    {"nombre": "Javier", "puntos": 9, "rebotes": 4, "asistencias": 8, "robos": 2, "bloqueos": 0},
    {"nombre": "Andrés", "puntos": 14, "rebotes": 9, "asistencias": 2, "robos": 1, "bloqueos": 2},
    {"nombre": "Raúl", "puntos": 17, "rebotes": 5, "asistencias": 7, "robos": 3, "bloqueos": 1},
    {"nombre": "Álvaro", "puntos": 11, "rebotes": 6, "asistencias": 4, "robos": 2, "bloqueos": 1},
    {"nombre": "Fernando", "puntos": 22, "rebotes": 12, "asistencias": 3, "robos": 2, "bloqueos": 4}
]


estadisticas = ["puntos", "rebotes", "asistencias", "robos", "bloqueos"]

jugador_actual = None
widgets = []

fig = plt.figure(figsize=(12, 7))
fig.canvas.manager.set_window_title("Gestión visual de baloncesto")


def limpiar_pantalla():
    global widgets
    fig.clear()
    widgets = []


def crear_boton(posicion, texto, funcion):
    ax = fig.add_axes(posicion)
    boton = Button(ax, texto)
    boton.on_clicked(funcion)
    widgets.append(boton)
    return boton


def buscar_jugador(nombre):
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            return jugador
    return None


# -------------------------------------------------
# PANTALLA INICIAL
# -------------------------------------------------

def pantalla_inicio():

    limpiar_pantalla()

    fig.suptitle(
        "ELIGE UN JUGADOR",
        fontsize=20,
        fontweight="bold"
    )

    y = 0.80

    for jugador in jugadores:

        crear_boton(
            [0.38, y, 0.24, 0.045],
            jugador["nombre"],
            lambda event, nombre=jugador["nombre"]: seleccionar_jugador(nombre)
        )

        y -= 0.055

    plt.draw()


# -------------------------------------------------
# SELECCIONAR JUGADOR
# -------------------------------------------------

def seleccionar_jugador(nombre):

    global jugador_actual

    jugador_actual = buscar_jugador(nombre)

    pantalla_menu_jugador()

#pantalla grafico
def pantalla_grafico():

    limpiar_pantalla()

    fig.suptitle(
        f"GRÁFICO DE {jugador_actual['nombre']}",
        fontsize=18,
        fontweight="bold"
    )

    estadisticas_jugador = [
        jugador_actual["puntos"],
        jugador_actual["rebotes"],
        jugador_actual["asistencias"],
        jugador_actual["robos"],
        jugador_actual["bloqueos"]
    ]

    nombres = [
        "Puntos",
        "Rebotes",
        "Asistencias",
        "Robos",
        "Bloqueos"
    ]

    ax = fig.add_axes([0.10, 0.20, 0.80, 0.60])

    ax.bar(
        nombres,
        estadisticas_jugador
    )

    ax.set_ylabel("Valor")

    ax.set_title(
        f"Estadísticas de {jugador_actual['nombre']}"
    )

    crear_boton(
        [0.38, 0.05, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()

# -------------------------------------------------
# MENÚ DEL JUGADOR
# -------------------------------------------------

def pantalla_menu_jugador():

    limpiar_pantalla()

    fig.suptitle(
        f"JUGADOR: {jugador_actual['nombre']}",
        fontsize=18,
        fontweight="bold"
    )

    ax = fig.add_axes([0.08, 0.22, 0.35, 0.55])

    ax.axis("off")

    texto = (
        f"ESTADÍSTICAS\n\n"
        f"Puntos: {jugador_actual['puntos']}\n\n"
        f"Rebotes: {jugador_actual['rebotes']}\n\n"
        f"Asistencias: {jugador_actual['asistencias']}\n\n"
        f"Robos: {jugador_actual['robos']}\n\n"
        f"Bloqueos: {jugador_actual['bloqueos']}"
    )

    ax.text(
        0,
        1,
        texto,
        fontsize=14,
        va="top"
    )

    crear_boton(
        [0.55, 0.70, 0.28, 0.08],
        "Actualizar estadísticas",
        lambda event: pantalla_actualizar()
    )

    crear_boton(
        [0.55, 0.58, 0.28, 0.08],
        "Mejor jugador",
        lambda event: pantalla_mejor_jugador()
    )

    crear_boton(
        [0.55, 0.46, 0.28, 0.08],
        "Ordenar jugadores",
        lambda event: pantalla_ordenar()
    )

    crear_boton(
        [0.55, 0.34, 0.28, 0.08],
        "Analizar equipo",
        lambda event: pantalla_analisis()
    )

    crear_boton(
        [0.55, 0.22, 0.28, 0.08],
        "Ver todos",
        lambda event: pantalla_todos()
    )

    crear_boton(
        [0.55, 0.12, 0.28, 0.08],
        "Ver gráfico",
        lambda event: pantalla_grafico()
    )

    crear_boton(
        [0.55, 0.02, 0.28, 0.08],
        "Crear jugador",
        lambda event: pantalla_crear_jugador()
    )

    crear_boton(
        [0.55, -0.08, 0.28, 0.08],
        "Eliminar jugador",
        lambda event: pantalla_eliminar_jugador()
    )

    crear_boton(
        [0.55, -0.18, 0.28, 0.08],
        "Cambiar jugador",
        lambda event: pantalla_inicio()
    )

    plt.draw()

# -------------------------------------------------
# ACTUALIZAR ESTADÍSTICAS
# -------------------------------------------------

def pantalla_actualizar():

    limpiar_pantalla()

    fig.suptitle(
        f"Actualizar estadísticas de {jugador_actual['nombre']}",
        fontsize=18,
        fontweight="bold"
    )

    ax = fig.add_axes([0.12, 0.60, 0.75, 0.20])
    ax.axis("off")

    ax.text(
        0,
        1,
        "Escribe la estadística y el nuevo valor",
        fontsize=14,
        va="top"
    )

    ax_est = fig.add_axes([0.20, 0.42, 0.30, 0.07])
    caja_est = TextBox(ax_est, "Estadística: ", initial="puntos")
    widgets.append(caja_est)

    ax_val = fig.add_axes([0.20, 0.30, 0.30, 0.07])
    caja_val = TextBox(ax_val, "Nuevo valor: ", initial="0")
    widgets.append(caja_val)

    ax_resultado = fig.add_axes([0.20, 0.15, 0.55, 0.08])
    ax_resultado.axis("off")

    def actualizar(event):

        estadistica = caja_est.text.lower()
        valor = caja_val.text

        ax_resultado.clear()
        ax_resultado.axis("off")

        if estadistica not in estadisticas:

            ax_resultado.text(
                0,
                0.8,
                "Esa estadística no existe",
                fontsize=12
            )

        elif not valor.isdigit():

            ax_resultado.text(
                0,
                0.8,
                "El valor debe ser numérico",
                fontsize=12
            )

        else:

            jugador_actual[estadistica] = int(valor)

            ax_resultado.text(
                0,
                0.8,
                "Estadística actualizada correctamente",
                fontsize=12
            )

        plt.draw()

    crear_boton(
        [0.58, 0.35, 0.18, 0.08],
        "Actualizar",
        actualizar
    )

    crear_boton(
        [0.35, 0.04, 0.25, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


# -------------------------------------------------
# MEJOR JUGADOR
# -------------------------------------------------

def pantalla_mejor_jugador():

    limpiar_pantalla()

    fig.suptitle(
        "MEJOR JUGADOR",
        fontsize=18,
        fontweight="bold"
    )

    ax = fig.add_axes([0.15, 0.68, 0.7, 0.12])
    ax.axis("off")

    ax.text(
        0.5,
        0.5,
        "Selecciona una estadística",
        fontsize=14,
        ha="center"
    )

    y = 0.52

    for estadistica in estadisticas:

        crear_boton(
            [0.38, y, 0.24, 0.07],
            estadistica,
            lambda event, est=estadistica: mostrar_mejor(est)
        )

        y -= 0.09

    crear_boton(
        [0.38, 0.08, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


def mostrar_mejor(estadistica):

    limpiar_pantalla()

    mejor = max(jugadores, key=lambda j: j[estadistica])

    fig.suptitle(
        f"Mejor jugador en {estadistica}",
        fontsize=18,
        fontweight="bold"
    )

    ax = fig.add_axes([0.20, 0.30, 0.60, 0.40])
    ax.axis("off")

    ax.text(
        0.5,
        0.5,
        f"{mejor['nombre']}\n\n{estadistica}: {mejor[estadistica]}",
        fontsize=20,
        ha="center",
        va="center"
    )

    crear_boton(
        [0.38, 0.10, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


# -------------------------------------------------
# ORDENAR JUGADORES
# -------------------------------------------------

def pantalla_ordenar():

    limpiar_pantalla()

    fig.suptitle(
        "ORDENAR JUGADORES",
        fontsize=18,
        fontweight="bold"
    )

    ax = fig.add_axes([0.15, 0.68, 0.7, 0.12])
    ax.axis("off")

    ax.text(
        0.5,
        0.5,
        "Selecciona una estadística",
        fontsize=14,
        ha="center"
    )

    y = 0.52

    for estadistica in estadisticas:

        crear_boton(
            [0.38, y, 0.24, 0.07],
            estadistica,
            lambda event, est=estadistica: mostrar_ordenados(est)
        )

        y -= 0.09

    crear_boton(
        [0.38, 0.08, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


def mostrar_ordenados(estadistica):

    limpiar_pantalla()

    fig.suptitle(
        f"Jugadores ordenados por {estadistica}",
        fontsize=18,
        fontweight="bold"
    )

    lista = sorted(
        jugadores,
        key=lambda j: j[estadistica],
        reverse=True
    )

    ax = fig.add_axes([0.20, 0.18, 0.60, 0.65])
    ax.axis("off")

    columnas = ["Posición", "Jugador", estadistica]

    datos = []

    for i, jugador in enumerate(lista, start=1):

        datos.append([
            i,
            jugador["nombre"],
            jugador[estadistica]
        ])

    tabla = ax.table(
        cellText=datos,
        colLabels=columnas,
        cellLoc="center",
        loc="center"
    )

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(12)
    tabla.scale(1, 1.6)

    crear_boton(
        [0.38, 0.06, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


# -------------------------------------------------
# ANÁLISIS
# -------------------------------------------------

def pantalla_analisis():

    limpiar_pantalla()

    fig.suptitle(
        "ANÁLISIS DEL EQUIPO",
        fontsize=18,
        fontweight="bold"
    )

    total_puntos = sum(j["puntos"] for j in jugadores)
    promedio = total_puntos / len(jugadores)

    total_rebotes = sum(j["rebotes"] for j in jugadores)
    total_asistencias = sum(j["asistencias"] for j in jugadores)

    ax = fig.add_axes([0.20, 0.25, 0.60, 0.50])
    ax.axis("off")

    texto = (
        f"Total de puntos: {total_puntos}\n\n"
        f"Promedio de puntos: {round(promedio, 2)}\n\n"
        f"Total de rebotes: {total_rebotes}\n\n"
        f"Total de asistencias: {total_asistencias}"
    )

    ax.text(
        0.5,
        0.5,
        texto,
        fontsize=16,
        ha="center",
        va="center"
    )

    crear_boton(
        [0.38, 0.08, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


# -------------------------------------------------
# TODOS LOS JUGADORES
# -------------------------------------------------

def pantalla_todos():

    limpiar_pantalla()

    fig.suptitle(
        "TODOS LOS JUGADORES",
        fontsize=18,
        fontweight="bold"
    )

    ax = fig.add_axes([0.08, 0.18, 0.84, 0.68])
    ax.axis("off")

    columnas = [
        "Nombre",
        "Puntos",
        "Rebotes",
        "Asistencias",
        "Robos",
        "Bloqueos"
    ]

    datos = []

    for jugador in jugadores:

        datos.append([
            jugador["nombre"],
            jugador["puntos"],
            jugador["rebotes"],
            jugador["asistencias"],
            jugador["robos"],
            jugador["bloqueos"]
        ])

    tabla = ax.table(
        cellText=datos,
        colLabels=columnas,
        cellLoc="center",
        loc="center"
    )

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(11)
    tabla.scale(1, 1.5)

    crear_boton(
        [0.38, 0.06, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )
    plt.draw()
def pantalla_crear_jugador():

    limpiar_pantalla()

    fig.suptitle(
        "CREAR NUEVO JUGADOR",
        fontsize=18,
        fontweight="bold"
    )

    cajas = {}

    campos = [
        "nombre",
        "puntos",
        "rebotes",
        "asistencias",
        "robos",
        "bloqueos"
    ]

    y = 0.72

    for campo in campos:

        ax_caja = fig.add_axes([0.35, y, 0.30, 0.06])

        caja = TextBox(
            ax_caja,
            campo.capitalize() + ": "
        )

        cajas[campo] = caja

        widgets.append(caja)

        y -= 0.09

    ax_resultado = fig.add_axes([0.20, 0.12, 0.60, 0.08])

    ax_resultado.axis("off")

    def crear(event):

        ax_resultado.clear()

        ax_resultado.axis("off")

        nombre = cajas["nombre"].text.strip()

        if nombre == "":

            ax_resultado.text(
                0.5,
                0.5,
                "Debes escribir un nombre",
                fontsize=12,
                ha="center",
                va="center"
            )

        elif buscar_jugador(nombre) is not None:

            ax_resultado.text(
                0.5,
                0.5,
                "Ese jugador ya existe",
                fontsize=12,
                ha="center",
                va="center"
            )

        else:

            nuevo_jugador = {
                "nombre": nombre
            }

            correcto = True

            for estadistica in estadisticas:

                valor = cajas[estadistica].text.strip()

                if not valor.isdigit():

                    correcto = False

                else:

                    nuevo_jugador[estadistica] = int(valor)

            if correcto:

                jugadores.append(nuevo_jugador)

                ax_resultado.text(
                    0.5,
                    0.5,
                    "Jugador creado correctamente",
                    fontsize=12,
                    ha="center",
                    va="center"
                )

            else:

                ax_resultado.text(
                    0.5,
                    0.5,
                    "Las estadísticas deben ser números",
                    fontsize=12,
                    ha="center",
                    va="center"
                )

        plt.draw()

    crear_boton(
        [0.25, 0.04, 0.20, 0.07],
        "Crear",
        crear
    )

    crear_boton(
        [0.55, 0.04, 0.20, 0.07],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


def pantalla_eliminar_jugador():

    limpiar_pantalla()

    fig.suptitle(
        "ELIMINAR JUGADOR",
        fontsize=18,
        fontweight="bold"
    )

    ax = fig.add_axes([0.15, 0.78, 0.70, 0.10])

    ax.axis("off")

    ax.text(
        0.5,
        0.5,
        "Selecciona el jugador que quieres eliminar",
        fontsize=14,
        ha="center",
        va="center"
    )

    y = 0.68

    for jugador in jugadores:

        crear_boton(
            [0.38, y, 0.24, 0.045],
            jugador["nombre"],
            lambda event, nombre=jugador["nombre"]: pantalla_confirmar_eliminar(nombre)
        )

        y -= 0.055

    crear_boton(
        [0.38, 0.04, 0.24, 0.07],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


def pantalla_confirmar_eliminar(nombre):

    limpiar_pantalla()

    fig.suptitle(
        "CONFIRMAR ELIMINACIÓN",
        fontsize=18,
        fontweight="bold"
    )

    ax = fig.add_axes([0.20, 0.35, 0.60, 0.30])

    ax.axis("off")

    ax.text(
        0.5,
        0.5,
        f"¿Seguro que quieres eliminar a {nombre}?",
        fontsize=16,
        ha="center",
        va="center"
    )

    def eliminar(event):

        global jugador_actual

        jugador = buscar_jugador(nombre)

        if jugador is not None:

            jugadores.remove(jugador)

            if jugador_actual == jugador:

                jugador_actual = None

        pantalla_inicio()

    crear_boton(
        [0.25, 0.18, 0.20, 0.08],
        "Sí, eliminar",
        eliminar
    )

    crear_boton(
        [0.55, 0.18, 0.20, 0.08],
        "Cancelar",
        lambda event: pantalla_eliminar_jugador()
    )
    plt.draw()

pantalla_inicio()

plt.show()



# Mostrar todos los jugadores en formato tabla
def mostrar_tabla_jugadores():
    print("ESTADÍSTICAS DEL EQUIPO")
    print(f"{'Nombre':<12}{'Puntos':<10}{'Rebotes':<12}{'Asistencias':<15}{'Robos':<10}{'Bloqueos':<12}")
    print("-" * 70)

    for jugador in jugadores:
        print(f"{jugador['nombre']:<12}"
              f"{jugador['puntos']:<10}"
              f"{jugador['rebotes']:<12}"
              f"{jugador['asistencias']:<15}"
              f"{jugador['robos']:<10}"
              f"{jugador['bloqueos']:<12}")

respuesta_tabla = input("¿Quieres mostrar todos los jugadores en tabla? (si/no): ").lower()
if respuesta_tabla == "si":
    mostrar_tabla_jugadores()
else: 
    print("No se mostrará la tabla.")



# Calcular promedio de cualquier estadística
def promedio_cualquier_estadistica():
    estadistica = elegir_estadistica()
    if estadistica is None:
        return
    total = 0
    for jugador in jugadores:
        total += jugador[estadistica]
    promedio = total / len(jugadores)
    print(f"Promedio de {estadistica}: {promedio:.2f}")

respuesta_promedio2 = input("¿Quieres calcular el promedio de alguna estadística? (si/no): ").lower()
if respuesta_promedio2 == "si": 
    promedio_cualquier_estadistica()
else:
    print("No se calculará ningún promedio.")
