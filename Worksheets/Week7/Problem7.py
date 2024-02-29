

from collections import deque

def verifying_distance_lables(V, E, C, dist, source):
    """
    This function confirms the distance lables in dist.
    Args:
        V: an array of verticies, numbered 1 to n.
        E: an adjacency matrix of the graph.
        C: returns cost of edge E
        dist: an array of distances from a source node.
        source: the source node.
    """
    shortest_tree_matrix = [[0 for i in range(len(V)+1)] for j in range(len(V)+1)]

    if dist[source] != 0:
        return False
    ## Confirm all distances are possible
    for edge in E:
        u, v = edge
        if dist[u] + C[u][v] < dist[v]:
            return False
        elif dist[u] + C[u][v] == dist[v]:
            shortest_tree_matrix[u][v] = 1
    ## Run BFS to confirm all nodes are reachable
    q = deque()
    q.append(source)
    visited = [False for i in range(len(V)+1)]
    visited[source] = True
    while q:
        cur_node = q.popleft()
        for neighbor in range(1,len(V)+1):
            if shortest_tree_matrix[cur_node][neighbor] == 1 and not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
    return all(visited)
    
        

