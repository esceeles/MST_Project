# -*- coding: utf-8 -*-
#    Copyright (C) 2017 NetworkX Developers
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    Loïc Séguin-C. <loicseguin@gmail.com>
#    All rights reserved.
#    BSD license.
"""
Algorithms for calculating min/max spanning trees/forests.

"""
from heapq import heappop, heappush
from operator import itemgetter
from itertools import count
from networkx.utils import UnionFind

__all__ = [
    'minimum_spanning_edges',
    'minimum_spanning_tree',
]

def kruskal_mst_edges(G, minimum, weight='weight', data=True):

    subtrees = UnionFind()

    edges = G.edges(data=True)

    def filter_nan_edges(edges=edges, weight=weight):
        sign = 1 if minimum else -1
        for u, v, d in edges:
            wt = d.get(weight, 1) * sign
            yield wt, u, v, d
    edges = sorted(filter_nan_edges(), key=itemgetter(0))
    # Multigraphs need to handle edge keys in addition to edge data.
    for wt, u, v, d in edges:
        if subtrees[u] != subtrees[v]:
            if data:
                yield (u, v, d)
            else:
                yield (u, v)
            subtrees.union(u, v)



def prim_mst_edges(G, minimum, weight='weight', data=True):


    push = heappush
    pop = heappop

    nodes = list(G)
    c = count()

    sign = 1 if minimum else -1

    while nodes:
        u = nodes.pop(0)
        frontier = []
        visited = [u]


        for v, d in G.adj[u].items():
            wt = d.get(weight, 1) * sign
            push(frontier, (wt, next(c), u, v, d))
        while frontier:
            W, _, u, v, d = pop(frontier)
            if v in visited:
                continue
            # Multigraphs need to handle edge keys in addition to edge data.
            if data:
                yield u, v, d
            else:
                yield u, v
            # update frontier
            visited.append(v)
            nodes.remove(v)
            for w, d2 in G.adj[v].items():
                if w in visited:
                    continue
                new_weight = d2.get(weight, 1) * sign
                push(frontier, (new_weight, next(c), v, w, d2))


ALGORITHMS = {
    'prim': prim_mst_edges,
    'kruskal': kruskal_mst_edges
}

def minimum_spanning_edges(G, algorithm, weight='weight', data=True):

    algo = ALGORITHMS[algorithm]

    return algo(G, minimum=True, weight=weight, data=data)


def minimum_spanning_tree(G, weight='weight', algorithm='kruskal'):

    edges = minimum_spanning_edges(G, algorithm, weight, data=True)
    T = G.__class__()  # Same graph class as G
    T.graph.update(G.graph)
    T.add_nodes_from(G.nodes.items())
    T.add_edges_from(edges)
    return T
