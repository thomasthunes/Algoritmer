from collections import namedtuple as T
from collections import deque

Graph = T("Graph", "V N")

G = Graph(V=[0, 1, 2, 3], N=[[1, 2], [0, 2, 3], [0, 1], [1]])
G1 = Graph(V=[0, 1, 2, 3], N=[[1, 3], [0], [3], [2, 0]])


# for v in G1.V:
#    print(v, G1.N[v])


def f(G): # total runtime is O(V + E)
    queue = deque([G.V[0]])   # O(1)
    visited = []   # O(1)
    label_partition = {  # O(1)
        0: [G.V[0]],
        1: []
    }

    label = 1
    while len(queue) != 0:  # O(nodes)
        node = queue.popleft()  # O(1)
        visited.append(node)   # O(1)

        all_neigh_unvisited = True  # O(1)
        for neigh in G.N[node]:  # O(edges)
            if neigh not in visited:  # O(1)
                queue.append(neigh)  # O(1)
                label_partition[label].append(neigh)  # O(1)
            else:
                all_neigh_unvisited = False   # O(1)

        if all_neigh_unvisited:  # O(1)
            label = abs(label - 1)  # O(1)
    return label_partition


print(f(G1))
print(f(G))
