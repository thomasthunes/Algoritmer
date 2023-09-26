from collections import namedtuple as T
from collections import deque


def isBipartite(p):
    for elem in p[0]:
        if elem in p[1]:
            return False
    return True


def bipartiteLabelPartition(G):
    queue = deque([G.V[0]])
    visited = []
    label_partition = {
        0: [G.V[0]],
        1: []
    }
    label = 1
    while len(queue) != 0:
        node = queue.popleft()
        visited.append(node)

        all_neigh_unvisited = True
        for neigh in G.N[node]:
            if neigh not in visited:
                queue.append(neigh)
                label_partition[label].append(neigh)
            else:
                all_neigh_unvisited = False

        if all_neigh_unvisited:
            label = abs(label - 1)

    if isBipartite(label_partition):
        print("The graph is a bipartite graph")
        print(label_partition)
        return label_partition
    print("The graph is an odd cycle")
    print(label_partition)
    return label_partition


Graph = T("Graph", "V N")

G0 = Graph(V=[0, 1, 2, 3], N=[[1, 2], [0, 2, 3], [0, 1], [1]])
G1 = Graph(V=[0, 1, 2, 3], N=[[1, 3], [0], [3], [2, 0]])

bipartiteLabelPartition(G0)
bipartiteLabelPartition(G1)

