import sys
input = sys.stdin.readline

n,m = map(int,input().split())
costs = list(int(input()) for _ in range(n))

start = max(costs)
end = sum(costs)
k = 0
while start <= end:
    mid = (start + end) // 2
    tmp = mid
    num = 1
    for i in range(n):
        if tmp < costs[i]:
            tmp = mid
            num += 1
        tmp -= costs[i]
    
    if num > m:
        start = mid + 1
    else:
        end = mid - 1
        k = mid

print(k)