# Given a directed graph G = (V, E ) describe an O(mn) time algorithm to find the smallest length
# cycle in G (or return that the graph is acyclic). Assume m ≥ n. Give a reason for both correctness
# and running time. 

from collections import deque

def shortest_cycle(V, E):
    """
    This function finds the shortest cycle in a directed graph G = (V, E).
    Args:
        V: an array of verticies, numbered 1 to n.
        E: an adjacency matrix of the graph.
    """
    min_cycle = float('inf')
    for node in V:
        dist = [-1 for i in range(len(V)+1)]
        q = deque()
        q.append(node)
        dist[node] = 0
        while q:
            cur_node = q.popleft()
            for neighbor in range(1,len(V)+1):
                if E[cur_node][neighbor] == 1:
                    # If not visited, distance += 1
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[cur_node] + 1
                        q.append(neighbor)
                    elif dist[neighbor] >= dist[cur_node]:
                        min_cycle = min(min_cycle, dist[neighbor] + dist[cur_node] + 1)
                    
    return min_cycle if min_cycle != float('inf') else "Graph is acyclic."

