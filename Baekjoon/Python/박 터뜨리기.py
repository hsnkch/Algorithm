import sys
input = sys.stdin.readline

n,k = map(int,input().split())
if n < k*(k+1)//2:
    ans = -1
elif (n - k*(k+1)//2) % k == 0:
    ans = k-1
else:
    ans = k
print(ans)