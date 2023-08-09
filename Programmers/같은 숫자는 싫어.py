from collections import deque
def solution(arr):
    answer = []
    d = deque(arr)
    idx = 0
    while len(d) > 0:
        if idx < len(d)-1 and d[idx] == d[idx+1]:
            d.popleft()
        else:
            answer.append(d.popleft())
    return answer


# 다른 풀이
# def solution(arr):
#     answer = []
#     for i in arr:
#         if answer[-1:] == [i] :
#             continue
#         answer.append(i)
#     return answer

print(solution([1,1,3,3,0,1,1]))