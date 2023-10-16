import sys
input = sys.stdin.readline

def dfs(x,y,number):
    if len(number) == 6:
        result.append(number)
        return
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    for dx, dy in dir:
        rx = x + dx
        ry = y + dy
        if 0<=rx<5 and 0<=ry<5:
            dfs(rx,ry,number+str(boards[rx][ry]))

boards = []
result = []
for i in range(5):
    boards.append(list(map(int,input().split())))

for i in range(5):
    for j in range(5):
        dfs(i,j,str(boards[i][j]))

print(len(set(result)))



