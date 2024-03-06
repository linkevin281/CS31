##### This is a class. It contains the methods for creating and 
##### minor manipulations of graphs.
##### 
##### The graph is stored as an adjacency list. This is represented by a dict() structure,
##### where the keys are vertices and the values are sets with the corresponding neighborhood lists. 
##### 
##### Original code by : C. Seshadhri, Jan 2015
##### Modified by : Deeparnab Chakrabarty, Apr 2019

import itertools

class graph(object):

#### Initializing empty graph
####

    def __init__(self):
        self.vertices = set()    # Vertices are stored in a set   
        self.adj_list = dict()   # Initial adjacency list is empty dictionary 
        self.weights = dict()    # Initialize weights list for edges; default is 1


#### Stats
####

    def num_vertices(self):     #Returns number of vertices
        return len(self.vertices)

    def num_edges(self):
        s = 0
        for v in self.vertices:
            s = s + len(self.adj_list[v])
        return s

#### Checks if (node) is vertex of graph. Output is 1 (yes) or 0 (no).
####

    def isVertex(self,node):
        if node in self.vertices:               # Check if node is vertex
            return 1
        return 0                                 # Vertex not present!

#### Checks if (node1, node2) is edge of graph. Output is 1 (yes) or 0 (no).
####

    def isEdge(self,node1,node2):
        if node1 in self.vertices:               # Check if node1 is vertex
            if node2 in self.adj_list[node1]:    # Then check if node2 is neighbor of node1
                return 1                         # Edge is present!

#        if node2 in self.vertices:               # Check if node2 is vertex
#            if node1 in self.adj_list[node2]:    # Then check if node1 is neighbor of node2 
#                return 1                         # Edge is present!

        return 0                                 # Edge not present!

##### Return weight of edge (u,v) if present. Assumed to be directed
##### 
      
    def weight(self, node1, node2):
        if self.isEdge(node1, node2):
            return self.weights[(node1,node2)]
        else:
            print((node1,node2), "is not an edge")
            return None

        
    
    
#### Add vertex (v)
####

    def Add_Vertex(self,node):
        if not self.isVertex(node):
            self.vertices.add(node)
            self.adj_list[node] = set()

#### Add directed edge (node1, node2). Can add weights as (node1, node2, w). Default w = 1
####
    
    def Add_Edge(self,node1,node2,wt=1):
        if node1 == node2:                  # Self loop, so do nothing
            return
        if not self.isVertex(node1):
            self.Add_Vertex(node1)
        if not self.isVertex(node2):
            self.Add_Vertex(node2)

        nbrs = self.adj_list[node1]   # nbrs is neighbor list of node1
        if node2 not in nbrs:         # Check if node2 already neighbor of node1
            nbrs.add(node2)           # Add node2 to this list
        
        self.weights[(node1,node2)] = wt    #add weight

#### Add undirected, simple edge (node1, node2) Can add weights as (node1, node2, w). Default w = 1
#### Calls above twice
    
    def Add_Und_Edge(self,node1,node2,w=1):
        self.Add_Edge(node1,node2,w)
        self.Add_Edge(node2,node1,w)

        
#### Read a graph from a file with list of edges. Arguments are fname (file name), sep (separator), flag (undirected/directed). Looks for file fname.
#### Default is DIRECTED. Set flag = "u" for UNDIRECTED
#### Assumes that line looks like:
#### 
#### node1 sep node2 sep weight
####
####
#### If sep is not set, then it is just whitespace.
#### IMPORTANT: if the first character of line is # (hash), this line is assumed to be a comment and ignored.


    
    
    def Read_Edges(self,fname,sep=None,flag=None):
        self.vertices = set()
        self.adj_list = dict() #purge graph before reading
        
        f_input = open(fname,'r')        # Open file
        list_edges = f_input.readlines() # Read lines as list
        
        for each_edge in list_edges:             # Loop of each line/edge
            edge = each_edge.strip()             # Remove whitespace from edge
            if len(edge) == 0:                   # If empty line, move to next line
                continue
            if edge[0] == '#':                   # line starts with #, and is comment
                continue                         # this is comment, so move to next line
            tokens = edge.split(sep)        # Split by sep to get tokens (nodes)
            if(len(tokens) > 2):
                w = tokens[2]
            else:
                w = 1
            if(flag=="u"):                  #If flag set to undirected
                self.Add_Und_Edge(tokens[0],tokens[1],w)
            else:
                self.Add_Edge(tokens[0],tokens[1],w) # Default is directed. Add directed edge given by first two tokens
            
#### Read labels on vertices of a graph
#### Assumes that line looks like:
#### 
#### node sep label
####
#### If node not found in G.vertices, then will return an error
####
#### If sep is not set, then it is just whitespace.
#### IMPORTANT: if the first character of line is # (hash), this line is assumed to be a comment and ignored.   

    def Read_Vertex_Labels(self, fname, sep=None):
        self.label = dict()
        
        f_input = open(fname,'r')        # Open file
        list_pairs = f_input.readlines() # Read lines as list
        
        for each_line in list_pairs:
            pair = each_line.strip()    # Remove whitespace
            if(len(pair) == 0):         #if empty line or start with #, ignore
                continue
            if pair[0] == '#':
                continue
            token = pair.split(sep)
            if(self.isVertex(token[0])):
                self.label[token[0]] = token[1]
            else:
                print("Error: Vertex not in Graph")
                return -1

#### 
#### For some applications you may need the incidence lists to be ordered in a certain order sigma. The following code does that
                

    def Reorder_Edges(self, sg):
        for v in self.vertices:
            self.adj_list[v] = sorted(self.adj_list[v], key=lambda x:sg.index(x))


############### Check if a path p as a list of vertices is a path

    def check_path(self, p):
    #check if p, given as a list of distinct vertices, is a valid path or not    
        for i in range(len(p) - 1):
            if not(self.isEdge(p[i], p[i+1])):
                return False
        return (len(p) == len(set(p)))

