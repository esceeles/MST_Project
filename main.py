import networkx as nx
import random
import timeit
import parallel_boruvkas as pb
import algorithms as alg
import matplotlib.pyplot as plt

def time_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
print("Running...")
G = nx.gnm_random_graph(20000, 25000, seed=None, directed=False)
for (u, v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(0,10)

print("Graph:")
print(sorted(G.edges(data=False)))

print('\n')
print("Trees:")

print("Regular:")
#reg = alg.minimum_spanning_tree(G, algorithm='boruvka')
#print(sorted(reg.edges(data=True)))
wrapped= time_wrapper(alg.minimum_spanning_tree, G, algorithm='boruvka')
print(timeit.timeit(wrapped, number=1))

print("Parallel:")
#par = pb.minimum_spanning_tree(G, algorithm='parallel_boruvka')
#print(sorted(par.edges(data=True)))
wrapped= time_wrapper(pb.minimum_spanning_tree, G, algorithm='parallel_boruvka')
print(timeit.timeit(wrapped, number=1))




"""
wrapped= time_wrapper(alg.minimum_spanning_tree, G, algorithm='prim')
print(timeit.timeit(wrapped, number=1))

wrapped= time_wrapper(alg.minimum_spanning_tree, G, algorithm='kruskal')
print(timeit.timeit(wrapped, number=1))
"""

"""
#wrapped = wrapper(function, arguments)
#timeit.timeit(function, number of times to execute function)

from pylab import plot, show, ion, ioff
#x = random(1000)
#plot(x)
#show() # Figure now shows correctly but console blocks
# Closing the figure returns control back to the console
#ion() # turn on interactive plotting
#plot(x) # returns control back to the console immediately

prim_time = []
kruskal_time = []
boruvka_time = []


print("Entering For Loop...")
for i in range(997, 1000):
    print("nodes: ", i, ". edges: ", i)
    #Graph Creation
    G = nx.gnm_random_graph(i, i, seed=None, directed=False)
    for (u, v) in G.edges():
        G.edges[u,v]['weight'] = random.randint(0,10)
    #print(sorted(G.edges(data=True)))

    #nx.draw(G)  # default spring_layout
    #nx.draw(G, pos=nx.spectral_layout(G), nodecolor='r', edge_color='b')
    #plt.show()

    #Kruskal
    wrapped = time_wrapper(nx.minimum_spanning_tree, G, algorithm='kruskal')
    kruskal_time.append(timeit.timeit(wrapped, number =1))

    #Prim
    wrapped = time_wrapper(nx.minimum_spanning_tree, G, algorithm='prim')
    prim_time.append(timeit.timeit(wrapped, number=1))
"""
"""
    #Boruvka
    wrapped = time_wrapper(nx.minimum_spanning_tree, G, algorithm='boruvka')
    boruvka_time.append(timeit.timeit(wrapped, number=1))
"""
"""
    print('\n')


plot(prim_time)
show()
plot(kruskal_time)
show()
plot(boruvka_time)
show()
"""