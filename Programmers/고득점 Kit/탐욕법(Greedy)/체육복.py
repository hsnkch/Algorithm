def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n + 2)
    for i in lost:
        students[i] -= 1
    
    for j in reserve:
        students[j] += 1
    
    for k in range(1, n+1):
        if students[k] == 0:
            if students[k - 1] == 2:
                students[k - 1] -= 1
                students[k] += 1
            elif students[k + 1] == 2:
                students[k + 1] -= 1
                students[k] += 1

    cnt = 0
    for l in students[1:-1]:
        if l >= 1:
            cnt += 1
    return cnt


print(solution(5,[2,4],[1,3,5]))