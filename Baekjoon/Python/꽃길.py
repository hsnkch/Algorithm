import sys
input = sys.stdin.readline

n = int(input())
price = list(list(map(int,input().split())) for _ in range(n))

dx = [1,-1,0,0,0]
dy = [0,0,1,-1,0]
visited = [[0]*n for _ in range(n)]
ans = 1e9
total = 0

def check(x,y):
    for i in range(5):
        rx = x + dx[i]
        ry = y + dy[i]
        if visited[rx][ry] == 1:
            return False
    return True

def dfs(depth):
    global ans,total
    if depth == 3:
        ans = min(ans,total)
        return

    for i in range(1,n-1):
        for j in range(1,n-1):
            if check(i,j):
                for k in range(5):
                    a = i + dx[k]
                    b = j + dy[k]
                    visited[a][b] = 1
                    total += price[a][b]
                
                dfs(depth + 1)

                for k in range(5):
                    a = i + dx[k]
                    b = j + dy[k]
                    visited[a][b] = 0
                    total -= price[a][b]

dfs(0)
print(ans)