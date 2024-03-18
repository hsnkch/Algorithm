import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
files = [input().rstrip() for _ in range(n)]

dic = defaultdict(int)
for file in files:
    dic[file.split('.')[1]] += 1

result = sorted(list(dic.items()),key=lambda x: x[0])
for i,j in result:
    print(f"{i} {j}")