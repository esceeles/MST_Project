from collections import defaultdict

from collections import defaultdict


# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph
        self.boruvkaMST = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

        # A utility function to find set of an element i

    # (uses path compression technique)
    def find(self, parent, i):
        #print("in find, i, parent: ", i, parent)
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

        # A function that does union of two sets of x and y

    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

            # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    def BoruvkaMST(self):
        parent = [];
        rank = [];

        # An array to store index of the cheapest edge of
        # subset. It store [u,v,w] for each component
        cheapest = []

        # Initially there are V different trees.
        # Finally there will be one tree that will be MST
        numTrees = self.V
        MSTweight = 0

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest = [-1] * self.V

            # Keep combining components (or sets) until all
        # compnentes are not combined into single MST

        while numTrees > 1:

            # Traverse through all edges and update
            # cheapest of every component
            for i in range(len(self.graph)):

                # Find components (or sets) of two corners
                # of current edge
                u, v, w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                # If two corners of current edge belong to
                # same set, ignore current edge. Else check if
                # current edge is closer to previous
                # cheapest edges of set1 and set2
                if set1 != set2:

                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]

                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]

                        # Consider the above picked cheapest edges and add them
            # to MST
            for node in range(self.V):

                # Check if cheapest for current set exists
                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        MSTweight += w
                        self.union(parent, rank, set1, set2)
                        #print("Edge %d-%d with weight %d included in MST" % (u, v, w))
                        self.boruvkaMST.append([u, v, w])
                        numTrees = numTrees - 1

            # reset cheapest array
            cheapest = [-1] * self.V

        #print("Weight of MST is %d" % MSTweight)
        return self.boruvkaMST


    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):

        result = []  # This will store the resultant MST

        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1:  Sort all the edges in non-decreasing
        # order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        #print("Pre sort graph: ", self.graph)
        self.graph = sorted(self.graph, key=lambda item: item[2])           #edges are sorted in order by weight, smallest to largest
        #print("Graph: ", self.graph)

        parent = [];
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)                 #adds each node to parent list
            rank.append(0)                      #associated rank for each node in parent list
        #print("parent: ", parent)
        #print("rank: ", rank)
            # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            #print("e = ", e)                #e is index for result, i is index for all sorted edges
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            #print("i = ", i)
            u, v, w = self.graph[i]             #gets next smallest weighted edge from graph
            #print("graph: ", self.graph)
            #print(u, v, "weight: ", w)
            i = i + 1                           #increments i so we don't look at this edge again
            x = self.find(parent, u)
            y = self.find(parent, v)
            #print("x, y: ", x, y)           #checks to see that x and y are not already connected by some other edges, checks no cycle
            # If including this edge does't cause cycle,
            # include it in result and increment the index
            # of result for next edge
            if x != y:
                #print("no cycle")
                e = e + 1
                result.append([u, v, w])
                #print("result: ", result)
                self.union(parent, rank, x, y)
                # Else discard the edge

            #else:
                #print("cycle found")
        # print the contents of result[] to display the built MST
        #print("Following are the edges in the constructed MST")
        return result
        #for u, v, weight in result:
            # print str(u) + " -- " + str(v) + " == " + str(weight)
            #print("%d -- %d == %d" % (u, v, weight))


class Heap():

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

        # A utility function to swap two nodes of

    # min heap. Needed for min heapify
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[int(a)] = self.array[int(b)]
        self.array[b] = t

        # A standard function to heapify at given idx

    # This function also updates position of nodes
    # when they are swapped. Position is needed
    # for decreaseKey()
    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < \
                self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < \
                self.array[smallest][1]:
            smallest = right

            # The nodes to be swapped in min heap
        # if idx is not smallest
        if smallest != idx:
            # Swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            # Swap nodes
            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

            # Standard function to extract minimum node from heap

    def extractMin(self):

        # Return NULL wif heap is empty
        if self.isEmpty() == True:
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):

        # Get the index of v in  heap array

        i = self.pos[v]
        i = int(i)
        # Get the node and update its dist value
        self.array[i][1] = dist

        # Travel up while the complete tree is not
        # hepified. This is a O(Logn) loop

        while i > 0 and self.array[i][1] < \
                self.array[int((i - 1) / 2)][1]:
            # Swap this node with its parent
            parentpos = int((i-1)/2)
            self.pos[self.array[i][0]] = (i - 1) / 2
            self.pos[self.array[parentpos][0]] = i

            self.swapMinHeapNode(i, parentpos)

            # move to parent index
            i = parentpos;

            # A utility function to check if a given vertex

    # 'v' is in min heap or not
    def isInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True
        return False


def printArr(parent, n):
    result = []
    for i in range(1, n):
        print("% d - % d" % (parent[i], i))
        result.append((parent[i], i))
    return result


class GraphB():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

        # Adds an edge to an undirected graph

    def addEdge(self, src, dest, weight):
        # Add an edge from src to dest.  A new node is
        # added to the adjacency list of src. The node
        # is added at the begining. The first element of
        # the node has the destination and the second
        # elements has the weight
        #self.graph.append([src, dest, weight])
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        # Since graph is undirected, add an edge from
        # dest to src also
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

        # The main function that prints the Minimum
    # Spanning Tree(MST) using the Prim's Algorithm.
    # It is a O(ELogV) function

    def PrimMST(self):
        # Get the number of vertices in graph
        V = self.V

        # key values used to pick minimum weight edge in cut
        key = []

        # List to store contructed MST
        parent = []

        # minHeap represents set E
        minHeap = Heap()

        # Initialize min heap with all vertices. Key values of all
        # vertices (except the 0th vertex) is is initially infinite
        for v in range(V):
            parent.append(-1)
            key.append(10000000000)
            minHeap.array.append(minHeap.newMinHeapNode(v, key[v]))
            minHeap.pos.append(v)

            # Make key value of 0th vertex as 0 so
        # that it is extracted first
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])

        # Initially size of min heap is equal to V
        minHeap.size = V;

        # In the following loop, min heap contains all nodes
        # not yet added in the MST.
        while minHeap.isEmpty() == False:

            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            # Traverse through all adjacent vertices of u
            # (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:

                v = pCrawl[0]

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less than
                # its previously calculated distance
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u

                    # update distance value in min heap also
                    minHeap.decreaseKey(v, key[v])

        result = printArr(parent, V)
        return result

