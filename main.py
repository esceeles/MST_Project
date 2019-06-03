import timeit
from scipy.stats import ttest_ind, f_oneway
import gc
import algorithms_mod as am
import statistics

#wrapper function for timing algorithms runtime
def time_wrapper(func):
    def wrapped():
        return func()
    return wrapped

print("Running...")

#disables garbage collection
gc.disable()

###arrays to store runtimes for each category of graph
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

##############readfile and build graph#################

filename = "graphs/small_sparse.txt"
f= open(filename)
nodes = int(f.readline())
print("reading small sparse")
print(nodes)
edges = int(f.readline())
print(edges)

ssk = am.Graph(nodes)
ssp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    ssk.addEdge(int(u), int(v), int(w))
    ssp.addEdge(int(u), int(v), int(w))
f.close()
########################################################3

##############readfile and build graph#################

filename = "graphs/small_dense.txt"
f= open(filename)
nodes = int(f.readline())
print("reading small_dense")
print(nodes)
edges = int(f.readline())
print(edges)

sdk = am.Graph(nodes)
sdp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    sdk.addEdge(int(u), int(v), int(w))
    sdp.addEdge(int(u), int(v), int(w))

f.close()
########################################################3

##############readfile and build graph#################

filename = "graphs/med_sparse.txt"
f= open(filename)
nodes = int(f.readline())
print("reading med_sparse")
print(nodes)
edges = int(f.readline())
print(edges)

msk = am.Graph(nodes)
msp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    msk.addEdge(int(u), int(v), int(w))
    msp.addEdge(int(u), int(v), int(w))
f.close()
########################################################3


##############readfile and build graph#################

filename = "graphs/med_dense.txt"
f= open(filename)

nodes = int(f.readline())
print("reading med dense")
print(nodes)
edges = int(f.readline())
print(edges)

mdk = am.Graph(nodes)
mdp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    mdk.addEdge(int(u), int(v), int(w))
    mdp.addEdge(int(u), int(v), int(w))

f.close()

########################################################3

##############readfile and build graph#################

filename = "graphs/large_sparse.txt"
f= open(filename)
nodes = int(f.readline())
print("read large sparse")
print(nodes)
edges = int(f.readline())
print(edges)

lsk = am.Graph(nodes)
lsp = am.GraphB(nodes)

for i in range(edges):
    data = f.readline()
    u, v, w = data.split(',')
    lsk.addEdge(int(u), int(v), int(w))
    lsp.addEdge(int(u), int(v), int(w))

f.close()
########################################################3

file_name = str("large sparse")
f= open(str(file_name +".txt"),"w+")
f.write(file_name)
f.write('\n')

f.write(str("sparse = .001, dense = .08"))
f.write('\n')

#################writes mean time of execution on small/med/large sparse/dense graphs######
###################tests small/med/large sparse/dense graphs######################

for i in range(0, 10):
    print("iteration: ", i)

    #small sparse
    x = timeit.timeit(ssp.PrimMST, number = 1)
    sspt.append(x)
    print(x)

    x = timeit.timeit(ssk.KruskalMST, number = 1)
    sskt.append(x)

    x = timeit.timeit(ssk.BoruvkaMST, number=1)
    ssbt.append(x)
    print(x)

    #small dense
    x = timeit.timeit(sdp.PrimMST, number = 1)
    sdpt.append(x)
    print(x)

    x = timeit.timeit(sdk.KruskalMST, number = 1)
    sdkt.append(x)
    print(x)

    x = timeit.timeit(sdk.BoruvkaMST, number=1)
    sdbt.append(x)
    print(x)

    #med sparse
    x = timeit.timeit(msp.PrimMST, number = 1)
    mspt.append(x)
    print(x)

    x = timeit.timeit(msk.KruskalMST, number = 1)
    mskt.append(x)
    print(x)

    x = timeit.timeit(msk.BoruvkaMST, number=1)
    msbt.append(x)
    print(x)


    #med dense
    x = timeit.timeit(mdp.PrimMST, number = 1)
    mdpt.append(x)
    print(x)

    x = timeit.timeit(mdk.KruskalMST, number = 1)
    mdkt.append(x)
    print(x)

    x = timeit.timeit(mdk.BoruvkaMST, number=1)
    mdbt.append(x)
    print(x)


    #large spares
    x = timeit.timeit(lsp.PrimMST, number = 1)
    lspt.append(x)

    x = timeit.timeit(lsk.KruskalMST, number = 1)
    lskt.append(x)

    x = timeit.timeit(lsk.BoruvkaMST, number=1)
    lsbt.append(x)

#writes means of runtime to file for each graph type
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
f.write(str("\nlsk: "+ str(statistics.mean(lskt))))
f.write(str("\nlsb: "+ str(statistics.mean(lsbt))))

f.write('\n')

#################comparing avg performance with eachother for significant differences##############
f.write("\ncomparing avg performance with eachother for significant difference... anova:\n")

data1, data2, data3 = sspt, sskt, ssbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nanova small sparse: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))

data1, data2, data3 = sdpt, sdkt, sdbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nanova small dense: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))

data1, data2, data3 = mspt, mskt, msbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nanova medium sparse: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))

data1, data2, data3 = lspt, lskt, lsbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nanova medium dense: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))

data1, data2 = lspt, lskt
stat, p = ttest_ind(data1, data2)
f.write("\n ttest p and k med dense: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))


data1, data2, data3 = lspt, lskt, lsbt
stat, p = f_oneway(data1, data2, data3)
f.write("\nanova large sparse: ")
f.write("stat: " + str(stat)+ " ")
f.write("p: " + str(p))

f.close()