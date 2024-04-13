# here we find minimum spanning tree using kruskal algo and union find algo(it detects cycles in graph using parent list)

class Edge:
    def __init__(self,src,dist,wt):
        self.src=src
        self.dist=dist
        self.wt=wt
# this method gives the parent of that vertex
def getParent(v,parent):
    if v==parent[v]:
        return v
    return getParent(parent[v],parent)
def kruskal(edges,nVertices):
    parent=[i for i in range(nVertices)] #initially parent of its vertex is itself
    output=[]
    i=0 #for edges
    count=0 #it tracks edges ,for n vertex we need n-1 edges
    edges=sorted(edges,key=lambda edge:edge.wt)
    while count<(nVertices-1):
        curr_edged=edges[i]
        src_parent=getParent(curr_edged.src,parent)
        dist_parent=getParent(curr_edged.dist,parent)
        if src_parent!=dist_parent:
            parent[src_parent]=dist_parent
            output.append(edges[i])
            count=count+1
        i=i+1
    return output
    
li=[int(i) for i in input().split()]
nodes=li[0]
vertices=li[1]
edges=[]
for i in range(vertices):
    curr_edge=[int(i) for i in input().split()]
    src=curr_edge[0]
    dit=curr_edge[1]
    wt=curr_edge[2]
    edge=Edge(src,dit,wt)
    edges.append(edge)


print("output:")
output=kruskal(edges,nodes)
for edge in output:
    if edge.src<edge.dist:
        print(str(edge.src)+" "+str(edge.dist)+" "+str(edge.wt))
    else:
        print(str(edge.dist)+" "+str(edge.src)+" "+str(edge.wt))
    
