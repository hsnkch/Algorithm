import sys
input = sys.stdin.readline

l = int(input().rstrip())
nums = list(map(int, input().split()))
n = int(input().rstrip())
nums.append(0)
nums.sort()

ans = 0
for i in range(l):
    if nums[i] == n or nums[i+1] == n:
        ans = 0
        break

    elif nums[i] < n < nums[i+1]:
        ans = (nums[i+1] - n) * (n - nums[i]) - 1
        break

print(ans)


