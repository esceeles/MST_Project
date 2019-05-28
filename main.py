import networkx as nx
import random
import timeit
import algorithms as alg
from scipy.stats import ttest_ind, f_oneway
from pylab import plot, show, ion, ioff, subplot, figure, savefig
import gc

def time_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
print("Running...")


gc.disable()

prim_time = []
kruskal_time = []
boruvka_time = []
parallel_time = []

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

    #Boruvka
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='boruvka')
    boruvka_time.append(timeit.timeit(wrapped, number =1))
    print("Boruvka: ", boruvka_time[-1])

    #Par
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='parallel')
    parallel_time.append(timeit.timeit(wrapped, number =1))
    print("Parallel: ", parallel_time[-1])


data1, data2, data3, data4 = prim_time, kruskal_time, boruvka_time, parallel_time
stat, p = ttest_ind(data1, data2)
f.write("\nttest prim & kruskal: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))
print("ttest: ", stat, " ", p)

stat, p = f_oneway(data1, data2, data3)
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
f.write("Boruvka time: ")
for i in boruvka_time:
    f.write(str(i)+ ", ")
f.write("\nParallel time: ")
for i in parallel_time:
    f.write(str(i)+ ", ")


f.write('\n')

plot(prim_time, color = 'blue')
plot(kruskal_time, color = 'green')
plot(boruvka_time, color = 'yellow')
plot(parallel_time, color = 'red')

savefig(str(test+"_a.png"))


prim_time.clear()
kruskal_time.clear()
boruvka_time.clear()
parallel_time.clear()



test = "Small, Dense Graphs"
f.write(test)
for nodes in range(10, 1000, 10):
    edges = nodes**2
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

    #Boruvka
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='boruvka')
    boruvka_time.append(timeit.timeit(wrapped, number =1))
    print("Boruvka: ", boruvka_time[-1])

    #Par
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='parallel')
    parallel_time.append(timeit.timeit(wrapped, number =1))
    print("Parallel: ", parallel_time[-1])


data1, data2, data3, data4 = prim_time, kruskal_time, boruvka_time, parallel_time
stat, p = ttest_ind(data1, data2)
f.write("\nttest prim & kruskal: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))
print("ttest: ", stat, " ", p)

stat, p = f_oneway(data1, data2, data3)
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
f.write("Boruvka time: ")
for i in boruvka_time:
    f.write(str(i)+ ", ")
f.write("\nParallel time: ")
for i in parallel_time:
    f.write(str(i)+ ", ")


f.write('\n')

plot(prim_time, color = 'blue')
plot(kruskal_time, color = 'green')
plot(boruvka_time, color = 'yellow')
plot(parallel_time, color = 'red')

savefig(str(test+"_a.png"))


prim_time.clear()
kruskal_time.clear()
boruvka_time.clear()
parallel_time.clear()


test = "Large, Sparse Graphs"
f.write(test)
for nodes in range(100, 10000, 100):
    edges = nodes + 100
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

    #Boruvka
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='boruvka')
    boruvka_time.append(timeit.timeit(wrapped, number =1))
    print("Boruvka: ", boruvka_time[-1])

    #Par
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='parallel')
    parallel_time.append(timeit.timeit(wrapped, number =1))
    print("Parallel: ", parallel_time[-1])


data1, data2, data3, data4 = prim_time, kruskal_time, boruvka_time, parallel_time
stat, p = ttest_ind(data1, data2)
f.write("\nttest prim & kruskal: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))
print("ttest: ", stat, " ", p)

stat, p = f_oneway(data1, data2, data3)
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
f.write("Boruvka time: ")
for i in boruvka_time:
    f.write(str(i)+ ", ")
f.write("\nParallel time: ")
for i in parallel_time:
    f.write(str(i)+ ", ")


f.write('\n')

plot(prim_time, color = 'blue')
plot(kruskal_time, color = 'green')
plot(boruvka_time, color = 'yellow')
plot(parallel_time, color = 'red')

savefig(str(test+"_a.png"))


prim_time.clear()
kruskal_time.clear()
boruvka_time.clear()
parallel_time.clear()


test = "Large, Dense Graphs"
f.write(test)
for nodes in range(100, 10000, 100):
    edges = nodes ** 2
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

    #Boruvka
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='boruvka')
    boruvka_time.append(timeit.timeit(wrapped, number =1))
    print("Boruvka: ", boruvka_time[-1])

    #Par
    wrapped = time_wrapper(alg.minimum_spanning_tree, G, algorithm='parallel')
    parallel_time.append(timeit.timeit(wrapped, number =1))
    print("Parallel: ", parallel_time[-1])


data1, data2, data3, data4 = prim_time, kruskal_time, boruvka_time, parallel_time
stat, p = ttest_ind(data1, data2)
f.write("\nttest prim & kruskal: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))
print("ttest: ", stat, " ", p)

stat, p = f_oneway(data1, data2, data3)
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
f.write("Boruvka time: ")
for i in boruvka_time:
    f.write(str(i)+ ", ")
f.write("\nParallel time: ")
for i in parallel_time:
    f.write(str(i)+ ", ")


f.write('\n')

plot(prim_time, color = 'blue')
plot(kruskal_time, color = 'green')
plot(boruvka_time, color = 'yellow')
plot(parallel_time, color = 'red')

savefig(str(test+"_a.png"))


prim_time.clear()
kruskal_time.clear()
boruvka_time.clear()
parallel_time.clear()


test = "Prim as density changes"
test = "Kruskal as density changes"
test = "Boruvka as density changes"
test = "Parallel Boruvka as density changes"

