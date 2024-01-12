import sys
input = sys.stdin.readline

r,c = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

flag = False

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if x <= -1 or x >= r or y <= -1 or y >= c:
                    continue

                if graph[x][y] == "S":
                    flag = True
                    break

if flag:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = "D"
    for k in graph:
        print(''.join(k))