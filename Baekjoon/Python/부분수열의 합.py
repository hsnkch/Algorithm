from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))

nums = set()

for i in range(1,n+1):
    for j in combinations(s,i):
        nums.add(sum(j))

for i in range(1, sum(s)+2):
    if i not in nums:
        print(i)
        break