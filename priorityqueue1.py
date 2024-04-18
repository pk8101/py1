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
    
    def removeDown(self):
        parentIndex=0
        leftIndex=2*parentIndex+1
        rightIndex=2*parentIndex+2
        while leftIndex<self.getSize():
            minIndex=parentIndex
            if self.pq[minIndex].priority>self.pq[leftIndex].priority:
                minIndex=leftIndex
            if rightIndex<self.getSize() and self.pq[minIndex].priority>self.pq[rightIndex].priority:
                minIndex=rightIndex
            
            if minIndex==parentIndex:
                break
            self.pq[parentIndex],self.pq[minIndex]=self.pq[minIndex],self.pq[parentIndex]
            parentIndex=minIndex
            leftIndex=2*parentIndex+1
            rightIndex=2*parentIndex+2
        
    def removeMin(self):
        if self.isEmpty():
            return None
        ele=self.pq[0].value
        self.pq[0]=self.pq[self.getSize()-1]
        self.pq.pop()
        self.removeDown()
        return ele
    
pq=PriorityQueue()
pq.insert('A',10)
pq.insert('C',5)
pq.insert('B',19)
pq.insert('D',4)

for _ in range(pq.getSize()):
    print(pq.removeMin())