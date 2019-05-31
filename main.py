#import networkx as nx
import random
import timeit
#import algorithms as alg
from scipy.stats import ttest_ind, f_oneway, ttest_rel, normaltest
import matplotlib.pyplot as plt
from pylab import plot, show, ion, ioff, subplot, figure, savefig, subplots
import gc
import math
from randomGraph import multigraph
import algorithms_mod as am
from scipy.stats import describe
import statistics

def time_wrapper(func):
    def wrapped():
        return func()
    return wrapped

print("Running...")

gc.disable()


prim_time = []
krus_time = []
bor_time = []
log_time = []
nodes_list = []
edges_list = []



##############readfile and build graph#################

filename = "small_sparse.txt"
f= open(filename)
nodes = int(f.readline())
print(nodes)
edges = int(f.readline())
print(edges)

ssk = am.Graph(nodes)
ssp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    print(u, v, w)
    ssk.addEdge(int(u), int(v), int(w))
    ssp.addEdge(int(u), int(v), int(w))
f.close()
########################################################3

##############readfile and build graph#################

filename = "small_dense.txt"
f= open(filename)
nodes = int(f.readline())
print(nodes)
edges = int(f.readline())
print(edges)

sdk = am.Graph(nodes)
sdp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    print(u, v, w)
    sdk.addEdge(int(u), int(v), int(w))
    sdp.addEdge(int(u), int(v), int(w))

f.close()
########################################################3

##############readfile and build graph#################

filename = "med_sparse.txt"
f= open(filename)
nodes = int(f.readline())
print(nodes)
edges = int(f.readline())
print(edges)

msk = am.Graph(nodes)
msp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    print(u, v, w)
    msk.addEdge(int(u), int(v), int(w))
    msp.addEdge(int(u), int(v), int(w))
f.close()
########################################################3

##############readfile and build graph#################

filename = "med_dense.txt"
f= open(filename)
nodes = int(f.readline())
print(nodes)
edges = int(f.readline())
print(edges)

mdk = am.Graph(nodes)
mdp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    print(u, v, w)
    mdk.addEdge(int(u), int(v), int(w))
    mdp.addEdge(int(u), int(v), int(w))

f.close()
########################################################3

##############readfile and build graph#################

filename = "large_sparse.txt"
f= open(filename)
nodes = int(f.readline())
print(nodes)
edges = int(f.readline())
print(edges)

lsk = am.Graph(nodes)
lsp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    print(u, v, w)
    lsk.addEdge(int(u), int(v), int(w))
    lsp.addEdge(int(u), int(v), int(w))

f.close()
########################################################3

"""
##############readfile and build graph#################

filename = "large_dense.txt"
f= open(filename)
nodes = int(f.readline())
print(nodes)
edges = int(f.readline())
print(edges)

ldk = am.Graph(nodes)
ldp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    print(u, v, w)
    ldk.addEdge(int(u), int(v), int(w))
    ldp.addEdge(int(u), int(v), int(w))

f.close()
########################################################3
"""
#################writes mean time of execution on small/med/large sparse/dense graphs######
###################tests small/med/large sparse/dense graphs######################
sspt = []
sskt = []
ssbt = []
sdpt = []
sdkt = []
sdbt = []
mspt = []
mskt = []
msbt = []
mdpt = []
mdkt = []
mdbt = []
lspt = []
lskt = []
lsbt = []
#ldpt = []
#ldkt = []
#ldbt = []

for i in range(0, 10):
    #small sparse
    x = timeit.timeit(ssp.PrimMST, number = 1)
    sspt.append(x)

    x = timeit.timeit(ssk.KruskalMST, number = 1)
    sskt.append(x)

    x = timeit.timeit(ssk.BoruvkaMST, number=1)
    ssbt.append(x)

    #small dense
    x = timeit.timeit(sdp.PrimMST, number = 1)
    sdpt.append(x)

    x = timeit.timeit(sdk.KruskalMST, number = 1)
    sdkt.append(x)

    x = timeit.timeit(sdk.BoruvkaMST, number=1)
    sdbt.append(x)

    #med sparse
    x = timeit.timeit(msp.PrimMST, number = 1)
    mspt.append(x)

    x = timeit.timeit(msk.KruskalMST, number = 1)
    mskt.append(x)

    x = timeit.timeit(msk.BoruvkaMST, number=1)
    msbt.append(x)

    #med dense
    x = timeit.timeit(mdp.PrimMST, number = 1)
    mdpt.append(x)

    x = timeit.timeit(mdk.KruskalMST, number = 1)
    mdkt.append(x)

    x = timeit.timeit(mdk.BoruvkaMST, number=1)
    mdbt.append(x)

    #large spares
    x = timeit.timeit(lsp.PrimMST, number = 1)
    lspt.append(x)

    x = timeit.timeit(lsk.KruskalMST, number = 1)
    lskt.append(x)

    x = timeit.timeit(lsk.BoruvkaMST, number=1)
    lsbt.append(x)

    """
    #large dense
    x = timeit.timeit(ldp.PrimMST, number = 1)
    ldpt.append(x)

    x = timeit.timeit(ldk.KruskalMST, number = 1)
    ldkt.append(x)

    x = timeit.timeit(ldk.BoruvkaMST, number=1)
    ldbt.append(x)
    """

file_name = str("small_med_large_sparse_dense")
savefig(str(file_name+".png"))
f= open(str(file_name +".txt"),"w+")
f.write(file_name)
f.write('\n')

f.write(str("sparse = .001, dense = .8"))
f.write('\n')

f.write(str("\nssp: "+ str(statistics.mean(sspt))))
f.write(str("\nssk: "+ str(statistics.mean(sskt))))
f.write(str("\nssb: "+ str(statistics.mean(ssbt))))
f.write(str("\nsdp: "+ str(statistics.mean(sdpt))))
f.write(str("\nsdk: "+ str(statistics.mean(sskt))))
f.write(str("\nsdb: "+ str(statistics.mean(sdbt))))
f.write(str("\nmsp: "+ str(statistics.mean(mspt))))
f.write(str("\nmsk: "+ str(statistics.mean(mskt))))
f.write(str("\nmsb: "+ str(statistics.mean(msbt))))
f.write(str("\nmdp: "+ str(statistics.mean(mdpt))))
f.write(str("\nmdk: "+ str(statistics.mean(mdkt))))
f.write(str("\nmdb: "+ str(statistics.mean(mdbt))))
f.write(str("\nlsp: "+ str(statistics.mean(lspt))))
f.write(str("\nlsk: "+ str(statistics.mean(sskt))))
f.write(str("\nlsb: "+ str(statistics.mean(lsbt))))
#f.write(str("\nldp: "+ str(statistics.mean(ldpt))))
#f.write(str("\nldk: "+ str(statistics.mean(ldkt))))
#f.write(str("\nldb: "+ str(statistics.mean(ldbt))))
f.write('\n')

f.close()




#################comparing avg performance with eachother for significant differences##############
f.write("\ncomparing avg performance with eachother for significant difference... not ttest, anova:\n")

data1, data2, data3 = sspt, sskt, ssbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nttest small sparse: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))

data1, data2, data3 = sdpt, sdkt, sdbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nttest small dense: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))


data1, data2, data3 = mdpt, mdkt, mdbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nttest medium dense: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))

data1, data2, data3 = mspt, mskt, msbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nttest medium sparse: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))

data1, data2, data3 = lspt, lskt, lsbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nttest large sparse: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))

f.close()




"""

###############writing to file###################
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




#######################################

prim_time.clear()
kruskal_time.clear()
"""