import sys
input = sys.stdin.readline

n = int(input())
l = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)

for i in range(l):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 함수
def dfs(graph, node, visited):
    # 현재 node 방문처리
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph, 1, visited)
cnt = 0

for i in visited:
    if i:
        cnt += 1

print(cnt-1)    # 1은 뺴야됨됨


