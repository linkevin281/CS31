# Suppose a CS curriculum consists of n courses, all of them mandatory. The pre-requisite directed
# acyclic graph G = (V,E) with |V | = n and |E| = m, has a vertex for each course, and a directed edge
# from course v to course w if and only if v is a pre-requisite for w. A student cannot take a course
# before all its pre-requisite courses have been taken. Furthermore, a course and its pre-requisite
# course cannot be taken in the same term. Your objective is to design an algorithm that figures
# out the minimum number of terms required to complete the curriculum. You may assume that a
# student can take any number of courses in any given term.
#
# Design an O(n + m) time dynamic programming algorithm to find the minimum number of
# terms needed to complete every course. You should 
# (a) clearly describe the algorithm using pseudocode and the algorithm should return which prescribe which course should be taken in which term, 
# (b) prove why your algorithm is correct

# Lets let V and E be arrays with unchanging indexes as the function runs (not sets). This is needed for the topological sort to work and GetPrereqs.
# Lets let G'(V,E_p) be the graph with the edges reversed. 
def ChoosingCourses(G,V,E):
    topo = Topo(V,E)                         # topo[1:n], the topological order of the verticies, where 1 has no prereqs and n has the most prereqs. topo[1] stores the index of the vertex with no prereqs.
    GetPrereqs = [0 for i in range(len(V)+1)] # GetPrereqs[1:n] stores the index of the most recent prereq

    dp = [0 for i in range(len(topo)+1)] # dp[0:n]
    dp[0] = 0

    for i in range(1,len(V)+1):
        dp[i] = GetPrereqs(i) + 1 

        for u,v in V["neighbors"][topo[i]]: # Treat this section as pseudocode -> the idea is we find all courses that this course is a prereq for
            GetPrereqs[v] = i               # set any of those courses to have this course as a prereq 
       
    return dp

def Topo(V,E):
    return [] # An array of the topological order of the graph. Returns indexes of verticies.
    # Citation: Lecture 15. 


