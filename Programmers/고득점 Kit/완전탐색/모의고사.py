def solution(answers):
    answer = []
    num_1 = [1,2,3,4,5]
    num_2 = [2,1,2,3,2,4,2,5]
    num_3 = [3,3,1,1,2,2,4,4,5,5]

    cnt_one = 0
    cnt_two = 0
    cnt_thr = 0

    for i in range(len(answers)):
        if answers[i] == num_1[i % len(num_1)]:
            cnt_one += 1

        if answers[i] == num_2[i % len(num_2)]:
            cnt_two += 1

        if answers[i] == num_3[i % len(num_3)]:
            cnt_thr += 1

    print(cnt_one, cnt_two, cnt_thr)
    if cnt_one == max(cnt_one, cnt_two, cnt_thr):
        answer.append(1)
    if cnt_two == max(cnt_one, cnt_two, cnt_thr):
        answer.append(2)
    if cnt_thr == max(cnt_one, cnt_two, cnt_thr):
        answer.append(3)

    answer.sort()
    return answer



print(solution([1,2,3,4,5]))