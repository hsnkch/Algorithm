import sys
input = sys.stdin.readline

N = int(input())

live = [0]*21   # 살아있는 벌레 숫자
death = [0]*21  # 죽은 벌레 숫자

live[1] = 1     # 1년도에 하나 살아있
death[4] = 1    # 4년에 하나 죽
for i in range(2,21):   # 0년도 1년도는 빼야됨 
    born = live[i-1]    # 태어난거 작년 살아있는거
    live[i] = born*2 - death[i]    
    if i % 2 == 0:  # 짝수년도 태어난 애들
        if i+4 <= 20:
            death[i+4] += born  # 4년뒤에 죽
    else :  # 홀수년도 태어난 애들
        if i+3 <= 20:
            death[i+3] += born  # 3년뒤에 죽

print(live[N])
