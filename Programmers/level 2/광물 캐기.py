def solution(picks, minerals):
    answer = 0
    if sum(picks) < len(minerals):
        minerals = minerals[:5*sum(picks)]
    
    # 광물 조사
    cnt_min = [[0, 0, 0]for x in range(10)] # dia, iron, stone
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_min[i//5][1] += 1
        else : 
            cnt_min[i//5][2] += 1

    # 피로도 높은 순 정렬
    cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))

    for dia, iron, stone in cnt_min:
        for i in range(len(picks)):
            if i == 0 and picks[i] > 0:
                picks[i] -= 1
                answer += dia + iron + stone
                break
            
            elif i == 1 and picks[i]>0: 
                picks[i]-=1
                answer += 5*dia + iron + stone
                break

            elif i == 2 and picks[i]>0: 
                picks[i]-=1
                answer += 25*dia + 5*iron + stone
                break


    return answer


print(solution([1,3,2],	["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))