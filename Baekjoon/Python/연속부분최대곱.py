import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = [float(input().rstrip()) for _ in range(n)]

dp = [0.0] * n
dp[0] = nums[0]
for i in range(1,n):
    dp[i] = max(nums[i],nums[i]*dp[i-1])

print('%0.3f'%max(dp))