from collections import deque
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(maps,i,j,n,m,visited))

    if answer:
        return sorted(answer)
    else:
        return [-1]


def bfs(maps, a, b, n, m, visited):
    q = deque()
    tmp = int(maps[a][b])
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    q.append((a,b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            rx = x + dx
            ry = y + dy

            if 0 <= rx < n and 0 <= ry < m and visited[rx][ry] == False and maps[rx][ry] != 'X':
                visited[rx][ry] = True
                tmp += int(maps[rx][ry])
                q.append((rx,ry))
    return tmp



print(solution(["XXXXX","XXXXX","XXXXX", "XXXXX"]	))