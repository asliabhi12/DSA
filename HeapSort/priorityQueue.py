import heapq

list = [1, 2,3 ,23,24,2,13,1,2,45]

heapq.heapify(list)
print(list)

heapq.heappop(list)
print(list)

heapq.heappush(list, 566)
print(list)

heapq.merge(list, [1,4,6,7])
print(list)