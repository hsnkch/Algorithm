def solution(distance, rocks, n):
    answer = 0
    # rocks.append(0)
    # rocks.append(distance)
    # rocks.sort()

    # d = []

    # for i in range(len(rocks)-1):
    #     d.append(rocks[i+1]-rocks[i])

    # idx = [i for i in range(len(rocks)-2)]
    # tmp = []
    # for j in permutations(idx,n):
    #     tmp = d.copy()
    #     for k in range(n):
    #         tmp.append(d[j[k]]+d[j[k]+1])
    #         # tmp.remove(d[j[k]])
    #         tmp.remove(d[j[k]+1])
    #     print(tmp)
    #     answer = max(answer,min(tmp))

    left = 1
    right = distance
    rocks.sort()
    rocks.append(distance)


    while left <= right:
        mid = (left + right)//2
        # 제거한 바위 수
        delete = 0
        # 이전 바위 위치
        prev_rock = 0

        for rock in rocks:
            dist = rock = prev_rock
            # 거리가 커트라인 보다 작으면 바위를 제거
            if dist < mid:
                delete +=1
                # 제거한 바위 많으면 break
                if delete > n:
                    break
            # 바위 제거 안했으면 prev_rock 갱신
            else:
                prev_rock = rock

        # 초과 제거한 경우 = 커트라인이 높음
        if delete > n:
            right = mid - 1
        
        # 이하 제거한 경우 = 커트라인이 적절 or 낮음
        else:
            answer = mid
            left = mid + 1
    return answer

print(solution(25,[2,14,11,21,17],2))