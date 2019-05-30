#import networkx as nx
import random
import timeit
#import algorithms as alg
from scipy.stats import ttest_ind, f_oneway
from pylab import plot, show, ion, ioff, subplot, figure, savefig
import gc

def time_wrapper(func):
    def wrapped():
        return func()
    return wrapped
print("Running...")
import algorithms_mod as am


gc.disable()
filename = "text_gen.txt"
f= open(filename)
nodes = int(f.readline())
print(nodes)
edges = int(f.readline())
print(edges)

g = am.Graph(nodes)
h = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    print(u, v, w)
    g.addEdge(int(u), int(v), int(w))
    h.addEdge(int(u), int(v), int(w))


x = timeit.timeit(h.PrimMST, number = 1)
print(x)
y = timeit.timeit(g.KruskalMST, number = 1)
print(y)

"""
filename = "graphs\dense 1000 nodes n^2 edges.txt"
f= open(filename)
nodes = int(f.readline())
print(nodes)
edges = int(f.readline())
print(edges)

g = am.Graph(nodes)
h = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    print(u, v, w)
    g.addEdge(int(u), int(v), int(w))
    h.addEdge(int(u), int(v), int(w))


print("Making first MSTs...")

prim_time = []
kruskal_time = []
boruvka_time = []

for i in range(0, 5):
    # Prim
    wrapped = time_wrapper(h.PrimMST())
    prim_time.append(timeit.timeit(wrapped, number=1))
    print(prim_time[-1])

    # Kruskal
    wrapped = time_wrapper(g.KruskalMST())
    kruskal_time.append(timeit.timeit(wrapped, number=1))
    print(kruskal_time[-1])

data1, data2 = prim_time, kruskal_time
stat, p = ttest_ind(data1, data2)
print("ttest: ", stat, " ", p)

stat, p = f_oneway(data1, data2)
print("Anova: ", stat, " ", p)


plot(prim_time, color = 'blue')
plot(kruskal_time, color = 'green')

show()

"""

"""
print(h)

x = alg.minimum_spanning_tree(G, algorithm='prim')
print(x.edges())


prim_time = []
kruskal_time = []

file_name = str("final_algs")
f= open(str(file_name +".txt"),"w+")

test = "Small, Sparse Graphs"
f.write(test)

for nodes in range(10, 1000, 10):
    edges = nodes
    print("nodes: ", nodes, ". edges: ", edges)
    #Graph Creation
    G = nx.gnm_random_graph(nodes, edges, seed=None, directed=False)

    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = random.randint(1,1000)

    # Prim
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='prim')
    prim_time.append(timeit.timeit(wrapped, number=1))
    print("Prim: ", prim_time[-1])

    #Kruskal
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='kruskal')
    kruskal_time.append(timeit.timeit(wrapped, number =1))
    print("Kruskal: ", kruskal_time[-1])


data1, data2 = prim_time, kruskal_time
stat, p = ttest_ind(data1, data2)
f.write("\nttest prim & kruskal: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))
print("ttest: ", stat, " ", p)

stat, p = f_oneway(data1, data2)
f.write("\nAnova: ")
f.write("stat: " + str(stat) + " ")
f.write("p: " + str(p))
f.write('\n\n')
print("Anova: ", stat, " ", p)

f.write("Prim time: ")
for i in prim_time:
    f.write(str(i)+ ", ")
f.write("\nKruskal time: ")
for i in kruskal_time:
    f.write(str(i)+ ", ")


f.write('\n')

plot(prim_time, color = 'blue')
plot(kruskal_time, color = 'green')

savefig(str(test+"_a.png"))


prim_time.clear()
kruskal_time.clear()
"""