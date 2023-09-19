from collections import Counter

def solution(weights):
    answer = 0

    counter_list = Counter(weights)
    for k,v in counter_list.items():
        if v>=2:
            answer += v*(v-1)//2    # 같은 무게
    weights = set(weights) 
    
    # 2:3 2:4 3:4 비율 가지면 짝궁 가능함
    for w in weights:
        if w*2/3 in weights:
            answer += counter_list[w*2/3] * counter_list[w]
        if w*2/4 in weights:
            answer += counter_list[w*2/4] * counter_list[w]
        if w*3/4 in weights:
            answer += counter_list[w*3/4] * counter_list[w]
    return answer 


print(solution([100,180,360,100,270]))