import sys
input = sys.stdin.readline
from collections import defaultdict

dic = defaultdict(int)

cnt = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    dic[tree] += 1 
    cnt += 1

trees = sorted(list(dic.keys()))
for i in trees:
    print(i ,f"{dic[i]/cnt*100:.4f}")

