import networkx as nx
import random
import timeit
import parallel_boruvkas as pb
import algorithms as alg
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, f_oneway
from pylab import plot, show, ion, ioff, subplot, figure, savefig
import gc

def time_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
print("Running...")


gc.disable()

start = 0
end = 2000
step = 50


prim_time = []
kruskal_time = []
boruvka_time = []
parallel_time = []

file_name = str("first_test_wo_gc.txt")
f= open(file_name,"w+")

f.write("nodes from 0 to 2000, steps of 50, edges= nodes:\n\n")

for i in range(start, end, step):
    print("nodes: ", i, ". edges: ", i)
    #Graph Creation
    G = nx.gnm_random_graph(i, i, seed=None, directed=False)
    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = random.randint(0,10)
    #print(sorted(G.edges(data=True)))

    #Kruskal
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='kruskal')
    kruskal_time.append(timeit.timeit(wrapped, number =1))

    #Prim
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='prim')
    prim_time.append(timeit.timeit(wrapped, number=1))


data1, data2 = prim_time, kruskal_time
stat, p = ttest_ind(data1, data2)
f.write("\nttest: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))
print("ttest: ", stat, " ", p)
stat, p = f_oneway(data1, data2)
f.write("\nAnova: ")
f.write("stat: " + str(stat) + " ")
f.write("p: " + str(p))
f.write('\n')
print("Anova: ", stat, " ", p)

f.write("Prim time: ")
for i in prim_time:
    f.write(str(i)+ ", ")
f.write("\nKruskal time: ")
for i in kruskal_time:
    f.write(str(i)+ ", ")
f.write('\n')

prim_time.clear()
kruskal_time.clear()
boruvka_time = []
parallel_time = []


f.write("\n\ngraph has 0 to 2000 nodes, edges = nodes^2 at intervals of 100\n\n")

start = 0
end = 2000
step = 50
for i in range(start, end, step):
    print("nodes: ", i, ". edges: ", i^2)
    #Graph Creation
    G = nx.gnm_random_graph(i, i^2, seed=None, directed=False)
    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = random.randint(0,10)
    #print(sorted(G.edges(data=True)))

    #Kruskal
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='kruskal')
    kruskal_time.append(timeit.timeit(wrapped, number =1))

    #Prim
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='prim')
    prim_time.append(timeit.timeit(wrapped, number=1))
    """
    #Boruvka
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='boruvka')
    boruvka_time.append(timeit.timeit(wrapped, number=1))

    wrapped = time_wrapper(pb.minimum_spanning_tree, G, algorithm='parallel_boruvka')
    parallel_time.append(timeit.timeit(wrapped, number=1))
    print('\n')
    """

data1, data2 = prim_time, kruskal_time
stat, p = ttest_ind(data1, data2)
f.write("ttest: ")
f.write(str(stat) + " ")
f.write(str(p))
stat, p = f_oneway(data1, data2)
f.write("\nAnova: ")
f.write(str(stat) + " ")
f.write(str(p))
f.write('\n')

#writing to file
f.write("Prim time: ")
for i in prim_time:
    f.write(str(i)+ ", ")
f.write("\nKruskal time: ")
for i in kruskal_time:
    f.write(str(i)+ ", ")
f.write("\nBoruvka time: ")
for i in boruvka_time:
    f.write(str(i)+ ", ")
f.write("\nParallel Time: ")
for i in parallel_time:
    f.write(str(i)+ ", ")
f.write('\n')
print(prim_time, '\n')
print(kruskal_time, '\n')
print(boruvka_time, '\n')
print(parallel_time, '\n')

#making plot and saving to file
plot(prim_time, color = 'blue')
plot(kruskal_time, color = 'green')
plot(boruvka_time, color = 'yellow')
plot(parallel_time, color = 'red')

savefig(str(file_name+".png"))
#show()


f.close()