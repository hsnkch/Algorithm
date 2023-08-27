from itertools import permutations
def solution(k, dungeons):
    answer = 0

    perm = permutations(dungeons)

    for i in perm:
        now = k
        cnt = 0
        for j in i:
            if now>=j[0]:
                now -= j[1]
                cnt += 1
        answer = max(answer, cnt)

    return answer
    # while k > end_time and idx < len(dungeons):
    #     if dungeons[idx][0] >= end_time + dungeons[idx][1]:
    #         end_time += dungeons[idx][1]
    #         answer += 1
    #     idx += 1

print(solution(80, [[80,20],[50,40],[30,10]]))