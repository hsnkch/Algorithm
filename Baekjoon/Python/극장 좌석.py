import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())

seats = [0]
for i in range(m):
    seats.append(int(input().rstrip()))
seats.append(n+1)

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
ways = [0] * (m+3)

for i in range(1, m + 2):
    a = seats[i] - seats[i-1] - 1
    ways[i] = dp[a]

for way in ways:
    if way != 0:
        ans *= way

print(ans)