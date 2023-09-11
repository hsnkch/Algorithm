def dfs(graph, start, visited):
    visited[start] = True
    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

def solution(n, computers):
    cnt = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(computers,i, visited)
            cnt += 1

    
    return cnt


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))