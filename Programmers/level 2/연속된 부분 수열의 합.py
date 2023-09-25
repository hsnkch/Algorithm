def solution(sequence, k):
    answer = []
    sum = 0
    left = 0
    right = -1

    while True:
        # 합이 더 작으면 오른쪽 요소 더하기
        if sum < k:
            right += 1
            if right >= len(sequence):
                break

            sum += sequence[right]
        
        # 합이 이상이면 왼쪽 요소 빼기
        else:
            sum -= sequence[left]
            if left >= len(sequence):
                break

            left += 1
        
        if sum == k:
            answer.append([left, right])

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]


print(solution([1, 1, 1, 2, 3, 4, 5],5))