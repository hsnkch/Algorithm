import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
ans = []
cards = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    tmp = 0
    for j in combinations(cards[i],3):
        a = sum(j) % 10

        tmp  = max(tmp,a)
    
    ans.append((tmp,i+1))

result = sorted(ans,key=lambda x : (-x[0],-x[1]))
print(result[0][1])
