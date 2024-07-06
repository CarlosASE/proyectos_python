import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Función que verifica si un movimiento del caballo en el tablero es válido.
def es_movimiento_valido(tablero, fila, columna):
    tamaño = len(tablero)
    return 0 <= fila < tamaño and 0 <= columna < tamaño and tablero[fila][columna] == -1

# Función que intenta encontrar todas las soluciones posibles al problema del recorrido del caballo desde una posición específica.
def encontrar_todas_las_soluciones(tablero, fila, columna, contador_movimientos, movimientos, posiciones, soluciones):
    tamaño = len(tablero)
    if contador_movimientos == tamaño * tamaño:
        soluciones.append(posiciones[:])  # Guardar una copia de la solución actual
        return
    for movimiento in movimientos:
        siguiente_fila, siguiente_columna = fila + movimiento[0], columna + movimiento[1]
        if es_movimiento_valido(tablero, siguiente_fila, siguiente_columna):
            tablero[siguiente_fila][siguiente_columna] = contador_movimientos
            posiciones.append((siguiente_fila, siguiente_columna))
            encontrar_todas_las_soluciones(tablero, siguiente_fila, siguiente_columna, contador_movimientos + 1, movimientos, posiciones, soluciones)
            tablero[siguiente_fila][siguiente_columna] = -1
            posiciones.pop()

# Inicializa el tablero y busca todas las soluciones posibles desde todas las posiciones iniciales.
def configurar_tablero(tamaño):
    soluciones = []
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    for fila_inicial in range(tamaño):
        for columna_inicial in range(tamaño):
            tablero = [[-1 for _ in range(tamaño)] for _ in range(tamaño)]
            posiciones = [(fila_inicial, columna_inicial)]
            tablero[fila_inicial][columna_inicial] = 0
            encontrar_todas_las_soluciones(tablero, fila_inicial, columna_inicial, 1, movimientos, posiciones, soluciones)
    
    return soluciones

# Anima una solución específica.
def animar_solucion(solucion, tamaño, on_complete):
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, tamaño - 0.5)
    ax.set_ylim(-0.5, tamaño - 0.5)
    ax.set_xticks(np.arange(-0.5, tamaño, 1))
    ax.set_yticks(np.arange(-0.5, tamaño, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)

    caballo, = ax.plot([], [], 'rs', markersize=28)
    marcas = np.full((tamaño, tamaño), '', dtype='<U1')

    def init():
        caballo.set_data([], [])
        return caballo

    def update(frame):
        x, y = solucion[frame]
        marcas[x, y] = 'X'
        ax.clear()
        ax.set_xlim(-0.5, tamaño - 0.5)
        ax.set_ylim(-0.5, tamaño - 0.5)
        ax.set_xticks(np.arange(-0.5, tamaño, 1))
        ax.set_yticks(np.arange(-0.5, tamaño, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(True)
        for i in range(tamaño):
            for j in range(tamaño):
                if marcas[i, j] == 'X':
                    ax.text(j, tamaño - 1 - i, 'X', color='black', ha='center', va='center', fontsize=8, fontweight='bold')
        caballo.set_data(y, tamaño - 1 - x)
        return caballo

    ani = animation.FuncAnimation(fig, update, frames=len(solucion), init_func=init, blit=False, repeat=False, interval=50)
    
    def on_complete_callback(*args):
        plt.close(fig)
        if on_complete:
            on_complete()

    fig.canvas.mpl_connect('close_event', on_complete_callback)
    plt.show(block=False)
    plt.pause(len(solucion) * 0.05 + 0.5)  # Duración de la animación + margen de seguridad
    plt.close(fig)  # Cerrar la figura después de la animación

# Solicita al usuario el tamaño del tablero y muestra todas las soluciones.
def mostrar_soluciones(tamaño_tablero):
    soluciones = configurar_tablero(tamaño_tablero)
    if soluciones:
        print(f"Se encontraron {len(soluciones)} soluciones. Mostrando cada una de ellas.")
        def mostrar_siguiente_solucion(index=0):
            if index < len(soluciones):
                print(f"Animando solución {index+1}/{len(soluciones)}")
                animar_solucion(soluciones[index], tamaño_tablero, lambda: mostrar_siguiente_solucion(index + 1))
        mostrar_siguiente_solucion()
    else:
        print(f"No se encontraron soluciones para un tablero de tamaño {tamaño_tablero}x{tamaño_tablero}.")

# Solicita al usuario el tamaño del tablero.
while True:
    try:
        tamaño_tablero = int(input("Ingresa el tamaño del tablero (mínimo 1): "))
        if tamaño_tablero >= 1:
            break
        else:
            print("Por favor elige un tamaño de 1 o más.")
    except ValueError:
        print("Entrada inválida. Por favor ingresa un valor entero.")

mostrar_soluciones(tamaño_tablero)