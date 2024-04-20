import heapq

# inbuilt min heap operations
l1=[9,3,4,2,7,8]

heapq.heapify(l1) #it takes the iterable and do heapify operations

heapq.heappush(l1,3) #it push the element in last and do heap operations

heapq.heappop(l1) #it remove the minimum element and do heap operations

heapq.heapreplace(l1,4) #it will replace the min element with this given number and do heap operations

print(l1)
# inbuilt max heap operations
l2=[6,9,1,2,3,4,10,20]

heapq._heapify_max(l2) #it takes iterable and do heapify operations

heapq._heappop_max(l2) #it remove the maximum element and do heap operations

heapq._heapreplace_max(l1,4) #it will replace the max element with this given number and do heap operations

#for push in max heap we use heapq._siftdown_max(iterable,0,len(iterable)-1)
l2.append(20)
heapq._siftdown_max(l2,0,len(l2)-1)

print(l2)
