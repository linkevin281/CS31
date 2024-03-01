# We are given a directed graph G with non-negative costs c(u, v) on edges. There may be cases where
# there are multiple shortest cost paths between s and a vertex v. In that case, it maybe useful to find the
# shortest cost path with the fewest edges. To that end, define best[v] to be the minimum number of edges
# among all shortest cost paths from s to v. Design an efficient algorithm to find best[v] for all vertices v.
# Note: best[s] = 0.

import math, heapq

class Node:
    neighbors: list
    data: any
    name: str

class Edge:
    v: Node
    u: Node

class Graph:
    edges: list[Edge]
    verticies: list[Node]

def BFS(source, target, graph):
    p_queue = heapq.heapify([])
    heapq.heappush((0,source))
    visited = set()

    ## Distance, BT, edges 
    data = {}
    for node in graph.verticies:
        data[node.name] = [float('inf'), None, float('inf')]

    ## Take out closest node to source
    while p_queue:
        cur_node = heapq.heappop(p_queue)
        visited.add(cur_node)
        cn_distance, cn_bt, cn_edges = data[cur_node.name]
        for neighbor in cur_node:
            n_distance, n_bt, n_edges= data[neighbor.name]
            new_distance = cn_distance + graph.verticies[cur_node, neighbor]
            if new_distance <= n_distance:
                n_distance = new_distance
                n_bt = cur_node
                n_edges = cn_edges + 1
            if neighbor not in visited:
                visited.add(neighbor)
    return data[target.name][0]

