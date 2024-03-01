


def APSP(V, E):
    """
    This function returns the all-pairs shortest path matrix.
    Args:
        V: an array of verticies, numbered 1 to n.
        E: an adjacency matrix of the graph.
    """

    dist = [[[0 for k in range(len(V)+1)] for j in range(len(V)+1)] for i in range(len(V)+1)]

    ## Init base case, distances without any intermediate verticies
    for i in range(1, len(V)+1):
        for j in range(1, len(V)+1):
            dist[i][j][0] = E[i][j]
    
    ## Recursive case
    for k in range(1, len(V)+1):
        for j in range(1, len(V)+1):
            for i in range(1, len(V)+1):
                dist[i][j][k] = min(dist[i][j][k-1], dist[i][k][k-1] + dist[k][j][k-1])
    
    return dist

