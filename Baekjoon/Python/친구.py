import sys
input = sys.stdin.readline

n = int(input())
friends = [input().rstrip() for _ in range(n)]
result = [[0]*n for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        for k in range(n): 
            if i == j:
                continue

            if friends[i][j] == 'Y': 
                result[i][j] = 1
            elif (friends[i][k] == 'Y' and friends[k][j] == 'Y'):
                result[i][j] = 1
                
for i in result:
    ans = max(ans,sum(i))

print(ans)
