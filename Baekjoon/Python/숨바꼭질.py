from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
route = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    if a > b:
        route[b].append(a)
    else:
        route[a].append(b)
visited = [0] * (n+1)

def bfs(num):
    q = deque()
    q.append(num)
    visited[num] = 1
    while q:
        node = q.popleft()
        for i in route[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                q.append(i)

bfs(1)
ans = max(visited)
print(visited.index(ans),ans-1,visited.count(ans))