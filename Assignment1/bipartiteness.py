from collections import namedtuple as T

Graph = T("Graph", "V N")


def odd_cycle(neighbor, node, parent_mapping):
    """

    :param neighbor:
    :param node:
    :param parent_mapping:
    :return: a list of nodes in the odd cycle
    """
    odd_cycle = []
    start_node = neighbor
    end_node = node

    while start_node != end_node:
        if start_node in odd_cycle:
            # if we started on the wrong node, we switch direction
            start_node, end_node = node, neighbor
            odd_cycle = []

        odd_cycle.append(start_node)
        start_node = parent_mapping[start_node][0]
    odd_cycle.append(start_node)
    return odd_cycle


def dfs(G):
    """
        Determine if a given connected and undirected graph is bipartite or contains an odd cycle.

        Parameters:
        - G (Graph): A named tuple representing the graph structure, with fields 'V' and 'N'.
                     'V' is a list of vertices, and 'N' is a dictionary mapping vertices to their neighbors.

        Returns:
        - If bipartite: A dictionary mapping each vertex to 0 or 1, representing the bipartition.
        - If contains an odd cycle: A list containing the vertices forming the odd cycle.

        Note:
        - The first vertex in 'G.V' is assumed to be labeled as 0.
    """
    def dfs_helper(node, label):
        visited.add(node)
        partition[label].append(node)
        label = 1 - label

        for neighbor in G.N[node]:
            if neighbor in partition[1 - label]:
                wrong_label_nodes.append(neighbor)
                wrong_label_nodes.append(node)
                return
            if neighbor not in visited:
                parent_mapping[neighbor] = [node]
                dfs_helper(neighbor, label)
        return

    root = G.V[0]
    visited = set()
    wrong_label_nodes = []
    partition = {
        0: [],
        1: []
    }
    label = 0
    parent_mapping = {root: [G.N[root][0]]}
    dfs_helper(root, label)

    if len(wrong_label_nodes) != 0:
        neigh, node = wrong_label_nodes[0], wrong_label_nodes[1]
        oc = odd_cycle(neigh, node, parent_mapping)
        print("Odd cycle: ", oc)
        return oc

    print("The graph is a bipartite graph: ", partition)
    return partition


G0_0 = Graph(V=[0, 1, 2, 3, 4, 5, 6, 7], N=[[1, 3], [0, 5], [3, 5, 6], [0, 2], [5], [1, 2, 4], [2, 7, 8], [6], [6]])
G1_0 = Graph(V=[0, 1, 2, 3], N=[[1, 2], [0, 2, 3], [0, 1], [1]])
G2_0 = Graph(V=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], N=[[1, 3, 9], [0, 5], [3, 5, 6], [0, 2], [5], [1, 2, 4], [2, 7, 8], [6], [6], [0]])
G3_0 = Graph(V=[0, 1, 2, 3, 4, 5, 6], N=[[6, 1, 3], [0, 5], [3, 5], [0, 2], [5], [1, 2, 4], [0]])

# Odd cycles
G0 = Graph(V=[0, 1, 2, 3], N=[[1, 2], [0, 2, 3], [0, 1], [1]])
G3 = Graph(V=[0, 1, 2, 3, 4], N=[[1, 2], [0, 3, 4], [0], [1, 4], [3, 1]])
G4 = Graph(V=[0, 1, 2, 3, 4, 5], N=[[1], [0, 2], [1, 3], [2, 4, 5], [3, 5], [3, 4]])
G6 = Graph(V=[0, 1, 2, 3, 4, 5], N=[[1, 3], [0], [3, 5], [0, 2], [5], [1, 2, 4]])
G8 = Graph(V=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
           N=[[1, 10], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 0]])

# Partite graphs
G5 = Graph(V=[0, 1, 2, 3], N=[[1, 2], [0, 3], [0, 3], [1, 2]])
G7 = Graph(V=[0, 1, 2, 3, 4], N=[[1, 3], [0, 2], [1], [0, 4], [3]])

# bi
gpt1 = Graph(V=[0, 1, 2, 3, 4], N=[[1, 3], [0, 2, 4], [1, 3], [0, 2, 4], [1, 3]])
gpt2 = Graph(V=[0, 1, 2, 3, 4, 5], N=[[1, 3], [0, 2, 4], [1, 3], [0, 2, 4], [1, 3], [5]])
# odd
gpt3 = Graph(V=[0, 1, 2, 3, 4], N=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2, 4], [3]])
# bi
gpt4 = Graph(V=[0, 1, 2, 3], N=[[1, 3], [0, 2], [1, 3], [0, 2]])
gpt5 = Graph(V=[0, 1, 2, 3], N=[[1, 2], [0, 3], [0, 3], [1, 2]])

# dfs(G0_0)
# dfs(G1_0)
# dfs(G0)
# dfs(G3)
# dfs(G4)
# dfs(G5)
# dfs(G6)
# dfs(G7)
# dfs(G8)

#dfs(gpt1)
#dfs(gpt2)
#dfs(gpt3)
#dfs(gpt4)
#dfs(gpt5)

#dfs(G2_0)
dfs(G3_0)
