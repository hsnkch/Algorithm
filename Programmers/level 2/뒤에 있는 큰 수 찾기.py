from collections import deque
def solution(numbers):
    q = deque()
    answer = [-1] * len(numbers)

    for idx in range(len(numbers)):
        target = numbers[idx]
        while q and numbers[q[-1]] < target:
            answer[q.pop()] = target
        
        q.append(idx)

    return answer


print(solution(	[9, 1, 5, 3, 6, 2]))