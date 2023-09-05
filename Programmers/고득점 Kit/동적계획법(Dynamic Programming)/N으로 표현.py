def solution(N, number):
    answer = 0
    # d = [0] * 32001

    # if N == 1:
    #     d[1] = 1
    # else:
    #     d[1] = 2

    # for i in range(2, number+1):
    #     d[i] = d[i-1] + 2
    #     d[i+N] = d[i] + 1

    #     if i % N == 0:
    #         d[i] = min(d[i], d[d[i]//N] + 1)


    # return d[number]

    if number == 1:
        return 1
    set_list = []
    
    for cnt in range(1, 9): # 1개부터 8개까지 확인
        partial_set = set()
        partial_set.add(int(str(N) * cnt)) # 이어 붙여서 만드는 경우 넣기
        for i in range(cnt - 1): # (1, n-1) 부터 (n-1, 1)까지 사칙연산
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        # 만든 집합에 number가 처음 나오는지 확인
        if number in partial_set:
            return cnt
        set_list.append(partial_set)
    return -1

print(solution(5,12))

