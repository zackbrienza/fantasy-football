#Scott Dickson
#1/3/2018
#Implementations of various graph algorithms
#All take an adjacency list of size n^2 where n is
#the number of vertices in the graph

from Queue import Queue

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
            if adj[temp][i] == 1 and not visited[i]:
                q.put(i)
    
    #Path not found
    if not visited[end]:
        return []
    else:
    #Backtrack and recover the path    
        cur = end
        bt_visited = n*[False]
        
        while cur != start:
            bt_visited[cur] = True
            for i in range(n):
                if adj[i][cur] == 1 and visited[i] and not bt_visited[i]:
                    path = [[i,cur]] + path
                    cur = i
                    break
        return path
                           

#Given a graph, edge capacities and the source/sink node
#Generate a maximum flow assignment of flow on each edge
def ford_fulkerson(adj,cap,s,t):
    n = len(adj[0])
    flow = [[0 for x in range(n)] for y in range(n)] #No flow on the graph initially
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
    res = [[0 for x in range(n)] for y in range(n)]
    
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 1:
                if flow[i][j] > 0:
                    res[j][i] = 1 #add backwards edge
                if flow[i][j] < cap[i][j]:
                    res[i][j] = 1 #Add forward edge
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
            
            if min_diff == 0 or min_diff > diff:
                min_diff = diff
                
    #Now add/subtract [min_diff] amount of flow
    #from edges in the path       
        
    for i in range(len(path)):
        head = path[i][0]
        tail = path[i][1]
        
        if adj[head][tail] == 1:
            flow[head][tail] += min_diff
        elif adj[tail][head] == 1:
            flow[head][tail] -= min_diff
    
    return flow
        

#Graph class for easy use and testing 
class Graph:
    
    def __init__(self):
        self.n = 0
        self.adj = []
        self.cap = []
        
    def setNodes(self,num):
        self.n = num
        self.adj = [[0 for x in range(num)] for y in range(num)]
        self.cap = [[0 for x in range(num)] for y in range(num)]
    def add_edge(self,start,end,c=1):
        self.adj[start][end] = 1
        self.cap[start][end] = c #Default capacity
    def getAdj(self):
        return self.adj
    def getCap(self):
        return self.cap

if __name__ == '__main__':
    g = Graph()
    
    g.setNodes(7)
    g.add_edge(0,1,3)
    g.add_edge(0,2,5)

    
    g.add_edge(1,3,1)
    g.add_edge(2,3,2)
    
    g.add_edge(1,4,5)
    g.add_edge(3,4,1)
    
    g.add_edge(3,5,3)
    g.add_edge(2,5,2)
    
    g.add_edge(4,6,7)
    g.add_edge(5,6,3)
    
    print("Adjacency array:")
    print(g.getAdj())
    print("Capacity array:")
    print(g.getCap())
    
    #Test with all edges having cap 1
    print("Max flow array:")
    print(ford_fulkerson(g.getAdj(),g.getCap(),0,6))
    
    
    