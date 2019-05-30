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
"""
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

"""
from randomGraph import generateRandomConnectedGraph

prim_time = []
krus_time = []
bor_time = []
for i in range(100, 150, 10):
    nodes = i
    edges = i**2

    x = generateRandomConnectedGraph(nodes, nodes)
    k = am.Graph(nodes)
    p = am.GraphB(nodes)

    for (w, u, v) in x[1]:
        k.addEdge(u, v, w)
        p.addEdge(u, v, w)

    ex_edges = edges - (nodes-1)            #determines how many extra edges we'll need to meet our goal

    for i in range(ex_edges):             #adds random edges to graph
        u = random.randint(0, nodes-1)      #picks a random node for src
        v = random.randint(0, nodes-1)      #picks a random node for dest
        w = random.randint(0, 100)             #gets a random weight
        k.addEdge(u, v, w)                  #updates g and h
        p.addEdge(u, v, w)

    x = timeit.timeit(p.PrimMST, number = 1)
    prim_time.append(x)
    print("prim: ", x)
    y = timeit.timeit(k.KruskalMST, number = 1)
    krus_time.append(y)
    print("krus: ", y)
    z = timeit.timeit(k.BoruvkaMST, number=1)
    bor_time.append(z)
    print("bor: ", z)


data1, data2 = prim_time, krus_time
stat, p = ttest_ind(data1, data2)
print("ttest: ", stat, " ", p)

stat, p = f_oneway(data1, data2)
print("Anova: ", stat, " ", p)

from scipy.stats import describe

print("Prim: ", describe(prim_time))
print("Kruskal: ", describe(krus_time))
print("Boruvka: ", describe(bor_time))

plot(prim_time, color = 'blue')
plot(krus_time, color = 'green')
plot(bor_time, color = 'yellow')

show()


"""
file_name = str("final_algs")
f= open(str(file_name +".txt"),"w+")

test = "Small, Sparse Graphs"
f.write(test)

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