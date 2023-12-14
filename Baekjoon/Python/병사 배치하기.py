import sys
input = sys.stdin.readline

n = int(input())
soldiers = list(map(int, input().split()))

dp = [1] * n    # i번째를 마지막 값으로 하는 배열의 길이
for i in range(1,n):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(len(soldiers) - max(dp))
