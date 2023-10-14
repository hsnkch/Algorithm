import sys
input = sys.stdin.readline

ans = 0
N, M = map(int, input().split())
if 1 < M <= 6:
    if N > 2:
        ans = min(M-1,3)
    elif N == 2:
        ans = (M-1) // 2
    else:
        ans = 0
elif M == 1:
    ans = 0
else:
    if N > 2:
        ans = 4 + M - 7
    elif N == 2:
        ans = 3
    else:
        ans = 0

print(ans+1)
        



