def solution(clothes):
    dic = {}
    for i in range(len(clothes)):
        dic[clothes[i][1]] = []
        for j in range(len(clothes)):
            if clothes[i][1] == clothes[j][1]:
                dic[clothes[i][1]].append(clothes[j][0])
    cnt = 1

    for key, value in dic.items():
        print(key, value)
        cnt *= len(value)+1

    answer = cnt - 1
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))