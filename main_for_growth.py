import timeit
from scipy.stats import ttest_ind, f_oneway, ttest_rel, normaltest
import matplotlib.pyplot as plt
from pylab import plot, show, ion, ioff, subplot, figure, savefig, subplots
import math
from randomGraph import multigraph
import gc

gc.disable()

file_name = str("growth_over_node_growth")
f = open(str(file_name + ".txt"), "w+")
f.write(file_name)
f.write('\n')

f.write('\n')

prim_time =[]
krus_time = []
bor_time = []
log_time = []

############For looking at growth in time over node growth##############
prim_growth = []
krus_growth = []
bor_growth = []
log_growth = []
node_growth = []
node_time = []
min = 1000
max = 9500
scale = 500

f.write(str("nodes in range: " + str(min) + "-" + str(max)))
density = 0.1
f.write(str("\ndensity: " + str(density)))
f.write('\n')
for nodes in range(min, max, scale):
    print("nodes: ", nodes)

    node_time.append(nodes)
    p, k, edges = multigraph(nodes, density)

    x = timeit.timeit(p.PrimMST, number=1)  # Time Prim
    prim_time.append(x)
    print("prim: ", x)

    y = timeit.timeit(k.KruskalMST, number=1)  # Time Kruskal
    krus_time.append(y)
    print("krus: ", y)

    if x < 8:                           ####grows so much faster it's not worth putting on a graph. doubles every time
        z = timeit.timeit(k.BoruvkaMST, number=1)  # Time Boruvka
        bor_time.append(z)
        print("bor: ", z)

    log = edges * (math.log10(nodes))  # Get theoretical complexity
    log_time.append(log)

for i in range(len(prim_time) - 1):  # calculates growth at each interval for each alg
    g = prim_time[i + 1] - prim_time[i]
    g = g / prim_time[i + 1]
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

for i in range(len(bor_time)-1):
    g = bor_time[i + 1] - bor_time[i]
    g = g / bor_time[i + 1]
    g = g * 100
    bor_growth.append(g)

plt.plot(prim_growth, color='green')
plt.plot(krus_growth, color='blue')
plt.plot(bor_growth, color='yellow')
plt.plot(log_growth, color='red')


savefig(str(file_name + ".png"))


#################comparing growth rates with eachother for significant differences##############

data1, data2 = prim_growth, krus_growth
stat, p = ttest_ind(data1, data2)
f.write("\nttest prim & kruskal growth rates: ")
f.write("stat: " + str(stat) + " ")
f.write("p: " + str(p))


data1, data2 = krus_growth, bor_growth
stat, p = ttest_ind(data1, data2)
f.write("\nttest boruvka & kruskal growth rates: ")
f.write("stat: " + str(stat) + " ")
f.write("p: " + str(p))

data1, data2 = prim_growth, bor_growth
stat, p = ttest_ind(data1, data2)
f.write("\nttest prim & boruvka growth rates: ")
f.write("stat: " + str(stat) + " ")
f.write("p: " + str(p))

#########comparing with log growth rates for significant differences#################

data1, data2 = prim_growth, log_growth
stat, p = ttest_ind(data1, data2)
f.write("\nttest prim & log growth rates: ")
f.write("stat: " + str(stat) + " ")
f.write("p: " + str(p))

data1, data2 = krus_growth, log_growth
stat, p = ttest_ind(data1, data2)
f.write("\nttest kruskal & log growth rates: ")
f.write("stat: " + str(stat) + " ")
f.write("p: " + str(p))

data1, data2 = bor_growth, log_growth
stat, p = ttest_ind(data1, data2)
f.write("\nttest boruvka & log growth rates: ")
f.write("stat: " + str(stat) + " ")
f.write("p: " + str(p))

f.close()

###########################################################3
all_time = []  ####time as nodes increase####
all_time.append(list(krus_time))
all_time.append(list(prim_time))

fig, ax = plt.subplots()
ax.stackplot(node_time, all_time, labels=["krus", "prim"])
ax.set_title('growth in time over nodes')
ax.legend(loc='upper left')
ax.set_ylabel('time')
ax.set_xlabel('nodes')
# ax.set_ylim(ymin= 900, ymax = 1100)
fig.tight_layout()

savefig(str(file_name + "_time_over_nodes.png"))

