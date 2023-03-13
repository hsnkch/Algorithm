import sys
input = sys.stdin.readline
from collections import deque

# dfs 함수
def dfs(graph, node, visited):
    # 현재 node 방문처리
    visited[node] = True
    # 인접 리스트 정렬
    graph[node].sort()
    # 탐색한 node 출력
    print(node, end=' ')
    # 현재 node와 연결된 다른 node를 재귀적으로 방문
    for i in graph[node]:
        if not visited[i]:
            dfs(graph,i,visited)

# bfs 함수
def bfs(graph, start_node, visited):
    q = deque([start_node])
    # 현재 node 방문처리
    visited[start_node] = True
    # 인접 리스트 정렬
    graph[start_node].sort()
    # 큐에 아무것도 없을 때까지 반복
    while q:
        # 큐에서 원소 하나 뽑기
        node = q.popleft()
        # 탐색한 노드 출력
        print(node, end=' ')
        # 해당 노드와 연결되어있고 아직 방문 안한 원소를 큐에 삽입
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

N, M, V = map(int,input().split())
iGraph = [[] for i in range(N+1)]
dVisited = [False]*(N+1)
bVisited = [False]*(N+1)

for _ in range(M):
    a, b = map(int,input().split())
    iGraph[a].append(b)
    iGraph[b].append(a)

dfs(iGraph,V,dVisited)
print()
bfs(iGraph,V,bVisited)