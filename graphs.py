# we can implement graph using three ways
# 1.Edgelist->two list are there one for vertices and one for edges
# 2.adjecencylist->it can be written using dict
# 3.adjacencymatrix-> every thing will be written in matrix

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
    
    def __str__(self) :
        return str(self.adjacencyMatrix)
        
g=Graph(5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(3,4)
g.addEdge(1,3)
g.addEdge(2,4)
print(g)