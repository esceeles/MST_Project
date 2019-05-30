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
import networkx as nx

__all__ = [
    'minimum_spanning_edges',
    'minimum_spanning_tree',
]

from threading import Thread

def boruvka_threads(G, minimum=True, weight='weight',
                      keys=False, data=True, ignore_nan=False):

    forest = UnionFind(G)

    def best_edge(component):
        sign = 1 if minimum else -1
        minwt = float('inf')
        boundary = None
        for e in nx.edge_boundary(G, component, data=True):
            wt = e[-1].get(weight, 1) * sign
            if wt < minwt:
                minwt = wt
                boundary = e
        return boundary

    def best_edge_list(component, edgelist):
        sign = 1 if minimum else -1
        minwt = float('inf')
        boundary = None
        for e in nx.edge_boundary(G, component, data=True):
            wt = e[-1].get(weight, 1) * sign
            if wt < minwt:
                minwt = wt
                boundary = e
        edgelist.append(boundary)

    best_edges = []
    for component in forest.to_sets():

        process = Thread(target=best_edge_list, args=[component, best_edges])
        process.start()

    best_edges = [edge for edge in best_edges if edge is not None]

    while best_edges:

        best_edges_a = []
        for component in forest.to_sets():
            process = Thread(target = best_edge_list, args = [component, best_edges_a])
            process.start()

        best_edges = [edge for edge in best_edges_a if edge is not None]

        for u, v, d in best_edges:
            if forest[u] != forest[v]:
                if data:
                    yield u, v, d
                else:
                    yield u, v
                forest.union(u, v)

def boruvka_mst_edges(G, minimum=True, weight='weight', keys=False, data=True, ignore_nan=False):

    forest = UnionFind(G)

    def best_edge(component):
        sign = 1 if minimum else -1
        minwt = float('inf')
        boundary = None
        for e in nx.edge_boundary(G, component, data=True):
            wt = e[-1].get(weight, 1) * sign
            if wt < minwt:
                minwt = wt
                boundary = e
        return boundary

    best_edges = (best_edge(component) for component in forest.to_sets())

    best_edges = [edge for edge in best_edges if edge is not None]

    while best_edges:

        best_edges = (best_edge(component) for component in forest.to_sets())

        best_edges = [edge for edge in best_edges if edge is not None]

        for u, v, d in best_edges:
            if forest[u] != forest[v]:
                if data:
                    yield u, v, d
                else:
                    yield u, v
                forest.union(u, v)


def MakeSet(x):
    x.parent = x
    x.rank = 0

def Union(x, y):
    xRoot = Find(x)
    yRoot = Find(y)
    if xRoot.rank > yRoot.rank:
        yRoot.parent = xRoot
    elif xRoot.rank < yRoot.rank:
        xRoot.parent = yRoot
    elif xRoot != yRoot:  # Unless x and y are already in same set, merge them
        yRoot.parent = xRoot
        xRoot.rank = xRoot.rank + 1

def Find(x):
    if x.parent == x:
        return x
    else:
        x.parent = Find(x.parent)
        return x.parent




def kruskal_mst_edges(G, minimum, weight='weight', data=True):

    subtrees = UnionFind()

    edges = G.edges(data=True)

    def filter_nan_edges(edges=edges, weight=weight):
        sign = 1 if minimum else -1
        for u, v, d in edges:
            wt = d.get(weight, 1) * sign
            yield wt, u, v, d
    edges = sorted(filter_nan_edges(), key=itemgetter(0))
    for wt, u, v, d in edges:
        if subtrees[u] != subtrees[v]:
            if data:
                yield (u, v, d)
            else:
                yield (u, v)
            subtrees.union(u, v)



def prim_mst_edges(G, minimum, weight='weight', data=True):

    push = heappush         #allows us to use words push and pop in place of built in heapq algrs: heappush and heappop
    pop = heappop

    nodes = list(G)         #add all nodes of G to list, nodes
    c = count()

    #sign = 1 if minimum else -1

    while nodes:
        print("nodes: ", nodes)
        u = nodes.pop(0)
        print("u: ", u)
        frontier = []
        visited = [u]
        print("frontier: ", frontier)
        print("visited: ", visited)

        for v, d in G.adj[u].items():
            print("v, d: ", v, d)
            wt = d.get(weight, 1)
            print(wt)
            push(frontier, (wt, next(c), u, v, d))
            print("frontier: ", frontier)
        while frontier:
            W, _, u, v, d = pop(frontier)
            if v in visited:
                print("continuing")
                continue
            if data:
                print("data", u, v, d)
                yield u, v, d
            else:
                print("else", u, v)
                yield u, v
            # update frontier
            visited.append(v)
            nodes.remove(v)
            for w, d2 in G.adj[v].items():
                if w in visited:
                    continue
                new_weight = d2.get(weight, 1)
                push(frontier, (new_weight, next(c), v, w, d2))


ALGORITHMS = {
    'prim': prim_mst_edges,
    'kruskal': kruskal_mst_edges,
    'boruvka':boruvka_mst_edges,
    'parallel': boruvka_threads
}

def minimum_spanning_edges(G, algorithm, weight='weight', data=True):

    algo = ALGORITHMS[algorithm]

    return algo(G, minimum=True, weight=weight, data=data)


def minimum_spanning_tree(G, weight='weight', algorithm='kruskal'):

    edges = minimum_spanning_edges(G, algorithm, weight, data=True)
    print("edges: ", edges)
    T = G.__class__()  # Same graph class as G
    T.graph.update(G.graph)
    T.add_nodes_from(G.nodes.items())
    T.add_edges_from(edges)
    return T
