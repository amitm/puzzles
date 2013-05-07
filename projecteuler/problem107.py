

# a couple shortcuts
def mst_kruskal(edges, v):
    sorted_edges = sorted(edges, cmp=lambda x, y: cmp(x[2], y[2]))
    sets = range(v)
    a = []
    for edge in sorted_edges:
        edge_i_set = sets[edge[0]]
        edge_j_set = sets[edge[1]]
        if edge_i_set != edge_j_set:
            a.append(edge)
            sets = [edge_i_set if i == edge_j_set else i for i in sets]
    return a


def get_edges(network_file):
    edges = []
    v = 0
    for line in network_file:
        for j, item in enumerate(line.strip().split(',')):
            if j >= v and item != '-':
                edges.append((v, j, int(item)))
        v += 1
    return edges, v

if __name__ == '__main__':
    with open('data/network.txt') as f:
        edges, v = get_edges(f)
        cost = sum([i[2] for i in edges])
        new_cost = sum([i[2] for i in mst_kruskal(edges, v)])
        print cost - new_cost
