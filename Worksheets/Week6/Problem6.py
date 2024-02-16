

# E: (u,v) where u->v and u,v are verticies.
# V: an array of verticies, numbered 1 to n.
def CountTriangles(G,V,E):
    adj_list = [[] for i in range(len(V)+1)] # adj_list[1:n], where adj_list[i] is the list of neighbors of vertex i.
    for u,v in E:
        adj_list[u].append(v)
    for i in range(1,len(V)+1):
        adj_list[i].sort()

    triangles = 0
    for u in range(1,len(adj_list)+1):
        for v in range(1,len(adj_list)+1):
            if u != v:
                triangles += findW(u,v, adj_list)
    
    return triangles/3 # Each triangle is counted 3 times: u->v->w, v->w->u, w->u->v

def findW(u,v, adj_list):
    w = 0
    p, q = 0, 0
    while p < len(adj_list[u]) and q < len(adj_list[v]):
        if adj_list[u][p] == adj_list[v][q]:
            w += 1
            p += 1
            q += 1
        elif adj_list[u][p] < adj_list[v][q]:
            p += 1
        else:
            q += 1
    return w