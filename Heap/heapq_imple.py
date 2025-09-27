import heapq

arr = [4, 3, 2, 10, 8, 20, 22, 30]
heapq.heapify(arr)
print(arr)
heapq.heappush(arr, 10)
print(arr)
heapq.heapify(arr)
print(arr)

heapq.heappop(arr)
print(arr)

print(heapq.nlargest(2, arr))
print(heapq.nsmallest(2, arr))

print(heapq.heappushpop(arr, 99))

print(heapq.heapreplace(arr, 20))



