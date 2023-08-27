import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    
    for i in operations:
        if i[0] == 'I':
            num = int(i[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
     
        elif i == 'D 1' and max_heap:
            heapq.heappop(max_heap)
            min_heap = [-x for x in max_heap]
            heapq.heapify(min_heap)

        elif i == 'D -1' and min_heap:
            heapq.heappop(min_heap)
            max_heap = [-x for x in min_heap]
            heapq.heapify(max_heap)
        
    if not min_heap:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
