#import networkx as nx
import random
import timeit
#import algorithms as alg
from scipy.stats import ttest_ind, f_oneway, ttest_rel, normaltest
import matplotlib.pyplot as plt
#from pylab import plot, show, ion, ioff, subplot, figure, savefig, subplots
import gc
import math
from randomGraph import generateRandomConnectedGraph
import algorithms_mod as am


def time_wrapper(func):
    def wrapped():
        return func()
    return wrapped
print("Running...")

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
"""

prim_time = []
krus_time = []
bor_time = []
log_time = []
nodes_list = []
edges_list = []

nodes = 1000
edges = nodes * 2
#nodes_list.append(i)
#edges_list.append(i * 5)
x = generateRandomConnectedGraph(nodes, nodes)
k = am.Graph(nodes)
p = am.GraphB(nodes)

for (w, u, v) in x[1]:
    k.addEdge(u, v, w)
    p.addEdge(u, v, w)

ex_edges = edges - (nodes - 1)  # determines how many extra edges we'll need to meet our goal

for i in range(ex_edges):  # adds random edges to graph
    u = random.randint(0, nodes - 1)  # picks a random node for src
    v = random.randint(0, nodes - 1)  # picks a random node for dest
    w = random.randint(0, 100)  # gets a random weight
    k.addEdge(u, v, w)  # updates g and h
    p.addEdge(u, v, w)

for i in range(10, 3000, 10):
    nodes_list.append(100)
    """
"""
    nodes = 1000
    edges = i*5
    nodes_list.append(i)
    edges_list.append(i*5)
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
    """
"""
    x = timeit.timeit(p.PrimMST, number = 1)
    prim_time.append(x)
    print("prim: ", x)
    y = timeit.timeit(k.KruskalMST, number = 1)
    krus_time.append(y)
    print("krus: ", y)

    z = timeit.timeit(k.BoruvkaMST, number=1)
    bor_time.append(z)
    print("bor: ", z)

    log = edges * (math.log10(nodes))
    log_time.append(log)


plt.hist(prim_time)
plt.show()
plt.hist(krus_time)
plt.show()
data1, data2 = prim_time, krus_time
stat, p = ttest_ind(data1, data2)
print("ind ttest: ", stat, " ", p)

stat, p = normaltest(data1)
print("data1: ", stat, p)
stat, p = normaltest(data2)
print("data2: ", stat, p)

from scipy.stats import describe

print("Prim: ", describe(prim_time))
print("Kruskal: ", describe(krus_time))
#print("Boruvka: ", describe(bor_time))


all_time = []
all_time.append(list(krus_time))
all_time.append(list(prim_time))
all_time.append(list(bor_time))
#all_time.append(list(log_time))

print(len(all_time))
print(len(nodes_list))
plt.plot(prim_time)
plt.plot(krus_time)
#plt.show()

fig, ax = plt.subplots()
ax.stackplot(nodes_list, all_time, labels = ["krus", "prim", "bor"])
ax.set_title('growth in time over nodes')
ax.legend(loc='upper left')
ax.set_ylabel('time')
ax.set_xlabel('nodes')
#ax.set_ylim(ymin= 900, ymax = 1100)
fig.tight_layout()
#plt.show()

ax.set_title("thing")

prim_growth = []
krus_growth = []
log_growth = []
stat_growth = []
t_growth = []
for i in range(len(prim_time)-1):
    g = prim_time[i+1] - prim_time[i]
    g = g/prim_time[i+1]
    g = g * 100
    prim_growth.append(g)
    g = krus_time[i + 1] - krus_time[i]
    g = g / krus_time[i + 1]
    g = g * 100
    krus_growth.append(g)
    g = log_time[i + 1] - log_time[i]
    g = g / log_time[i + 1]
    g = g * 100
    log_growth.append(g)

print(prim_growth)
print(krus_growth)
plt.plot(prim_growth, color= 'green')
plt.plot(krus_growth, color= 'blue')
plt.plot(log_growth, color = 'red')
#plt.show()
"""
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