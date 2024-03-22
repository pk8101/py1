# STACK--> push,pop,top,size,isempty
# list will be consider as inbuilt stack or queue.LifoQueue()
import queue
# inbuilt stack from queue
s=queue.LifoQueue()
for i in range(5):
    s.put(i)
while not s.empty():
    print(s.get())


# QUEUE--> Enqueue,Dequeue,size,isempty,front
print()
# inbuilt queue
q=queue.Queue()
for i in range(4):
    q.put(i)

while not q.empty():
    print(q.get())
    