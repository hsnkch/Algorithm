import sys
input = sys.stdin.readline

n = int(input())
point = [list(map(int,input().split())) for _ in range(n)]

point = sorted(point, key=lambda x:x[0])

ans = 0
for i in range(1,n):
    if point[i][1] == point[0][1]:
       ans += abs(point[i][0] - point[0][0])
       break

for i in range(1,n):
    left_tmp = 1e5
    right_tmp = 1e5
    left = i-1
    right = i+1
    while left >= 0:
        if point[left][1] == point[i][1]:
            left_tmp = abs(point[left][0] - point[i][0])    
            break
        left -= 1
    
    while right < n:
        if point[right][1] == point[i][1]:
            right_tmp = abs(point[right][0] - point[i][0])    
            break
        right += 1
    
    tmp = min(left_tmp, right_tmp)
    ans += tmp

print(ans)