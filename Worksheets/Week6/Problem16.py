# We are given a directed acyclic graph G = (V,E) with |V | = n and |E| = m. Each vertex v has a
# cost cost(v) which is a positive integer. You need to design an algorithm to output should be an
# array/dictionary cheapest indexed by the vertices of G, such that cheapest[u] should contain just
# the cost of the cheapest vertex reachable from u. 

# Design and analyze an O(n + m) time dynamic programming algorithm.

# The following code is in python but should be treated as pseudocode. Ex. Line 17 is not valid python code.
def CheapestReachableVertex(G,V,E):
    topo = Topo(V,E)                            # topo[1:n], the topological order of the verticies where all outedges are to previous indexes. 
    cheapest = [0 for i in range(len(topo)+1)]  # cheapest[1:n], extra index for readability

    for i in range(1,len(topo)+1):  
        cheapest[i] = cost(topo[i])
    
    for i in range(1,len(topo)+1):
        cheapest[i] = min(cheapest[i], GetNeighbors(topo[i]))
    
    # Recovery.
    # Any vertex u, the cheapest vertex is stored at cheapest[topo.get(u)]
        # cheapest is in topo order
        # use topo.get(u) to get the index of vertex u
    return cheapest          
              
def GetNeighbors(v):
    return [] # An array of the out-neighbors of the vertex v.


def cost(v):
    return 0 # Some cost

def Topo(V,E):
    return [] # An array of the topological order of the graph. Returns verticies.
    # Citation: Lecture 15.