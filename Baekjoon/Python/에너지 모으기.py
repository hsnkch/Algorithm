import sys
input = sys.stdin.readline
from itertools import combinations


def dfs(tmp):
    global ans
    if len(w) == 2:
        if ans < tmp:
            ans = tmp
        return
    else:
        for i in range(1, len(w) - 1):
            k = w[i]
            del w[i]
            dfs(tmp + w[i-1] * w[i])
            w.insert(i, k)

n = int(input())
w = list(map(int, input().split()))
ans = 0
dfs(0)
print(ans)