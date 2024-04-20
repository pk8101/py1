import heapq

# inbuilt min heap operations
l1=[9,3,4,2,7,8]

heapq.heapify(l1) #it takes the iterable and do heapify operations

heapq.heappush(l1,3) #it push the element in last and do heap operations

heapq.heappop(l1) #it remove the minimum element and do heap operations

print(l1)