import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = sorted(list(int(input().rstrip()) for _ in range(n)))
ans = 0
for i in range(1,n+1):
    ans += abs(a[i-1] - i)

print(ans)