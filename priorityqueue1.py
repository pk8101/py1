class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority
        
class PriorityQueue:
    def __init__(self):
        self.pq=[]
    
    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize()==0
    
    def insertup(self):
        childnode=self.getSize()-1
        while childnode>0:
            parentIndex=(childnode-1)//2
            if self.pq[childnode].priority<self.pq[parentIndex].priority:
                self.pq[childnode],self.pq[parentIndex]=self.pq[parentIndex],self.pq[childnode]
                childnode=parentIndex
            else:
                break
        
    def insert(self,value,priority):
        pqNode=PriorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.insertup()
    
    def removeMin(self):
        pass