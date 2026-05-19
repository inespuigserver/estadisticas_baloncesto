import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
from matplotlib.patches import Rectangle

plt.rcParams["toolbar"] = "None"
plt.rcParams["font.family"] = "Segoe UI"

# Colores estilo aplicación de baloncesto
COLOR_FONDO = "#0F1117"
COLOR_PANEL = "#181B22"
COLOR_PANEL_2 = "#212633"

COLOR_BOTON = "#F97316"
COLOR_BOTON_HOVER = "#FDBA74"

COLOR_TEXTO = "#F8FAFC"
COLOR_TEXTO_SECUNDARIO = "#CBD5E1"
COLOR_TEXTO_BOTON = "#111827"

COLOR_BORDE = "#374151"
COLOR_VERDE = "#22C55E"

COLORES_GRAFICO = {
    "Puntos": "#F97316",
    "Rebotes": "#38BDF8",
    "Asistencias": "#A78BFA",
    "Robos": "#F472B6",
    "Bloqueos": "#22C55E"
}

plt.rcParams["text.color"] = COLOR_TEXTO
plt.rcParams["axes.labelcolor"] = COLOR_TEXTO
plt.rcParams["xtick.color"] = COLOR_TEXTO_SECUNDARIO
plt.rcParams["ytick.color"] = COLOR_TEXTO_SECUNDARIO

fig = plt.figure(figsize=(12, 7))
fig.patch.set_facecolor(COLOR_FONDO)
fig.canvas.manager.set_window_title("GameStats")

jugadores = [
    {"nombre": "Juan", "posicion": "Base", "puntos": 15, "rebotes": 7, "asistencias": 4, "robos": 2, "bloqueos": 1},
    {"nombre": "Pedro", "posicion": "Escolta", "puntos": 10, "rebotes": 5, "asistencias": 7, "robos": 1, "bloqueos": 0},
    {"nombre": "Luis", "posicion": "Alero", "puntos": 20, "rebotes": 10, "asistencias": 2, "robos": 3, "bloqueos": 2},
    {"nombre": "Carlos", "posicion": "Pívot", "puntos": 8, "rebotes": 3, "asistencias": 1, "robos": 0, "bloqueos": 1},
    {"nombre": "Miguel", "posicion": "Alero", "puntos": 18, "rebotes": 6, "asistencias": 5, "robos": 2, "bloqueos": 1},
    {"nombre": "Sergio", "posicion": "Pívot", "puntos": 12, "rebotes": 8, "asistencias": 3, "robos": 1, "bloqueos": 2},
    {"nombre": "David", "posicion": "Escolta", "puntos": 25, "rebotes": 11, "asistencias": 6, "robos": 4, "bloqueos": 3},
    {"nombre": "Javier", "posicion": "Base", "puntos": 9, "rebotes": 4, "asistencias": 8, "robos": 2, "bloqueos": 0},
    {"nombre": "Andrés", "posicion": "Ala-pívot", "puntos": 14, "rebotes": 9, "asistencias": 2, "robos": 1, "bloqueos": 2},
    {"nombre": "Raúl", "posicion": "Base", "puntos": 17, "rebotes": 5, "asistencias": 7, "robos": 3, "bloqueos": 1},
    {"nombre": "Álvaro", "posicion": "Escolta", "puntos": 11, "rebotes": 6, "asistencias": 4, "robos": 2, "bloqueos": 1},
    {"nombre": "Fernando", "posicion": "Ala-pívot", "puntos": 22, "rebotes": 12, "asistencias": 3, "robos": 2, "bloqueos": 4}
]

estadisticas = ["puntos", "rebotes", "asistencias", "robos", "bloqueos"]

jugador_actual = None
widgets = []


def limpiar_pantalla():
    global widgets
    fig.clear()
    fig.patch.set_facecolor(COLOR_FONDO)
    widgets = []


def crear_boton(posicion, texto, funcion):
    ax = fig.add_axes(posicion)
    ax.set_facecolor(COLOR_FONDO)

    boton = Button(
        ax,
        texto,
        color=COLOR_BOTON,
        hovercolor=COLOR_BOTON_HOVER
    )

    boton.label.set_color(COLOR_TEXTO_BOTON)
    boton.label.set_fontsize(10)
    boton.label.set_fontweight("bold")

    for borde in ax.spines.values():
        borde.set_edgecolor(COLOR_BORDE)
        borde.set_linewidth(1.2)

    boton.on_clicked(funcion)
    widgets.append(boton)

    return boton


def crear_ax(posicion, color=COLOR_FONDO):
    ax = fig.add_axes(posicion)
    ax.set_facecolor(color)
    return ax


def crear_cabecera(titulo, subtitulo="Basketball analytics dashboard"):
    fig.text(
        0.05, 0.94,
        "GAMESTATS",
        fontsize=24,
        fontweight="bold",
        color=COLOR_BOTON,
        ha="left",
        va="center"
    )

    fig.text(
        0.05, 0.90,
        subtitulo,
        fontsize=11,
        color=COLOR_TEXTO_SECUNDARIO,
        ha="left",
        va="center"
    )

    fig.text(
        0.95, 0.94,
        titulo.upper(),
        fontsize=18,
        fontweight="bold",
        color=COLOR_TEXTO,
        ha="right",
        va="center"
    )

    fig.add_artist(
        Rectangle(
            (0.05, 0.865),
            0.90,
            0.002,
            transform=fig.transFigure,
            color=COLOR_BORDE,
            linewidth=0
        )
    )


def crear_tarjeta(posicion, titulo, valor, color_acento):
    ax = fig.add_axes(posicion)

    ax.set_facecolor(COLOR_PANEL)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])

    for borde in ax.spines.values():
        borde.set_edgecolor(COLOR_BORDE)
        borde.set_linewidth(1.4)

    ax.add_patch(
        Rectangle(
            (0, 0.88),
            1,
            0.12,
            transform=ax.transAxes,
            color=color_acento,
            linewidth=0
        )
    )

    ax.text(
        0.08, 0.65,
        titulo.upper(),
        fontsize=10,
        fontweight="bold",
        color=COLOR_TEXTO_SECUNDARIO,
        ha="left",
        va="center"
    )

    ax.text(
        0.08, 0.30,
        str(valor),
        fontsize=28,
        fontweight="bold",
        color=COLOR_TEXTO,
        ha="left",
        va="center"
    )

    return ax


def buscar_jugador(nombre):
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            return jugador
    return None


def pantalla_inicio():

    limpiar_pantalla()

    crear_cabecera(
        "Elige un jugador",
        "Selecciona un jugador para consultar sus estadísticas"
    )

    col_izq_x = 0.22
    col_der_x = 0.58
    y_inicio = 0.66
    alto_boton = 0.055
    separacion = 0.065

    for i, jugador in enumerate(jugadores):

        col_x = col_izq_x if i % 2 == 0 else col_der_x
        fila = i // 2
        y = y_inicio - fila * separacion

        crear_boton(
            [col_x, y, 0.20, alto_boton],
            jugador["nombre"],
            lambda event, nombre=jugador["nombre"]: seleccionar_jugador(nombre)
        )

    plt.draw()


def seleccionar_jugador(nombre):

    global jugador_actual

    jugador_actual = buscar_jugador(nombre)

    pantalla_menu_jugador()


def pantalla_grafico():

    limpiar_pantalla()

    crear_cabecera(
        f"Gráfico de {jugador_actual['nombre']}",
        "Comparativa visual de estadísticas individuales"
    )

    estadisticas_jugador = [
        jugador_actual["puntos"],
        jugador_actual["rebotes"],
        jugador_actual["asistencias"],
        jugador_actual["robos"],
        jugador_actual["bloqueos"]
    ]

    nombres = ["Puntos", "Rebotes", "Asistencias", "Robos", "Bloqueos"]

    colores = [
        COLORES_GRAFICO["Puntos"],
        COLORES_GRAFICO["Rebotes"],
        COLORES_GRAFICO["Asistencias"],
        COLORES_GRAFICO["Robos"],
        COLORES_GRAFICO["Bloqueos"]
    ]

    ax = fig.add_axes([0.10, 0.20, 0.80, 0.58])
    ax.set_facecolor(COLOR_PANEL)

    barras = ax.bar(nombres, estadisticas_jugador, color=colores)

    ax.set_ylabel("Valor", color=COLOR_TEXTO)
    ax.set_title(
        f"Estadísticas de {jugador_actual['nombre']}",
        color=COLOR_TEXTO,
        fontsize=15,
        fontweight="bold"
    )

    ax.tick_params(axis="x", colors=COLOR_TEXTO)
    ax.tick_params(axis="y", colors=COLOR_TEXTO_SECUNDARIO)

    ax.grid(axis="y", color=COLOR_BORDE, linestyle="--", alpha=0.45)

    for borde in ax.spines.values():
        borde.set_color(COLOR_BORDE)

    limite_superior = max(estadisticas_jugador) + 5
    ax.set_ylim(0, limite_superior)

    for barra, valor in zip(barras, estadisticas_jugador):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 0.4,
            str(valor),
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
            color=COLOR_TEXTO
        )

    crear_boton(
        [0.38, 0.06, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


def pantalla_menu_jugador():

    limpiar_pantalla()

    crear_cabecera(
    "",
    f"Jugador seleccionado: {jugador_actual['nombre']}"
    )

    fig.text(
        0.06, 0.765,
        f"Posición: {jugador_actual.get('posicion', 'Sin posición')}",
        fontsize=12,
        color=COLOR_TEXTO_SECUNDARIO,
        ha="left"
    )

    fig.text(
        0.06, 0.735,
        "Resumen de rendimiento individual",
        fontsize=12,
        color=COLOR_TEXTO_SECUNDARIO,
        ha="left"
    )

    crear_tarjeta(
        [0.06, 0.57, 0.16, 0.16],
        "Puntos",
        jugador_actual["puntos"],
        COLORES_GRAFICO["Puntos"]
    )

    crear_tarjeta(
        [0.24, 0.57, 0.16, 0.16],
        "Rebotes",
        jugador_actual["rebotes"],
        COLORES_GRAFICO["Rebotes"]
    )

    crear_tarjeta(
        [0.42, 0.57, 0.16, 0.16],
        "Asistencias",
        jugador_actual["asistencias"],
        COLORES_GRAFICO["Asistencias"]
    )

    crear_tarjeta(
        [0.60, 0.57, 0.16, 0.16],
        "Robos",
        jugador_actual["robos"],
        COLORES_GRAFICO["Robos"]
    )

    crear_tarjeta(
        [0.78, 0.57, 0.16, 0.16],
        "Bloqueos",
        jugador_actual["bloqueos"],
        COLORES_GRAFICO["Bloqueos"]
    )

    fig.text(
        0.06, 0.48,
        "ACCIONES RÁPIDAS",
        fontsize=13,
        fontweight="bold",
        color=COLOR_TEXTO,
        ha="left"
    )

    botones = [
        ("Ver gráfico", pantalla_grafico),
        ("Actualizar estadísticas", pantalla_actualizar),
        ("Mejor jugador", pantalla_mejor_jugador),
        ("Ordenar jugadores", pantalla_ordenar),
        ("Analizar equipo", pantalla_analisis),
        ("Ver todos", pantalla_todos),
        ("Quinteto inicial", pantalla_quinteto_inicial),
        ("Crear jugador", pantalla_crear_jugador),
        ("Eliminar jugador", pantalla_eliminar_jugador),
        ("Cambiar jugador", pantalla_inicio),
    ]

    columnas_x = [0.06, 0.375, 0.69]
    y_inicio = 0.38
    ancho = 0.25
    alto = 0.075
    separacion_y = 0.11

    for i, (etiqueta, funcion) in enumerate(botones):
        x = columnas_x[i % 3]
        y = y_inicio - (i // 3) * separacion_y

        crear_boton(
            [x, y, ancho, alto],
            etiqueta,
            lambda event, f=funcion: f()
        )

    plt.draw()


def pantalla_actualizar():

    limpiar_pantalla()

    fig.suptitle(
        f"Actualizar estadísticas de {jugador_actual['nombre']}",
        fontsize=18,
        fontweight="bold"
    )

    ax = crear_ax([0.12, 0.60, 0.75, 0.20])
    ax.axis("off")
    ax.text(0, 1, "Escribe la estadística y el nuevo valor", fontsize=14, va="top")

    ax_est = fig.add_axes([0.20, 0.42, 0.30, 0.07])
    ax_est.set_facecolor("#F8FAFC")
    caja_est = TextBox(ax_est, "Estadística: ", initial="puntos")
    caja_est.text_disp.set_color("#111827")
    caja_est.label.set_color(COLOR_TEXTO)
    widgets.append(caja_est)

    ax_val = fig.add_axes([0.20, 0.30, 0.30, 0.07])
    ax_val.set_facecolor("#F8FAFC")
    caja_val = TextBox(ax_val, "Nuevo valor: ", initial="0")
    caja_val.text_disp.set_color("#111827")
    caja_val.label.set_color(COLOR_TEXTO)
    widgets.append(caja_val)

    ax_resultado = crear_ax([0.20, 0.15, 0.55, 0.08])
    ax_resultado.axis("off")

    def actualizar(event):

        estadistica = caja_est.text.strip().lower()
        valor = caja_val.text.strip()

        ax_resultado.clear()
        ax_resultado.axis("off")
        ax_resultado.set_facecolor(COLOR_FONDO)

        if estadistica not in estadisticas:
            ax_resultado.text(0, 0.8, "Esa estadística no existe", fontsize=12)
        elif not valor.isdigit():
            ax_resultado.text(0, 0.8, "El valor debe ser numérico", fontsize=12)
        else:
            jugador_actual[estadistica] = int(valor)
            ax_resultado.text(0, 0.8, "Estadística actualizada correctamente", fontsize=12)

        plt.draw()

    crear_boton([0.58, 0.35, 0.18, 0.08], "Actualizar", actualizar)
    crear_boton([0.35, 0.04, 0.25, 0.08], "Volver", lambda event: pantalla_menu_jugador())

    plt.draw()


def pantalla_mejor_jugador():

    limpiar_pantalla()

    fig.suptitle("MEJOR JUGADOR", fontsize=18, fontweight="bold")

    ax = crear_ax([0.15, 0.68, 0.7, 0.12])
    ax.axis("off")
    ax.text(0.5, 0.5, "Selecciona una estadística", fontsize=14, ha="center")

    y = 0.58

    for estadistica in estadisticas:
        crear_boton(
            [0.38, y, 0.24, 0.07],
            estadistica,
            lambda event, est=estadistica: mostrar_mejor(est)
        )
        y -= 0.085

    crear_boton(
        [0.38, 0.05, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


def mostrar_mejor(estadistica):

    limpiar_pantalla()

    mejor = max(jugadores, key=lambda j: j[estadistica])

    titulo_estadistica = estadistica.capitalize()
    color_estadistica = COLORES_GRAFICO.get(titulo_estadistica, COLOR_BOTON)

    crear_cabecera(
        f"Mejor en {estadistica}",
        "Jugador con mejor rendimiento en la estadística seleccionada"
    )

    # Panel principal
    ax_grafico = crear_ax([0.18, 0.58, 0.64, 0.18], COLOR_PANEL)
    ax_grafico.set_xticks([])
    ax_grafico.set_yticks([])

    for borde in ax_grafico.spines.values():
        borde.set_edgecolor(COLOR_BORDE)
        borde.set_linewidth(1.5)

    ax_grafico.text(
        0.5, 0.72,
        mejor["nombre"].upper(),
        fontsize=30,
        fontweight="bold",
        color=COLOR_TEXTO,
        ha="center",
        va="center"
    )

    ax_grafico.text(
        0.5, 0.38,
        f"{titulo_estadistica}: {mejor[estadistica]}",
        fontsize=24,
        fontweight="bold",
        color=color_estadistica,
        ha="center",
        va="center"
    )

    ax_grafico.text(
        0.5, 0.14,
        "Mejor jugador del equipo en esta estadística",
        fontsize=11,
        color=COLOR_TEXTO_SECUNDARIO,
        ha="center",
        va="center"
    )

    crear_tarjeta(
        [0.08, 0.37, 0.15, 0.13],
        "Puntos",
        mejor["puntos"],
        COLORES_GRAFICO["Puntos"]
    )

    crear_tarjeta(
        [0.255, 0.37, 0.15, 0.13],
        "Rebotes",
        mejor["rebotes"],
        COLORES_GRAFICO["Rebotes"]
    )

    crear_tarjeta(
        [0.43, 0.37, 0.15, 0.13],
        "Asistencias",
        mejor["asistencias"],
        COLORES_GRAFICO["Asistencias"]
    )

    crear_tarjeta(
        [0.605, 0.37, 0.15, 0.13],
        "Robos",
        mejor["robos"],
        COLORES_GRAFICO["Robos"]
    )

    crear_tarjeta(
        [0.78, 0.37, 0.15, 0.13],
        "Bloqueos",
        mejor["bloqueos"],
        COLORES_GRAFICO["Bloqueos"]
    )

    promedio = sum(j[estadistica] for j in jugadores) / len(jugadores)

    ax_grafico = crear_ax([0.18, 0.12, 0.64, 0.12], COLOR_PANEL)

    valores = [promedio, mejor[estadistica]]
    nombres = ["Promedio equipo", mejor["nombre"]]
    colores = [COLOR_PANEL_2, color_estadistica]

    barras = ax_grafico.bar(nombres, valores, color=colores)

    ax_grafico.set_title(
        "Comparación con el promedio",
        fontsize=10,
        color=COLOR_TEXTO,
        fontweight="bold"
    )

    ax_grafico.tick_params(axis="x", colors=COLOR_TEXTO_SECUNDARIO, labelsize=9)
    ax_grafico.tick_params(axis="y", colors=COLOR_TEXTO_SECUNDARIO, labelsize=8)

    ax_grafico.grid(axis="y", color=COLOR_BORDE, linestyle="--", alpha=0.35)

    for borde in ax_grafico.spines.values():
        borde.set_color(COLOR_BORDE)

    ax_grafico.set_ylim(0, max(valores) + 4)

    for barra, valor in zip(barras, valores):
        ax_grafico.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 0.2,
            str(round(valor, 2)),
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
            color=COLOR_TEXTO
        )

    crear_boton(
        [0.38, 0.015, 0.24, 0.055],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )
    plt.draw()


def pantalla_ordenar():

    limpiar_pantalla()

    fig.suptitle("ORDENAR JUGADORES", fontsize=18, fontweight="bold")

    ax = crear_ax([0.15, 0.68, 0.7, 0.12])
    ax.axis("off")
    ax.text(0.5, 0.5, "Selecciona una estadística", fontsize=14, ha="center")

    y = 0.58

    for estadistica in estadisticas:
        crear_boton(
            [0.38, y, 0.24, 0.07],
            estadistica,
            lambda event, est=estadistica: mostrar_ordenados(est)
        )
        y -= 0.085

    crear_boton(
        [0.38, 0.04, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


def mostrar_ordenados(estadistica):

    limpiar_pantalla()

    fig.suptitle(f"Jugadores ordenados por {estadistica}", fontsize=18, fontweight="bold")

    lista = sorted(jugadores, key=lambda j: j[estadistica], reverse=True)

    ax = crear_ax([0.20, 0.18, 0.60, 0.65])
    ax.axis("off")

    columnas = ["Posición", "Jugador", estadistica]
    datos = []

    for i, jugador in enumerate(lista, start=1):
        datos.append([i, jugador["nombre"], jugador[estadistica]])

    tabla = ax.table(
        cellText=datos,
        colLabels=columnas,
        cellLoc="center",
        loc="center"
    )

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(12)
    tabla.scale(1, 1.6)

    for cell in tabla.get_celld().values():
        cell.set_facecolor(COLOR_FONDO)
        cell.set_edgecolor("white")
        cell.set_linewidth(1.2)

    crear_boton([0.38, 0.06, 0.24, 0.08], "Volver", lambda event: pantalla_menu_jugador())

    plt.draw()


def pantalla_analisis():

    limpiar_pantalla()

    crear_cabecera(
        "Análisis del equipo",
        "Resumen global de rendimiento del equipo"
    )

    total_puntos = sum(j["puntos"] for j in jugadores)
    promedio = total_puntos / len(jugadores)
    total_rebotes = sum(j["rebotes"] for j in jugadores)
    total_asistencias = sum(j["asistencias"] for j in jugadores)
    total_robos = sum(j["robos"] for j in jugadores)
    total_bloqueos = sum(j["bloqueos"] for j in jugadores)

    mejor_anotador = max(jugadores, key=lambda j: j["puntos"])
    mejor_reboteador = max(jugadores, key=lambda j: j["rebotes"])

    crear_tarjeta(
        [0.08, 0.58, 0.18, 0.16],
        "Total puntos",
        total_puntos,
        COLORES_GRAFICO["Puntos"]
    )

    crear_tarjeta(
        [0.30, 0.58, 0.18, 0.16],
        "Promedio",
        round(promedio, 2),
        "#FACC15"
    )

    crear_tarjeta(
        [0.52, 0.58, 0.18, 0.16],
        "Rebotes",
        total_rebotes,
        COLORES_GRAFICO["Rebotes"]
    )

    crear_tarjeta(
        [0.74, 0.58, 0.18, 0.16],
        "Asistencias",
        total_asistencias,
        COLORES_GRAFICO["Asistencias"]
    )

    crear_tarjeta(
        [0.19, 0.34, 0.18, 0.16],
        "Robos",
        total_robos,
        COLORES_GRAFICO["Robos"]
    )

    crear_tarjeta(
        [0.41, 0.34, 0.18, 0.16],
        "Bloqueos",
        total_bloqueos,
        COLORES_GRAFICO["Bloqueos"]
    )

    crear_tarjeta(
        [0.63, 0.34, 0.18, 0.16],
        "Jugadores",
        len(jugadores),
        "#94A3B8"
    )

    ax = crear_ax([0.20, 0.17, 0.60, 0.10], COLOR_PANEL)
    ax.set_xticks([])
    ax.set_yticks([])

    for borde in ax.spines.values():
        borde.set_edgecolor(COLOR_BORDE)
        borde.set_linewidth(1.3)

    texto = (
        f"Máximo anotador: {mejor_anotador['nombre']} ({mejor_anotador['puntos']} puntos)   |   "
        f"Mejor reboteador: {mejor_reboteador['nombre']} ({mejor_reboteador['rebotes']} rebotes)"
    )

    ax.text(
        0.5, 0.5,
        texto,
        fontsize=12,
        color=COLOR_TEXTO,
        ha="center",
        va="center"
    )

    crear_boton(
        [0.38, 0.05, 0.24, 0.08],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()

def pantalla_todos():

    limpiar_pantalla()

    fig.suptitle("TODOS LOS JUGADORES", fontsize=18, fontweight="bold")

    ax = crear_ax([0.08, 0.18, 0.84, 0.68])
    ax.axis("off")

    columnas = ["Nombre", "Puntos", "Rebotes", "Asistencias", "Robos", "Bloqueos"]

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

    COLOR_MEJOR_VALOR = "#B7E4C7" 
    COLOR_BORDE = "#FFFFFF"

    for cell in tabla.get_celld().values():
        cell.set_facecolor(COLOR_FONDO)
        cell.set_edgecolor(COLOR_BORDE)

    for col in range(len(columnas)):
        tabla[(0, col)].get_text().set_fontweight("bold")

    max_puntos = max(jugador["puntos"] for jugador in jugadores)
    max_rebotes = max(jugador["rebotes"] for jugador in jugadores)
    max_asistencias = max(jugador["asistencias"] for jugador in jugadores)
    max_robos = max(jugador["robos"] for jugador in jugadores)
    max_bloqueos = max(jugador["bloqueos"] for jugador in jugadores)

    mejores = {
        1: max_puntos,
        2: max_rebotes,
        3: max_asistencias,
        4: max_robos,
        5: max_bloqueos
    }

    claves = {
        1: "puntos",
        2: "rebotes",
        3: "asistencias",
        4: "robos",
        5: "bloqueos"
    }
    for fila, jugador in enumerate(jugadores, start=1):
        for columna in range(1, 6):
            clave = claves[columna]

            if jugador[clave] == mejores[columna]:
                tabla[(fila, columna)].set_facecolor(COLOR_MEJOR_VALOR)
                tabla[(fila, columna)].get_text().set_color("#052E16")
                tabla[(fila, columna)].get_text().set_fontweight("bold")

    crear_boton([0.38, 0.06, 0.24, 0.08], "Volver", lambda event: pantalla_menu_jugador())

    plt.draw()

def pantalla_quinteto_inicial():

    limpiar_pantalla()

    crear_cabecera(
        "Quinteto inicial",
        "Mejores jugadores disponibles por cada estadística"
    )
    estadisticas_quinteto = [
        ("puntos", "Puntos"),
        ("rebotes", "Rebotes"),
        ("asistencias", "Asistencias"),
        ("robos", "Robos"),
        ("bloqueos", "Bloqueos")
    ]

    quinteto = []
    jugadores_usados = []

    for clave, nombre_estadistica in estadisticas_quinteto:

        jugadores_ordenados = sorted(
            jugadores,
            key=lambda j: j[clave],
            reverse=True
        )

        elegido = None

        for jugador in jugadores_ordenados:
            if jugador["nombre"] not in jugadores_usados:
                elegido = jugador
                break

        if elegido is not None:
            jugadores_usados.append(elegido["nombre"])
            quinteto.append({
                "estadistica": clave,
                "titulo": nombre_estadistica,
                "jugador": elegido,
                "valor": elegido[clave],
                "color": COLORES_GRAFICO[nombre_estadistica]
            })

    fig.text(
        0.06, 0.80,
        "QUINTETO INICIAL",
        fontsize=28,
        fontweight="bold",
        color=COLOR_TEXTO,
        ha="left"
    )

    fig.text(
        0.06, 0.765,
        "Un jugador seleccionado por cada estadística principal",
        fontsize=12,
        color=COLOR_TEXTO_SECUNDARIO,
        ha="left"
    )

    # Tarjetas del quinteto
    posiciones = [
        [0.06, 0.48, 0.16, 0.22],
        [0.24, 0.48, 0.16, 0.22],
        [0.42, 0.48, 0.16, 0.22],
        [0.60, 0.48, 0.16, 0.22],
        [0.78, 0.48, 0.16, 0.22]
    ]

    for i, item in enumerate(quinteto):

        ax = crear_ax(posiciones[i], COLOR_PANEL)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])

        for borde in ax.spines.values():
            borde.set_edgecolor(COLOR_BORDE)
            borde.set_linewidth(1.4)

        ax.add_patch(
            Rectangle(
                (0, 0.88),
                1,
                0.12,
                transform=ax.transAxes,
                color=item["color"],
                linewidth=0
            )
        )

        ax.text(
            0.08, 0.72,
            item["titulo"].upper(),
            fontsize=10,
            fontweight="bold",
            color=COLOR_TEXTO_SECUNDARIO,
            ha="left",
            va="center"
        )

        ax.text(
            0.08, 0.47,
            item["jugador"]["nombre"],
            fontsize=18,
            fontweight="bold",
            color=COLOR_TEXTO,
            ha="left",
            va="center"
        )
        ax.text(
            0.08, 0.34,
            item["jugador"]["posicion"],
            fontsize=10,
            color=COLOR_TEXTO_SECUNDARIO,
            ha="left",
            va="center"
        )

        ax.text(
            0.08, 0.16,
            str(item["valor"]),
            fontsize=30,
            fontweight="bold",
            color=item["color"],
            ha="left",
            va="center"
        )
    ax_tabla = crear_ax([0.16, 0.17, 0.68, 0.22], COLOR_FONDO)
    ax_tabla.axis("off")

    columnas = ["Posición", "Jugador", "Puntos", "Rebotes", "Asistencias", "Robos", "Bloqueos"]

    datos = []

    for item in quinteto:
        jugador = item["jugador"]
        datos.append([
            jugador["posicion"],
            jugador["nombre"],
            jugador["puntos"],
            jugador["rebotes"],
            jugador["asistencias"],
            jugador["robos"],
            jugador["bloqueos"]
        ])

    tabla = ax_tabla.table(
        cellText=datos,
        colLabels=columnas,
        cellLoc="center",
        loc="center"
    )

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1, 1.5)

    for (fila, columna), cell in tabla.get_celld().items():

        cell.set_edgecolor(COLOR_BORDE)
        cell.set_linewidth(1.1)

        if fila == 0:
            cell.set_facecolor(COLOR_BOTON)
            cell.get_text().set_color(COLOR_TEXTO_BOTON)
            cell.get_text().set_fontweight("bold")
        else:
            cell.set_facecolor(COLOR_PANEL)
            cell.get_text().set_color(COLOR_TEXTO)

    crear_boton(
        [0.38, 0.05, 0.24, 0.07],
        "Volver",
        lambda event: pantalla_menu_jugador()
    )

    plt.draw()


def pantalla_crear_jugador():

    limpiar_pantalla()

    fig.suptitle("CREAR NUEVO JUGADOR", fontsize=18, fontweight="bold")

    cajas = {}

    campos = ["nombre", "posicion", "puntos", "rebotes", "asistencias", "robos", "bloqueos"]

    y = 0.72

    for campo in campos:
        ax_caja = fig.add_axes([0.35, y, 0.30, 0.06])
        ax_caja.set_facecolor(COLOR_FONDO)
        caja = TextBox(ax_caja, campo.capitalize() + ": ")
        cajas[campo] = caja
        widgets.append(caja)
        y -= 0.09

    ax_resultado = crear_ax([0.20, 0.12, 0.60, 0.08])
    ax_resultado.axis("off")

    def crear(event):

        ax_resultado.clear()
        ax_resultado.axis("off")
        ax_resultado.set_facecolor(COLOR_FONDO)

        nombre = cajas["nombre"].text.strip()
        posicion = cajas["posicion"].text.strip()

        if nombre == "":
            ax_resultado.text(0.5, 0.5, "Debes escribir un nombre",
                              fontsize=12, ha="center", va="center")

        elif posicion == "":
            ax_resultado.text(0.5, 0.5, "Debes escribir una posición",
                              fontsize=12, ha="center", va="center")

        elif buscar_jugador(nombre) is not None:
            ax_resultado.text(0.5, 0.5, "Ese jugador ya existe",
                              fontsize=12, ha="center", va="center")

        else:
            nuevo_jugador = {"nombre": nombre, "posicion": posicion}
            correcto = True

            for estadistica in estadisticas:
                valor = cajas[estadistica].text.strip()
                if not valor.isdigit():
                    correcto = False
                else:
                    nuevo_jugador[estadistica] = int(valor)

            if correcto:
                jugadores.append(nuevo_jugador)
                ax_resultado.text(0.5, 0.5, "Jugador creado correctamente",
                                  fontsize=12, ha="center", va="center")
            else:
                ax_resultado.text(0.5, 0.5, "Las estadísticas deben ser números",
                                  fontsize=12, ha="center", va="center")

        plt.draw()

    crear_boton([0.25, 0.03, 0.20, 0.07], "Crear", crear)
    crear_boton([0.55, 0.03, 0.20, 0.07], "Volver", lambda event: pantalla_menu_jugador())

    plt.draw()


def pantalla_eliminar_jugador():

    limpiar_pantalla()

    fig.suptitle("ELIMINAR JUGADOR", fontsize=18, fontweight="bold")

    ax = crear_ax([0.15, 0.78, 0.70, 0.10])
    ax.axis("off")
    ax.text(0.5, 0.5, "Selecciona el jugador que quieres eliminar",
            fontsize=14, ha="center", va="center")

    # Distribuir en 2 columnas igual que pantalla_inicio
    col_izq_x = 0.22
    col_der_x = 0.58
    y_inicio = 0.68
    separacion = 0.065

    for i, jugador in enumerate(jugadores):
        col_x = col_izq_x if i % 2 == 0 else col_der_x
        fila = i // 2
        y = y_inicio - fila * separacion

        crear_boton(
            [col_x, y, 0.20, 0.052],
            jugador["nombre"],
            lambda event, nombre=jugador["nombre"]: pantalla_confirmar_eliminar(nombre)
        )

    crear_boton([0.38, 0.04, 0.24, 0.07], "Volver", lambda event: pantalla_menu_jugador())

    plt.draw()


def pantalla_confirmar_eliminar(nombre):

    limpiar_pantalla()

    fig.suptitle("CONFIRMAR ELIMINACIÓN", fontsize=18, fontweight="bold")

    ax = crear_ax([0.20, 0.35, 0.60, 0.30])
    ax.axis("off")

    ax.text(
        0.5, 0.5,
        f"¿Seguro que quieres eliminar a {nombre}?",
        fontsize=16, ha="center", va="center"
    )

    def eliminar(event):

        global jugador_actual

        jugador = buscar_jugador(nombre)

        if jugador is not None:
            jugadores.remove(jugador)
            if jugador_actual == jugador:
                jugador_actual = None

        pantalla_inicio()

    crear_boton([0.25, 0.18, 0.20, 0.08], "Sí, eliminar", eliminar)
    crear_boton([0.55, 0.18, 0.20, 0.08], "Cancelar", lambda event: pantalla_eliminar_jugador())

    plt.draw()

pantalla_inicio()
plt.show()