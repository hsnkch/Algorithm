import sys
input = sys.stdin.readline

def check(eggs):
    cnt = 0 
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    return cnt

def dfs(idx,eggs):
    global ans

    if idx == n:
        ans = max(ans, check(eggs))
        return
    
    if eggs[idx][0] <= 0:
        dfs(idx+1, eggs)
    else:
        flag = True
        for i in range(len(eggs)):
            if idx != i and eggs[i][0] > 0:
                flag = False
                eggs[idx][0] -= eggs[i][-1]
                eggs[i][0] -= eggs[idx][-1]
                dfs(idx + 1, eggs)
                eggs[idx][0] += eggs[i][-1]
                eggs[i][0] += eggs[idx][-1]
        
        if flag:
            dfs(n,eggs)

n = int(input())
eggs = []
ans = 0
for _ in range(n):
    eggs.append(list(map(int,input().split())))

dfs(0,eggs)
print(ans)