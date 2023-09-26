def solution(k, ranges):
    answer = []
    seqeunce = []
    seqeunce.append(k)
    while k > 0:
        if k == 1:
            break

        if k % 2 == 0:
            k = k // 2
            seqeunce.append(k)

        else:
            k = k*3 + 1
            seqeunce.append(k)

    for r in ranges:
        total = 0
        seqeunceRange = seqeunce[r[0] : len(seqeunce)+r[1]]
        
        # 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간
        if r[0] >= r[1] + len(seqeunce):
            answer.append(-1)
            continue
            
        for i in range(len(seqeunceRange) - 1):
            # 사다리꼴 넓이 구하는 공식 : ((윗변+아랫변) * 높이) / 2
            total += (((seqeunceRange[i] + seqeunceRange[i+1]) * 1) / 2)
        answer.append(total)

    return answer

print(solution(5,[[0,0],[0,-1],[2,-3],[3,-3]]))