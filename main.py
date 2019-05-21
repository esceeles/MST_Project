import numpy as np
import networkx as nx

# generates random graph with three vertices as adjacency matrix
adjacency = np.random.randint(0,2,(3,3))
print(adjacency)

# generates random graph with (n nodes, m edges)
er = nx.gnm_random_graph(3, 3, seed=None, directed=False)
er2 = nx.gnm_random_graph(3, 2, seed=None, directed=False)

G = nx.Graph()
G.add_edge(1, 2)

print(er.adj)
print(er2.adj)
print(G.adj)
