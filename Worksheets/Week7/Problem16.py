class Vertex:
    data: any
    neighbors: list

class Edge:
    u: Vertex
    v: Vertex
    color: "red" or "blue"
    cost: int

def BellmanFordMod(V: list[Vertex], E: list[list[Edge]], source: Vertex) -> bool:
    """
    This function accepts G(V, E) and a source vertex s. It returns whether or
      not there exists a cycle with strictly more red edges than blue edges.
    Args:
        V: an array of verticies, numbered 1 to n.
        E: an adjacency matrix of the graph.
    """
    ## Assign all red edges a -1, all blue edges a +1
    for edge in E:
        if edge.color == "red":
            edge.cost = -1
        else:
            edge.cost = 1
    ## Init distances
    dist = {vertex: float('inf') for vertex in V}
    ## Run BellmanFord as normal. If there is a negative cycle, such a cycle with more 
    #    red edges must exist.
    for vertex in V:
        for edge in E:
            u, v = edge.u, edge.v
            dist[v] = min(dist[u] + edge.cost, dist[v])
    ## If we detect a negative cycle, return True
    for v in V:
        for u in V.neighbors:
            u, v = edge.u, edge.v
            ## If there is an edge that can be improved still
            if dist[u] + edge.cost < dist[v]:
                return True
    return False


