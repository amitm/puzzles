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


def get_matrix(matrix_file):
    return [[int(i) for i in line.strip().split(',')] for line in matrix_file]


def get_graph(matrix):
    size = len(matrix)
    graph = [[] for i in xrange(size ** 2)]
    for i in xrange(size):
        for j in xrange(size):
            # going down
            current = i * size + j
            if i < size - 1:
                graph[current].append((current + size, matrix[i + 1][j]))
            # going right
            if j < size - 1:
                graph[current].append((current + 1, matrix[i][j + 1]))
    return graph


def topological_sort(graph):
    seen = set([0])

    def ts_helper(v):
        results = []
        for edge in graph[v]:
            if edge[0] not in seen:
                seen.add(edge[0])
                results = ts_helper(edge[0]) + results
        return [v] + results
    return ts_helper(0)


# can be optomized
def dag_shortest_path(graph, s):
    # technically the topological sort isnt neccessary
    sorted_verticies = topological_sort(graph)
    data = [None] * len(graph)
    data[s] = 0
    for u in sorted_verticies:
        if data[u] is not None:
            for edge in graph[u]:
                v = edge[0]
                if data[v] is None or data[u] + edge[1] < data[v]:
                    data[v] = data[u] + edge[1]
    return data


if __name__ == "__main__":
    with open('data/matrix.txt') as f:
        mtx = get_matrix(f)
        g = get_graph(mtx)
        print dag_shortest_path(g, 0)[len(g) - 1] + mtx[0][0]
