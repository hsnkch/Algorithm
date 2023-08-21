def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)

    for i in range(len(citations)):
        if citations[i] >= i+1 and len(citations[i+1:]) <= i+1:
            answer = i + 1
            
    return answer

    # 다른 풀이
    # citations.sort(reverse=True)
    # answer = max(map(min, enumerate(citations, start=1)))
    # return answer   

print(solution([3, 0, 6, 1, 5]))