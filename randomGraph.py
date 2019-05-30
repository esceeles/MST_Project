import random

def generateRandomConnectedGraph(self, V):

    initialSet = set()

    visitedSet = set()

    vertices = set()

    edges = set()

    #generate the set of names for the vertices

    for i in range(V):

        initialSet.add(int(i))

        vertices.add(int(i))

    #set the intial vertex to be connected

    curVertex = random.sample(initialSet, 1).pop()

    initialSet.remove(curVertex)

    visitedSet.add(curVertex)

    #loop through all the vertices, connecting them randomly

    while initialSet:

        adjVertex = random.sample(initialSet, 1).pop()

        edge = (random.randint(1, 100), curVertex, adjVertex)

        edges.add(edge)

        initialSet.remove(adjVertex)

        visitedSet.add(adjVertex)

        curVertex = adjVertex

    return vertices, edges

if __name__ == "__main__":
    nodes = 10000
    edges = nodes * 20
    file_name = "d_"+ str(nodes)+ "_n_" + str(edges)+"_e"
    f= open(str(file_name +".txt"),"w+")

    f.write(str(nodes) + '\n')
    f.write(str(edges) + '\n')

    x = generateRandomConnectedGraph(nodes, nodes)                 #generates random graph with n nodes and n-1 edges

    import algorithms_mod as am
    g = am.Graph(nodes)
    edgeDict = {}
    for (w, u, v) in x[1]:
        g.addEdge(u, v, w)

    print("Tree generated...")
    ex_edges = edges - (nodes-1)

    for i in range(ex_edges):             #adds 10 random edges to graph
        print(i)
        u = random.randint(0, nodes-1)
        v = random.randint(0, nodes-1)
        w = random.randint(0, 100)
        g.addEdge(u, v, w)


    for (u, v, w) in g.graph:
        f.write(str(u) + "," + str(v) + "," + str(w) + '\n')

    f.close()