#Scott Dickson
#1/3/2018
#Implementations of various graph algorithms
#All take an adjacency list of size n^2 where n is
#the number of vertices in the graph

import Queue

#Try to find a path fromt the start node to the end node
#If found return a list of edges. Nil will be returned if
#a path cannot be found. if adj[i][j] == 1 then there is a directed
#edge between vertex i and vertex j
def bfs(adj, start, end):
    q = Queue()
    n = len(adj[0])#Number of nodes
    visited = n*[False]
    
    visited[start] = True
    q.put(start)
    path = []
        
    while not q.empty():
        temp = q.get()
        visited[temp] = True
        if temp == end:
            break
        
        for i in range(n):
            if adj[temp][i] == 1 and visited[adj[temp][i]]:
                q.put(adj[temp][i])
    
    #Path not found
    if not visited[end]:
        return []
    else:
    #Backtrack and recover the path    
        cur = end
        
        while cur != start:
            for i in range(n):
                if adj[i][cur] == 1 and visited[i]:
                    path = [[i,cur]] + path
                    cur = i
        return path
                           

#Given a graph, edge capacities and the source/sink node
#Generate a maximum flow assignment of flow on each edge
def ford_fulkerson(adj,cap,s,t):
    n = len(adj[0])
    flow = n*[n*[0]] #No flow on the graph initially
    max_flow = False
    
    while not max_flow:
        #Find path in the residual graph
        path = bfs(makeResidual(adj,flow,cap), s, t)
    
        #Maxiumum flow has been reached
        if path == []:
            max_flow = True
        else:
            flow = augment(adj,flow,cap,path)
    
    return flow      
    

#Given a graph, flows and capacities return the residial graph's
#Adjacency list 
def makeResidual(adj,flow,cap):
    n = len(adj[0])
    res = adj
    
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 1:
                if flow[i][j] == cap[i][j]:
                    res[i][j] = 0
                if flow[i][j] > 0:
                    res[j][i] = 1 #add backwards edge
    return res

#Update the flow after an augmenting path has been found
def augment(adj,flow,cap,path):
    
    min_diff = 0
    
    for i in range(len(path)):
        head = path[i][0]
        tail = path[i][1]
        if adj[head][tail] == 1:
            diff = cap[head][tail] - flow[head][tail]
            
            if min_diff == 0:
                min_diff = diff
            elif min_diff > diff:
                min_diff = diff
        elif adj[tail][head] == 1: #Check for backwards edges    
            diff = flow[head][tail]
            
            if min_diff == 0:
                min_diff = diff
            elif min_diff > diff:
                min_diff = diff
                
    #Now add/subtract [min_diff] amount of flow
    #from edges in the path       
        
    for i in range(len(path)):
        head = path[i][0]
        tail = path[i][1]
        
        if adj[head][tail] == 1:
            flow[head][tail] += diff
        elif adj[tail][head] == 1:
            flow[head][tail] -= diff
    return flow
        



    


#Graph class for easy use and testing 
class Graph():
    self.n = 0
    self.adj = []

    def setNodes(num):
        self.n = n
        self.adj = n*[n*[0]]
    def add_edge(start,end):
        self.adj[start][end] = 1
    def getAdj():
        return self.adj
    





if __name__ == '__main__':
    print("Not yet")