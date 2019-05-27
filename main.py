import networkx as nx
import random
import timeit
#import parallel_boruvkas as pb
import algorithms as alg
#import matplotlib.pyplot as plt
#import algorithms_mod as am
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

file_name = str("only_sig_prim_better")
f= open(str(file_name +".txt"),"w+")

f.write("40 nodes ran 100 times, edges: i^3")
for i in range(3, 103, 1):
        print("nodes: ", i, ". edges: ", (i**2))
        #Graph Creation
        G = nx.gnm_random_graph(40, (40**2), seed=None, directed=False)

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


        krus = alg.minimum_spanning_tree(G, algorithm='kruskal')
        pri = alg.minimum_spanning_tree(G, algorithm='prim')
        print(sorted(krus.edges(data= True)))
        print(sorted(pri.edges(data=True)))

        krus_weight = 0
        pri_weight = 0
        for (u,v) in krus.edges():
            krus_weight += krus.edges[u,v]['weight']

        for (u,v) in pri.edges():
            pri_weight += pri.edges[u,v]['weight']

        print(krus_weight)
        print(pri_weight)


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
#plot(boruvka_time, color = 'yellow')
#plot(parallel_time, color = 'red')

savefig(str(file_name+"_a.png"))

prim_time.clear()
kruskal_time.clear()
boruvka_time.clear()
#parallel_time.clear()

print(prim_time)
print(kruskal_time)
print(boruvka_time)
#print(parallel_time)


"""
start = 0
end = 20000
step = 50

f.write("nodes from 0 to 20000, steps of 50, edges= nodes:\n\n")

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

savefig(str(file_name+"_b.png"))


prim_time.clear()
kruskal_time.clear()

print(prim_time)
print(kruskal_time)

f.write("\n\ngraph has 0 to 20000 nodes, edges = nodes^2 at intervals of 50\n\n")

start = 0
end = 20000
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
f.write('\n\n')
print("Anova: ", stat, " ", p)

#writing to file
f.write("Prim time: ")
for i in prim_time:
    f.write(str(i)+ ", ")
f.write("\nKruskal time: ")
for i in kruskal_time:
    f.write(str(i)+ ", ")

f.write('\n')
print(prim_time, '\n')
print(kruskal_time, '\n')


#making plot and saving to file
plot(prim_time, color = 'blue')
plot(kruskal_time, color = 'green')

savefig(str(file_name+"_c.png"))
#show()
"""

f.close()