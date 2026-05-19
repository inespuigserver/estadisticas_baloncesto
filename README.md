# GameStats – Aplicación de análisis de baloncesto

GameStats es una aplicación interactiva desarrollada en Python utilizando Matplotlib. Permite visualizar, gestionar y analizar estadísticas de jugadores de baloncesto mediante una interfaz gráfica construida completamente con figuras, botones, paneles y tablas dentro de Matplotlib.

## Descripción general

La aplicación permite:

- Seleccionar un jugador y ver un resumen de sus estadísticas.
- Mostrar un gráfico comparativo de sus valores principales.
- Ordenar jugadores según cualquier estadística.
- Identificar al mejor jugador en cada categoría.
- Analizar el rendimiento global del equipo.
- Ver una tabla completa con todos los jugadores.
- Generar un quinteto ideal sin repetir jugadores.
- Crear nuevos jugadores desde la interfaz.
- Actualizar estadísticas de jugadores existentes.
- Eliminar jugadores del sistema.

Toda la interfaz está construida con botones, paneles, tarjetas y tablas diseñadas manualmente mediante Matplotlib.

## Requisitos

- Python 3.8 o superior
- Matplotlib

Instalación de dependencias:

pip install matplotlib

## Ejecución

Para iniciar la aplicación:
python gamestats.py

## Estructura del proyecto

GameStats/
│── gamestats.py        Código principal de la aplicación
│── README.md           Archivo de documentación

## Funcionamiento de la aplicación

La interfaz está dividida en pantallas, cada una representada por una función independiente. Todas las pantallas se dibujan sobre la misma figura de Matplotlib, limpiando y reconstruyendo los elementos según la acción del usuario.

### Pantallas principales

1. pantalla_inicio() 
   Muestra todos los jugadores disponibles y permite seleccionar uno.

2. pantalla_menu_jugador()
   Presenta un resumen del jugador seleccionado y un menú de acciones rápidas.

3. pantalla_grafico() 
   Muestra un gráfico de barras con las estadísticas principales del jugador.

4. pantalla_mejor_jugador()  
   Permite elegir una estadística y ver quién es el mejor en ella.

5. pantalla_ordenar() 
   Ordena a todos los jugadores según la estadística seleccionada.

6. pantalla_analisis()  
   Muestra totales, promedios y mejores jugadores del equipo.

7. pantalla_todos()  
   Tabla completa con todos los jugadores y resaltado automático de los mejores valores.

8. pantalla_titulares()  
   Genera un quinteto ideal seleccionando al mejor jugador en cada estadística sin repetir jugadores.

9. pantalla_crear_jugador() 
   Formulario para añadir un nuevo jugador al sistema.

10. pantalla_eliminar_jugador() 
    Permite seleccionar un jugador y eliminarlo.

11. pantalla_actualizar() 
    Permite modificar cualquier estadística del jugador actual.

## Datos utilizados

Los jugadores se almacenan en una lista de diccionarios con la siguiente estructura:

{
    "nombre": "Juan",
    "posicion": "Base",
    "puntos": 15,
    "rebotes": 7,
    "asistencias": 4,
    "robos": 2,
    "bloqueos": 1
}


Las estadísticas principales son:

puntos
rebotes
asistencias
robos
bloqueos


## Objetivo del proyecto

Crear una aplicación para consultar, comparar y gestionar las estadísticas de jugadores de baloncesto de forma sencilla e interactiva.

El proyecto permite analizar el rendimiento individual y del equipo mediante pantallas visuales, tablas, gráficos y selección de titulares.