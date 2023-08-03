import sys
input = sys.stdin.readline

n = int(input()) 
dic = {}    # 숫자, 개수 key, value로 하는 dic

for i in range(n):
    num = int(input())  # input 받아서
    if num in dic:  # 있던 input이면
        dic[num] += dic[num]    # 1 늘리고
    else:   # 없던거면 
        dic[num] = 1    # 초기 value값 1로 dic에 추가
    
# dic의 key, value값을 받아서
# value기준 내림차순 후 key기준 오름차순
result = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])