import sys
input = sys.stdin.readline

n, m = map(int,input().split())
tree = sorted(list(map(int,input().split())))

start = 0
end = max(tree)
result = 0

while start <= end:
    mid = (end + start) // 2

    total = 0   # 나무의 총 길이
    for i in tree:
        if i > mid:
            total += (i-mid)
    if total == m:
        result = mid
        break
    elif total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)
