"""
/***************************************************************************************
*    Title: generateRandomConnectedGraph
*    Author: dtlafever
*    Date: 11/14/17
*    Availability: notexponential.com
*
***************************************************************************************/
"""


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

    nodes = 30000               #choose nodes
    density = 1                 #choose density rating
    edges = (density * (nodes**2 - nodes))/2        #edges based on density rating
    edges = int(edges)                              #if not int, round down

    #writes to file with this naming convention
    file_name = "large_" + str(nodes) + "_density_"+str(density)
    f= open(str(file_name +".txt"),"w+")

    f.write(str(nodes) + '\n')                          #writes nodes and edges to file
    f.write(str(edges) + '\n')

    x = generateRandomConnectedGraph(nodes, nodes)         #generates random tree with n nodes and n-1 edges

    for (w, u, v) in x[1]:
        f.write(str(u) + "," + str(v) + "," + str(w) + '\n')    #adds tree edges to file

    print("Tree generated...")
    ex_edges = edges - (nodes-1)                #how many additional edges will be needed for desired density

    for i in range(ex_edges):             #adds needed edges to file/graph
        print(i)
        u = random.randint(0, nodes-1)              #can create a multigraph, MST algorithms can handle multigraphs
        v = random.randint(0, nodes-1)
        w = random.randint(0, 100)
        f.write(str(u) + "," + str(v) + "," + str(w) + '\n')

    f.close()