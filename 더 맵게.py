import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    
    while heap:
        if heap[0] >= K:
            break
        
        if len(heap) < 2:
            answer = -1
            break
        
        min_1 = heapq.heappop(heap)
        min_2 = heapq.heappop(heap)
        heapq.heappush(heap, min_1 + min_2 * 2)
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))
