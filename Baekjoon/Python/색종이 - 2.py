import sys
input = sys.stdin.readline

n = int(input())

boards = [[0] * 102 for _ in range(102)]

for _ in range(n):
    x,y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            boards[i][j] = 1

cnt = 0
dx = [0,1,-1,0]
dy = [1,0,0,-1]

for i in range(1,101):
    for j in range(1,101):
        if boards[i][j] == 1:
            for k in range(4):
                rx = i + dx[k]
                ry = j + dy[k]
                if boards[rx][ry] == 0:
                    cnt += 1
print(cnt)