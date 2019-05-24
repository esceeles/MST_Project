from operator import itemgetter
from math import isnan

from networkx.utils import UnionFind, not_implemented_for

def kruskal_mst_edges(G, minimum, weight='weight',
                      keys=True, data=True, ignore_nan=False):

    subtrees = UnionFind()
    if G.is_multigraph():
        edges = G.edges(keys=True, data=True)

        def filter_nan_edges(edges=edges, weight=weight):
            sign = 1 if minimum else -1
            for u, v, k, d in edges:
                wt = d.get(weight, 1) * sign
                if isnan(wt):
                    if ignore_nan:
                        continue
                    msg = "NaN found as an edge weight. Edge %s"
                    raise ValueError(msg % ((u, v, k, d),))
                yield wt, u, v, k, d
    else:
        edges = G.edges(data=True)

        def filter_nan_edges(edges=edges, weight=weight):
            sign = 1 if minimum else -1
            for u, v, d in edges:
                wt = d.get(weight, 1) * sign
                if isnan(wt):
                    if ignore_nan:
                        continue
                    msg = "NaN found as an edge weight. Edge %s"
                    raise ValueError(msg % ((u, v, d),))
                yield wt, u, v, d
    edges = sorted(filter_nan_edges(), key=itemgetter(0))
    # Multigraphs need to handle edge keys in addition to edge data.
    if G.is_multigraph():
        for wt, u, v, k, d in edges:
            if subtrees[u] != subtrees[v]:
                if keys:
                    if data:
                        yield u, v, k, d
                    else:
                        yield u, v, k
                else:
                    if data:
                        yield u, v, d
                    else:
                        yield u, v
                subtrees.union(u, v)
    else:
        for wt, u, v, d in edges:
            if subtrees[u] != subtrees[v]:
                if data:
                    yield (u, v, d)
                else:
                    yield (u, v)
                subtrees.union(u, v)