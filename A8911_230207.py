import sys
input = sys.stdin.readline

T = int(input())    # test 케이스 수



for i in range(T):
    order = list(input().rstrip())  # 명령 리스트로 받기
    x, y = [0], [0] # 초기좌표
    direction = 0   # 나머지 0, 1, 2, 3 = 북, 동, 남, 서
     
    for j in order:  
        if j == 'F':    # 전진일때 x,y 좌표 x,y 리스트에 추가
            if direction % 4 == 0:
                x.append(x[len(x)-1])
                y.append(y[len(y)-1]+1)
            if direction % 4 == 1:
                x.append(x[len(x)-1]+1)
                y.append(y[len(y)-1])
            if direction % 4 == 2:
                x.append(x[len(x)-1])
                y.append(y[len(y)-1]-1)
            if direction % 4 == 3:
                x.append(x[len(x)-1]-1)
                y.append(y[len(y)-1])
        if j == 'B':    # 후진일때 x,y 좌표 x,y 리스트에 추가
            if direction % 4 == 0:
                x.append(x[len(x)-1])
                y.append(y[len(y)-1]-1)
            if direction % 4 == 1:
                x.append(x[len(x)-1]-1)
                y.append(y[len(y)-1])
            if direction % 4 == 2:
                x.append(x[len(x)-1])
                y.append(y[len(y)-1]+1)
            if direction % 4 == 3:
                x.append(x[len(x)-1]+1)
                y.append(y[len(y)-1])
        if j == 'L':    # 좌짝으로 돌기
            direction += 3
        if j == 'R':    # 우짝으로 돌기
            direction += 1
    width = abs(min(x))+abs(max(x))
    height = abs(min(y))+abs(max(y))    
    print(width*height)