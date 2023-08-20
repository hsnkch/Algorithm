def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0] - 1
        end = i[1]
        find = i[2] - 1
        s_array = sorted(array[start:end])
        answer.append(s_array[find])

    return answer

    # 다른 풀이
    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	))