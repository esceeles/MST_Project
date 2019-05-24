import numpy as np
import networkx as nx
import random

# generates random graph with three vertices as adjacency matrix
#adjacency = np.random.randint(0,2,(3,3))
#print(adjacency)

# generates random graph with (n nodes, m edges)
G = nx.gnm_random_graph(3, 3, seed=None, directed=False)
#er = nx.gnm_random_graph(3, 2, seed=None, directed=False)

#print(er.adj)
print(G.adj)

for (u, v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(0,10)

print(G.adj)





nx.prim_mst_edges(G, True, weight='weight',
                   keys=True, data=True, ignore_nan=False)

print(G.adj)