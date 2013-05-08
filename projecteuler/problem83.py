import sys
from problem81 import get_matrix


class PriorityQueue(object):
    # send in a list of distances, the idx is the vertex and the value
    # is the distance
    def __init__(self, distances):
        self._distances = [i for i in distances]

    def is_empty(self):
        return sum(self._distances) == -len(self._distances)

    def extract_min(self):
        min_v = None
        min_distance = sys.maxint
        for v, distance in enumerate(self._distances):
            if distance != -1 and distance < min_distance:
                min_distance = distance
                min_v = v
        if min_v is None:
            raise Exception("Queue is empty")
        self._distances[min_v] = -1
        return min_v

    def decrease(self, v, new_distance):
        if self._distances[v] == -1 or self._distances[v] < new_distance:
            raise Exception("Invalid decrease")
        self._distances[v] = new_distance


def get_graph(matrix):
    size = len(matrix)
    graph = [[] for i in xrange(size ** 2)]
    for i in xrange(size):
        for j in xrange(size):
            current = i * size + j
            # going up
            if i > 0:
                graph[current].append((current - size, matrix[i - 1][j]))
            # going down
            if i < size - 1:
                graph[current].append((current + size, matrix[i + 1][j]))
            # going left
            if j > 0:
                graph[current].append((current - 1, matrix[i][j - 1]))
            # going right
            if j < size - 1:
                graph[current].append((current + 1, matrix[i][j + 1]))
    return graph


def _min(distances):
    min_i = None
    min_distance = sys.maxint
    for i, d in enumerate(distances):
        if not d['completed'] and d['distance'] < min_distance:
            min_i = i
            min_distance = d['distance']
    return min_i


def dijkstra_small(graph, s):
    distances = [{'distance': sys.maxint,
                  'completed': False} for i in xrange(len(graph))]
    distances[s]['distance'] = 0
    while not all([d['completed'] for d in distances]):
        u = _min(distances)
        distances[u]['completed'] = True
        for edge in graph[u]:
            v = edge[0]
            v_distance = distances[v]['distance']
            new_distance = distances[u]['distance'] + edge[1]
            if new_distance < v_distance:
                distances[v]['distance'] = new_distance
    return [d['distance'] for d in distances]


def dijkstra(graph, s):
    distances = [sys.maxint] * len(graph)
    distances[s] = 0
    queue = PriorityQueue(distances)
    while not queue.is_empty():
        u = queue.extract_min()
        u_distance = distances[u]
        print u, u_distance
        for edge in graph[u]:
            v = edge[0]
            distance = distances[v]
            new_distance = u_distance + edge[1]
            if new_distance < distance:
                distances[v] = new_distance
                queue.decrease(v, new_distance)
    return distances


if __name__ == "__main__":
    with open('data/matrix.txt') as f:
        mtx = get_matrix(f)
        graph = get_graph(mtx)
        print dijkstra_small(graph, 0)[len(graph) - 1] + mtx[0][0]
