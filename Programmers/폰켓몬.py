def solution(nums):
    answer = 0
    if len(list(set(nums))) <= len(nums)/2:
        answer = len(list(set(nums)))
    else:
        answer = len(nums)/2

    return answer

print(solution([3,3,3,2,2,4]))

# 다른 풀이

# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))