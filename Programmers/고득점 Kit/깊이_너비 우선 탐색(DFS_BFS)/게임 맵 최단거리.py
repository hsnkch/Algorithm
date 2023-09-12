from collections import deque

def bfs(graph, x, y, n, m):
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    q = deque()
    q.append((x,y))
    graph[x-1][y-1] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            rx, ry = x + dx, y + dy

            if rx < 1 or ry < 1 or rx > n or ry > m:
                continue

            if graph[ry-1][rx-1] == 1:
                q.append((rx,ry))
                graph[ry-1][rx-1] = graph[y-1][x-1]+ 1
            
    if graph[-1][-1] <= 1:
        return -1

    return graph[-1][-1]
    
def solution(maps):
    return bfs(maps,1,1,len(maps[0]),len(maps))

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))