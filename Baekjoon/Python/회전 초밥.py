import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int,input().split())
sushi = []
for i in range(n):
    sushi.append(int(input().rstrip()))

left, right = 0, k-1
dic = defaultdict(int)
dic[c] += 1

for i in range(right + 1):
    dic[sushi[i]] += 1

ans = 0

while left < n:
    ans = max(len(dic),ans)

    dic[sushi[left]] -= 1
    if dic[sushi[left]] == 0:
        del dic[sushi[left]]
    
    left += 1
    right += 1

    dic[sushi[right % n]] += 1  # 한바퀴 넘어갔을 때

print(ans)