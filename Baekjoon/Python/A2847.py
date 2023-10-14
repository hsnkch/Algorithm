import sys
input = sys.stdin.readline
N = int(input())
scores = []
ans = 0
for i in range(N):
    scores.append(int(input().rstrip()))


for i in range(N-1,0,-1):
    if scores[i] <= scores[i-1]:
        ans += scores[i-1] - scores[i] + 1
        scores[i-1] = scores[i] - 1

print(ans)