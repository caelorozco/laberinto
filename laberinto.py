import heapq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# matriz del laberinto
laberinto = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0]
]

def obtener_vecinos(laberinto, nodo):
    vecinos = []
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for direccion in direcciones:
        vecino = (nodo[0] + direccion[0], nodo[1] + direccion[1])
        if 0 <= vecino[0] < len(laberinto) and 0 <= vecino[1] < len(laberinto[0]):
            if laberinto[vecino[0]][vecino[1]] == 0:
                vecinos.append(vecino)
    return vecinos

# algoritmo de Dijkstra
def dijkstra(laberinto, inicio, fin):
    filas, columnas = len(laberinto), len(laberinto[0])
    distancias = { (i, j): float('inf') for i in range(filas) for j in range(columnas) }
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    prev = {inicio: None}
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == fin:
            break
        
        for vecino in obtener_vecinos(laberinto, nodo_actual):
            nueva_distancia = distancia_actual + 1
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                prev[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    camino = []
    paso = fin
    while paso is not None:
        camino.append(paso)
        paso = prev[paso]
    camino.reverse()
    return camino

#damos las coordenadas de inicio y fin
inicio = (2, 2)
fin = (5, 5)
camino = dijkstra(laberinto, inicio, fin)

laberinto_visual = np.array(laberinto)
for nodo in camino:
    laberinto_visual[nodo[0]][nodo[1]] = 2

colormap = ListedColormap(['white', 'black', 'lightgreen'])

plt.imshow(laberinto_visual, cmap=colormap, interpolation='nearest')
plt.show()

