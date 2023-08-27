from collections import deque
def solution(priorities, location):
    answer = 0
    # index와 priorities 같이 생성
    d = deque([(i, p) for i, p in enumerate(priorities)])    
   
    while d:
        cur_l, cur_p = d.popleft()
        # any : 하나라도 조건에 부합하면 True
        if any(cur_p < p for p, _ in d):
            d.append((cur_p,cur_l))
        else:
            answer += 1
            if cur_l == location:
                break

    return answer

print(solution([2, 1, 3, 2],2))