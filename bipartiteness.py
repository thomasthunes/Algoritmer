from collections import namedtuple as T
from collections import deque


def isBipartite(p):
    for elem in p[0]:
        if elem in p[1]:
            return False
    return True


def bipartiteLabelPartition(G):  # total runtime is O(V + E)
    queue = deque([G.V[0]])  # O(1)
    visited = []  # O(1)
    label_partition = {  # O(1)
        0: [G.V[0]],
        1: []
    }

    label = 1
    while len(queue) != 0:  # O(nodes)
        node = queue.popleft()  # O(1)
        visited.append(node)  # O(1)

        all_neigh_unvisited = True  # O(1)
        for neigh in G.N[node]:  # O(edges)
            if neigh not in visited:  # O(1)
                queue.append(neigh)  # O(1)
                label_partition[label].append(neigh)  # O(1)
            else:
                all_neigh_unvisited = False  # O(1)

        if all_neigh_unvisited:  # O(1)
            label = abs(label - 1)  # O(1)

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

