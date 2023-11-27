import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

q = deque()
dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

while q:
    x, y = q.popleft()
    for i in range(len(dx)):
        rx = x + dx[i]
        ry = y + dy[i]
        if 0 <= rx < n and 0 <= ry < m:
            if graph[rx][ry] == 0:
                q.append((rx,ry))
                graph[rx][ry] = graph[x][y] + 1
                ans = max(ans, graph[x][y] + 1)

print(ans-1)