import re
import random

# Class WeightedGraph
class WeightedGraph:
    def __init__(self, G, nodes, edges):

        # initialize the graph
        self.vertices, self.edges = nodes, edges
        # use adjacent matrix to represent the graph
        self.graph = [[0]*self.vertices for _ in range(self.vertices)]

        # populate the graph
        for (u, v) in G.edges():
            w = random.randint(1, 10)
            print(u, v, w)
            self.graph[u][v] = w
            self.graph[v][u] = w
        for u in range(self.vertices):
            for v in range(self.vertices):
                print (self.graph[u][v], end=" ")
            print('\n')

# Union find data structure for quick kruskal algorithm
class UF:
    def __init__(self, N):
        self._id = [i for i in range(N)]

    # judge two node connected or not
    def connected(self, p, q):
        return self._find(p) == self._find(q)

    # quick union two component
    def union(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root

    # find the root of p
    def _find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p



# prim algorithm
def prim(G):
    # initialize the MST and the set X
    MST = set()
    X = set()

    # select an arbitrary vertex to begin with
    X.add(0)
    while len(X) != G.vertices:
        crossing = set()
        # for each element x in X, add the edge (x, k) to crossing if
        # k is not in X
        for x in X:
            for k in range(G.vertices):
                if k not in X and G.graph[x][k] != 0:
                    crossing.add((x, k))
        # find the edge with the smallest weight in crossing
        edge = sorted(crossing, key=lambda e:G.graph[e[0]][e[1]])[0]
        # add this edge to MST
        MST.add(edge)
        # add the new vertex to X
        X.add(edge[1])
    return MST


# kruskal algorithm
def kruskal(G):
    # initialize MST
    MST = set()
    edges = set()
    # collect all edges from graph G
    for j in range(G.vertices):
        for k in range(G.vertices):
            if G.graph[j][k] != 0 and (k, j) not in edges:
                edges.add((j, k))
    # sort all edges in graph G by weights from smallest to largest
    sorted_edges = sorted(edges, key=lambda e:G.graph[e[0]][e[1]])
    uf = UF(G.vertices)
    for e in sorted_edges:
        u, v = e
        # if u, v already connected, abort this edge
        if uf.connected(u, v):
            continue
        # if not, connect them and add this edge to the MST
        uf.union(u, v)
        MST.add(e)
    return MST