import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjacencyMatrix=[[0]*nVertices for j in range(nVertices)]
        
    def addEdge(self,v1,v2,wt):
        self.adjacencyMatrix[v1][v2]=wt
        self.adjacencyMatrix[v2][v1]=wt
    
    def __str__(self) :
        return str(self.adjacencyMatrix)
    
    def getMinVertex(self,visited,weight):
        minvertex=-1
        for i in range(self.nVertices):
            if (visited[i] is False and (minvertex==-1 or weight[minvertex]>weight[i])):
                minvertex=i
        return minvertex
    
    def prims(self):
        parent=[-1 for i in range(self.nVertices)]
        visited=[False for i in range(self.nVertices)]
        weight=[sys.maxsize for i in range(self.nVertices)]
        weight[0]=0
        
        for i in range(self.nVertices-1):
            minvertex=self.getMinVertex(visited,weight)
            visited[minvertex]=True
            
            for j in range(self.nVertices):
                if (self.adjacencyMatrix[minvertex][j]>0 and visited[j] is False):
                    if (self.adjacencyMatrix[minvertex][j]<weight[j]):
                        weight[j]=self.adjacencyMatrix[minvertex][j]
                        parent[j]=minvertex
        
        for i in range(1,self.nVertices):
            if i<parent[i]:
                print(str(i)+" "+str(parent[i])+" "+str(weight[i]))
            else:
                print(str(parent[i])+" "+str(i)+" "+str(weight[i]))        
        
            
        

g=Graph(4)
g.addEdge(0,1,3)
g.addEdge(0,3,5)
g.addEdge(1,2,1)
g.addEdge(2,3,8)
g.prims()