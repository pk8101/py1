
import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjacencyMatrix=[[0]*nVertices for j in range(nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjacencyMatrix[v1][v2]=1
        self.adjacencyMatrix[v2][v1]=1
    def removeedge(self,v1,v2):
        if self.containEdge(v1,v2) is False:
            return
        self.adjacencyMatrix[v1][v2]=0
        self.adjacencyMatrix[v2][v1]=0
    def containEdge(self,v1,v2):
        return True if self.adjacencyMatrix[v1][v2]>0 else False
    def __dfsHelper(self,sV,visited):
        print(sV)
        visited[sV]=True
        for i in range(self.nVertices):
            if (self.adjacencyMatrix[sV][i]>0 and visited[i] is False):
                self.__dfsHelper(i,visited)
                
    def dfs(self):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i,visited)
    
    def __bfsHelper(self,sV,visited):
        q=queue.Queue()
        q.put(sV)
        visited[sV]=True
        while q.empty() is False:
            u=q.get()
            print(u)
            for j in range(self.nVertices):
                if self.adjacencyMatrix[u][j]>0 and visited[j] is False:
                    q.put(j)
                    visited[j]=True
    def bfs(self):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i,visited)
        
        
    def __str__(self) :
        return str(self.adjacencyMatrix)
        
g=Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(3,6)
g.dfs()
print()
g.bfs()
print(g)