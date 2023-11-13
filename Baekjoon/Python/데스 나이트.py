from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip())
r1, c1, r2, c2 = map(int, input().split())

dx = [-1,1,-2,2,-1,1]
dy = [-2,-2,0,0,2,2]

graph = [[-1]*N for _ in range(N)]

def BFS(r1, c1):
    q = deque()
    q.append((c1,r1))
    graph[c1][r1] = 0
    while q:
        y, x = q.popleft()
        for i in range(6):
            rx = x + dx[i]
            ry = y + dy[i]
            if 0<=rx<N and 0<=ry<N and graph[ry][rx] == -1:
                graph[ry][rx] = graph[y][x] + 1
                q.append((ry,rx))

BFS(r1,c1)

print(graph[r2][c2])
    