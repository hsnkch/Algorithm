def solution(s):
    sum = 0
    answer = False
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            break

    if sum == 0:
        answer = True

    return answer


print(solution("(())()"))