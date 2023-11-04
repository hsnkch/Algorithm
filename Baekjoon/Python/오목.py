import sys
input = sys.stdin.readline

boards = list(list(map(int, input().split())) for _ in range(19))

dir = {(1,0),(0,1),(1,1),(-1,1)}

def bfs(x,y):
    target = boards[x][y]
    for dx, dy in dir:
        cnt = 1
        rx = x + dx
        ry = y + dy
        while 0 <= rx < 19 and 0 <= ry < 19 and boards[rx][ry] == target:
            cnt += 1
            if cnt == 5:
                if 0 <= x - dx < 19 and 0 <= y - dy < 19 and boards[x - dx][y - dy] == target:
                    break
                if 0 <= rx + dx < 19 and 0 <= ry + dy < 19 and boards[rx + dx][ry + dy] == target:
                    break
                print(target)
                print(x + 1, y + 1)
                exit(0)
            rx += dx
            ry += dy

for i in range(19):
    for j in range(19):
        if boards[i][j] != 0:
            bfs(i,j)
print(0)