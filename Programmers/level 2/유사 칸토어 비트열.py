def solution(n, l, r):
    answer = 0

    for i in range(l-1,r):
        if is_one(i):
            answer += 1


    return answer


def is_one(l):  # 5진수로 바꿨을 때 2가 포함X -> 1 
    while l >= 5:
        if (l-2) % 5 == 0:
            return False
        l //=5

    return l != 2



print(solution(2,4,17))