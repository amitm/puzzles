"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom
right, by only moving to the right and down, is indicated in bold red and is
equal to 2427.

131 673 234 103 18 201 96 342 965 150 630 803 746 422 111 537 699 497 121 956
805 732 524 37 331
Find the minimal path sum, in matrix.txt (right click and 'Save
Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top
left to the bottom right by only moving right and down.
"""

import sys

def get_graph(matrix):
    size = len(matrix)
    graph_matrix = [size ** 2 * [0] for i in xrange(size ** 2)]

    for row in xrange(size):
        for col in xrange(size):
            node = row * size + col
            if col < size - 1:
                graph_matrix[node][node + 1] = matrix[row][col + 1]
            if row < size - 1:
                graph_matrix[node][node + size] = matrix[row + 1][col]
    return graph_matrix

def get_neighbors(graph, node):
    return [i for i in xrange(len(graph)) if graph[node][i] > 0]

def get_path(graph, source, destination):
    distances = {}
    previous = {}
    unoptimized_nodes = []
    for v in xrange(len(graph)):
        distances[v] = sys.maxint
        previous[v] = None
        unoptimized_nodes.append(v)
    distances[source] = 0
    unoptimized_nodes = set(unoptimized_nodes)
    while len(unoptimized_nodes) > 0:
        current_node = None
        smallest_distance = sys.maxint
        for node in unoptimized_nodes:
            if distances[node] < smallest_distance:
                smallest_distance = distances[node]
                current_node = node
        if smallest_distance == sys.maxint or current_node == destination:
            break
        unoptimized_nodes.remove(current_node)
        
        for neighbor in get_neighbors(graph, current_node):
            distance = distances[current_node] + graph[current_node][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
    path = []
    d = destination
    while previous[d] is not None:
        path.insert(0, d)
        d = previous[d]
    return path, distances[destination]

if __name__ == "__main__":
    f = open('data/matrix.txt')
    matrix = []
    for line in f:
        matrix.append([int(i) for i in line.split(',')])
    print matrix
    graph = get_graph(matrix)
    print get_path(graph, 0, len(graph) - 1)[1] + matrix[0][0]

    