# Importo las bibliotecas necesarias para manejar matrices (numpy) y graficar (matplotlib).
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Creo una función llamada es_movimiento_valido que verifica si un movimiento del caballo en el tablero es válido.
# Me aseguro de que el movimiento esté dentro de los límites del tablero y que la casilla a la que el caballo se
# moverá no esté ya ocupada (representada por un valor diferente a -1).
def es_movimiento_valido(tablero, fila, columna):
    tamaño = len(tablero)
    return 0 <= fila < tamaño and 0 <= columna < tamaño and tablero[fila][columna] == -1

# Implemento la función resolver_tour_del_caballo para intentar encontrar una solución al problema del recorrido del 
#caballo usando un enfoque de backtracking.
# Utilizo un tablero, la posición actual del caballo, el número de movimientos realizados hasta ahora, la lista
# de movimientos posibles y las posiciones visitadas.
# Si se logran completar todos los movimientos necesarios (tamaño del tablero al cuadrado), entonces devuelvo True.
def resolver_tour_del_caballo(tablero, fila, columna, contador_movimientos, movimientos, posiciones):
    tamaño = len(tablero)
    if contador_movimientos == tamaño * tamaño:
        return True
    for movimiento in movimientos:
        siguiente_fila, siguiente_columna = fila + movimiento[0], columna + movimiento[1]
        if es_movimiento_valido(tablero, siguiente_fila, siguiente_columna):
            tablero[siguiente_fila][siguiente_columna] = contador_movimientos
            posiciones.append((siguiente_fila, siguiente_columna))
            if resolver_tour_del_caballo(tablero, siguiente_fila, siguiente_columna, contador_movimientos + 1, movimientos, posiciones):
                return True
            tablero[siguiente_fila][siguiente_columna] = -1
            posiciones.pop()
    return False

# configurar_tablero inicializa el tablero con el tamaño dado y coloca todos los valores a -1 para marcar que están
# desocupados.
# Define la lista de movimientos posibles del caballo y comienza la resolución desde la casilla inicial (0, 0).
# Si logra resolver el tour, devuelve la lista de posiciones y el tablero final. De lo contrario, indica que no hay solución.
def configurar_tablero(tamaño):
    tablero = [[-1 for _ in range(tamaño)] for _ in range(tamaño)]
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    posiciones = [(0, 0)]
    tablero[0][0] = 0
    if resolver_tour_del_caballo(tablero, 0, 0, 1, movimientos, posiciones):
        return posiciones, tablero
    else:
        print(f"No se encontró solución para un tablero de tamaño {tamaño}x{tamaño}.")
        return None, None

# animar_solucion utiliza matplotlib para mostrar una animación del recorrido que realiza el caballo sobre el tablero.
# Configura una cuadrícula, y en cada fotograma marca las posiciones visitadas con una 'X' y representa la posición actual del caballo con un cuadrado rojo.
def animar_solucion(posiciones, tablero):
    tamaño = len(tablero)
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
        x, y = posiciones[frame]
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

    ani = animation.FuncAnimation(fig, update, frames=len(posiciones), init_func=init, blit=False, repeat=False, interval=500)
    plt.show()

# Solicito al usuario que elija el tamaño del tablero. Me aseguro de que sea un valor entero de 1 o más.
# Una vez que se ingresa un tamaño válido, configuro el tablero y animo la solución si es encontrada.
while True:
    try:
        tamaño_tablero = int(input("Ingresa el tamaño del tablero (mínimo 1): "))
        if tamaño_tablero >= 1:
            break
        else:
            print("Por favor elige un tamaño de 1 o más.")
    except ValueError:
        print("Entrada inválida. Por favor ingresa un valor entero.")

posiciones, tablero = configurar_tablero(tamaño_tablero)
if posiciones:
    animar_solucion(posiciones, tablero)