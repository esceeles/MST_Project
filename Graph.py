from __future__ import division
import warnings
from copy import deepcopy
from collections.abc import Mapping

import networkx as nx
from networkx.classes.coreviews import AtlasView, AdjacencyView
from networkx.classes.reportviews import NodeView, EdgeView, DegreeView
from networkx.exception import NetworkXError
import networkx.convert as convert
from networkx.utils import pairwise


class Graph(object):

    node_dict_factory = dict
    node_attr_dict_factory = dict
    adjlist_outer_dict_factory = dict
    adjlist_inner_dict_factory = dict
    edge_attr_dict_factory = dict
    graph_attr_dict_factory = dict

    def to_directed_class(self):
        return nx.DiGraph

    def to_undirected_class(self):
        return Graph

def __init__(self, incoming_graph_data=None, **attr):

        self.graph_attr_dict_factory = self.graph_attr_dict_factory
        self.node_dict_factory = self.node_dict_factory
        self.node_attr_dict_factory = self.node_attr_dict_factory
        self.adjlist_outer_dict_factory = self.adjlist_outer_dict_factory
        self.adjlist_inner_dict_factory = self.adjlist_inner_dict_factory
        self.edge_attr_dict_factory = self.edge_attr_dict_factory

        self.graph = self.graph_attr_dict_factory()   # dictionary for graph attributes
        self._node = self.node_dict_factory()  # empty node attribute dict
        self._adj = self.adjlist_outer_dict_factory()  # empty adjacency dict
        # attempt to load graph with data
        if incoming_graph_data is not None:
            convert.to_networkx_graph(incoming_graph_data, create_using=self)
        # load graph attributes (must be after convert)
        self.graph.update(attr)


    @property
    def adj(self):
        return AdjacencyView(self._adj)

    @property
    def name(self):
        return self.graph.get('name', '')

    @name.setter
    def name(self, s):
        self.graph['name'] = s

    def __str__(self):
        return self.name

    def __iter__(self):
        return iter(self._node)


    def __contains__(self, n):
        try:
            return n in self._node
        except TypeError:
            return False


    def __len__(self):
        return len(self._node)


    def __getitem__(self, n):
        return self.adj[n]


    def add_node(self, node_for_adding, **attr):
        if node_for_adding not in self._node:
            self._adj[node_for_adding] = self.adjlist_inner_dict_factory()
            attr_dict = self._node[node_for_adding] = self.node_attr_dict_factory()
            attr_dict.update(attr)
        else:  # update attr even if node already exists
            self._node[node_for_adding].update(attr)


    def add_nodes_from(self, nodes_for_adding, **attr):

        for n in nodes_for_adding:
            try:
                if n not in self._node:
                    self._adj[n] = self.adjlist_inner_dict_factory()
                    attr_dict = self._node[n] = self.node_attr_dict_factory()
                    attr_dict.update(attr)
                else:
                    self._node[n].update(attr)
            except TypeError:
                nn, ndict = n
                if nn not in self._node:
                    self._adj[nn] = self.adjlist_inner_dict_factory()
                    newdict = attr.copy()
                    newdict.update(ndict)
                    attr_dict = self._node[nn] = self.node_attr_dict_factory()
                    attr_dict.update(newdict)
                else:
                    olddict = self._node[nn]
                    olddict.update(attr)
                    olddict.update(ndict)


    def remove_node(self, n):

        adj = self._adj
        try:
            nbrs = list(adj[n])  # list handles self-loops (allows mutation)
            del self._node[n]
        except KeyError:  # NetworkXError if n not in self
            raise NetworkXError("The node %s is not in the graph." % (n,))
        for u in nbrs:
            del adj[u][n]   # remove all edges n-u in graph
        del adj[n]          # now remove node


    def remove_nodes_from(self, nodes):
        adj = self._adj
        for n in nodes:
            try:
                del self._node[n]
                for u in list(adj[n]):   # list handles self-loops
                    del adj[u][n]  # (allows mutation of dict in loop)
                del adj[n]
            except KeyError:
                pass


    @property
    def nodes(self):
        nodes = NodeView(self)
        self.__dict__['nodes'] = nodes
        return nodes

    # for backwards compatibility with 1.x, will be removed for 3.x
    node = nodes

    def add_path(self, nodes, **attr):
        msg = "add_path is deprecated. Use nx.add_path instead."
        warnings.warn(msg, DeprecationWarning)
        return nx.add_path(self, nodes, **attr)

    def add_cycle(self, nodes, **attr):
        msg = "add_cycle is deprecated. Use nx.add_cycle instead."
        warnings.warn(msg, DeprecationWarning)
        return nx.add_cycle(self, nodes, **attr)

    def add_star(self, nodes, **attr):
        msg = "add_star is deprecated. Use nx.add_star instead."
        warnings.warn(msg, DeprecationWarning)
        return nx.add_star(self, nodes, **attr)

    def nodes_with_selfloops(self):
        msg = "nodes_with_selfloops is deprecated." \
              "Use nx.nodes_with_selfloops instead."
        warnings.warn(msg, DeprecationWarning)
        return nx.nodes_with_selfloops(self)

    def number_of_selfloops(self):
        msg = "number_of_selfloops is deprecated." \
              "Use nx.number_of_selfloops instead."
        warnings.warn(msg, DeprecationWarning)
        return nx.number_of_selfloops(self)

    def selfloop_edges(self, data=False, keys=False, default=None):
        msg = "selfloop_edges is deprecated. Use nx.selfloop_edges instead."
        warnings.warn(msg, DeprecationWarning)
        return nx.selfloop_edges(self, data, keys, default)
    # Done with backward compatibility methods for 1.x

    def number_of_nodes(self):
        return len(self._node)


    def order(self):
        return len(self._node)


    def has_node(self, n):
        try:
            return n in self._node
        except TypeError:
            return False


    def add_edge(self, u_of_edge, v_of_edge, **attr):
        u, v = u_of_edge, v_of_edge
        # add nodes
        if u not in self._node:
            self._adj[u] = self.adjlist_inner_dict_factory()
            self._node[u] = self.node_attr_dict_factory()
        if v not in self._node:
            self._adj[v] = self.adjlist_inner_dict_factory()
            self._node[v] = self.node_attr_dict_factory()
        # add the edge
        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict


    def add_edges_from(self, ebunch_to_add, **attr):

        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}  # doesn't need edge_attr_dict_factory
            else:
                raise NetworkXError(
                    "Edge tuple %s must be a 2-tuple or 3-tuple." % (e,))
            if u not in self._node:
                self._adj[u] = self.adjlist_inner_dict_factory()
                self._node[u] = self.node_attr_dict_factory()
            if v not in self._node:
                self._adj[v] = self.adjlist_inner_dict_factory()
                self._node[v] = self.node_attr_dict_factory()
            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
            datadict.update(attr)
            datadict.update(dd)
            self._adj[u][v] = datadict
            self._adj[v][u] = datadict


    def add_weighted_edges_from(self, ebunch_to_add, weight='weight', **attr):

        self.add_edges_from(((u, v, {weight: d}) for u, v, d in ebunch_to_add),
                            **attr)


    def remove_edge(self, u, v):

        try:
            del self._adj[u][v]
            if u != v:  # self-loop needs only one entry removed
                del self._adj[v][u]
        except KeyError:
            raise NetworkXError("The edge %s-%s is not in the graph" % (u, v))


    def remove_edges_from(self, ebunch):

        adj = self._adj
        for e in ebunch:
            u, v = e[:2]  # ignore edge data if present
            if u in adj and v in adj[u]:
                del adj[u][v]
                if u != v:  # self loop needs only one entry removed
                    del adj[v][u]


    def update(self, edges=None, nodes=None):

        if edges is not None:
            if nodes is not None:
                self.add_nodes_from(nodes)
                self.add_edges_from(edges)
            else:
                # check if edges is a Graph object
                try:
                    graph_nodes = edges.nodes
                    graph_edges = edges.edges
                except AttributeError:
                    # edge not Graph-like
                    self.add_edges_from(edges)
                else:  # edges is Graph-like
                    self.add_nodes_from(graph_nodes.data())
                    self.add_edges_from(graph_edges.data())
                    self.graph.update(edges.graph)
        elif nodes is not None:
            self.add_nodes_from(nodes)
        else:
            raise NetworkXError("update needs nodes or edges input")


    def has_edge(self, u, v):

        try:
            return v in self._adj[u]
        except KeyError:
            return False


    def neighbors(self, n):

        try:
            return iter(self._adj[n])
        except KeyError:
            raise NetworkXError("The node %s is not in the graph." % (n,))


    @property
    def edges(self):
        return EdgeView(self)

    def get_edge_data(self, u, v, default=None):

        try:
            return self._adj[u][v]
        except KeyError:
            return default


    def adjacency(self):

        return iter(self._adj.items())


    @property
    def degree(self):
        return DegreeView(self)

    def clear(self):

        self._adj.clear()
        self._node.clear()
        self.graph.clear()


    def is_multigraph(self):
        """Returns True if graph is a multigraph, False otherwise."""
        return False

    def is_directed(self):
        """Returns True if graph is directed, False otherwise."""
        return False

    def fresh_copy(self):
        # remove by v3 if not before
        msg = 'G.fresh_copy is deprecated. Use G.__class__ instead'
        warnings.warn(msg, DeprecationWarning, stacklevel=2)
        return self.__class__()

   def copy(self, as_view=False):
        if as_view is True:
            return nx.graphviews.generic_graph_view(self)
        G = self.__class__()
        G.graph.update(self.graph)
        G.add_nodes_from((n, d.copy()) for n, d in self._node.items())
        G.add_edges_from((u, v, datadict.copy())
                         for u, nbrs in self._adj.items()
                         for v, datadict in nbrs.items())
        return G


    def to_directed(self, as_view=False):

        graph_class = self.to_directed_class()
        if as_view is True:
            return nx.graphviews.generic_graph_view(self, graph_class)
        # deepcopy when not a view
        G = graph_class()
        G.graph.update(deepcopy(self.graph))
        G.add_nodes_from((n, deepcopy(d)) for n, d in self._node.items())
        G.add_edges_from((u, v, deepcopy(data))
                         for u, nbrs in self._adj.items()
                         for v, data in nbrs.items())
        return G


    def to_undirected(self, as_view=False):

        graph_class = self.to_undirected_class()
        if as_view is True:
            return nx.graphviews.generic_graph_view(self, graph_class)
        # deepcopy when not a view
        G = graph_class()
        G.graph.update(deepcopy(self.graph))
        G.add_nodes_from((n, deepcopy(d)) for n, d in self._node.items())
        G.add_edges_from((u, v, deepcopy(d))
                         for u, nbrs in self._adj.items()
                         for v, d in nbrs.items())
        return G


    def subgraph(self, nodes):
        induced_nodes = nx.filters.show_nodes(self.nbunch_iter(nodes))
        # if already a subgraph, don't make a chain
        subgraph = nx.graphviews.subgraph_view
        if hasattr(self, '_NODE_OK'):
            return subgraph(self._graph, induced_nodes, self._EDGE_OK)
        return subgraph(self, induced_nodes)


    def edge_subgraph(self, edges):
        return nx.edge_subgraph(self, edges)


    def size(self, weight=None):

        s = sum(d for v, d in self.degree(weight=weight))
        return s // 2 if weight is None else s / 2


    def number_of_edges(self, u=None, v=None):
        if u is None:
            return int(self.size())
        if v in self._adj[u]:
            return 1
        return 0


    def nbunch_iter(self, nbunch=None):

        if nbunch is None:   # include all nodes via iterator
            bunch = iter(self._adj)
        elif nbunch in self:  # if nbunch is a single node
            bunch = iter([nbunch])
        else:                # if nbunch is a sequence of nodes
            def bunch_iter(nlist, adj):
                try:
                    for n in nlist:
                        if n in adj:
                            yield n
                except TypeError as e:
                    message = e.args[0]
                    # capture error for non-sequence/iterator nbunch.
                    if 'iter' in message:
                        msg = "nbunch is not a node or a sequence of nodes."
                        raise NetworkXError(msg)
                    # capture error for unhashable node.
                    elif 'hashable' in message:
                        msg = "Node {} in sequence nbunch is not a valid node."
                        raise NetworkXError(msg.format(n))
                    else:
                        raise
            bunch = bunch_iter(nbunch, self._adj)
        return bunch
