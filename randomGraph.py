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

        edge = (random.randint(1, 1000), curVertex, adjVertex)

        edges.add(edge)

        initialSet.remove(adjVertex)

        visitedSet.add(adjVertex)

        curVertex = adjVertex

    return vertices, edges

def multigraph(nodes, density):

    edges = (density * (nodes**2 - nodes))/2
    edges = int(edges)


    x = generateRandomConnectedGraph(nodes, nodes)                 #generates random graph with n nodes and n-1 edges

    import algorithms_mod as am

    k = am.Graph(nodes)
    p = am.GraphB(nodes)

    for (w, u, v) in x[1]:
        p.addEdge(u, v, w)
        k.addEdge(u, v, w)


    ex_edges = edges - (nodes-1)

    for i in range(ex_edges):             #adds 10 random edges to graph
        u = random.randint(0, nodes-1)
        v = random.randint(0, nodes-1)
        w = random.randint(0, 1000)
        p.addEdge(u, v, w)
        k.addEdge(u, v, w)
    print("Tree generated...")

    return p, k, edges