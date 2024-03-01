class Vertex:
    name: str
    neighbors: list

class Edge:
    u: Vertex
    v: Vertex
    cost: int

def NegativeEdge(V: list[Vertex], E: list[list[Edge]], source: Vertex):
    """
    Finds the shortest path between s and all verticies in V if there is a single
    negative edge. 
    Args:
        V: is a list of verticies, numbered 1 to n
        E: is an adjacency matrix
        source: a source vertex
    """

    negative_edge = None
    for edge in E:
        if edge.cost < 0:
            negative_edge = edge
    
    ## Create E' with the negative edge removed.
    E_p = list(E)
    E_p.remove(edge)

    ## Run normal distance, may be incorrect
    dist = Dijkstra(V, E, source)
    ## Run distance from end vertex of negative edge
    dist_p = Dijkstra(V, E, negative_edge.v)

    ## Min cost either doesn't use the negative edge, so is found from normal Dijkstra
    ##   or does use negative edge. 
    for i in range(1, len(V)+1):
        dist[i] = min(dist[i], dist[negative_edge.u] + dist_p[V[i]] + negative_edge.cost)


def Dijkstra(V, E, source):
    """
    Runs Dijkstra according to Lecture 18
    """
    dist = [float('inf') for i in range(1, len(V)+1)]
    ## Update Dist
    return dist

