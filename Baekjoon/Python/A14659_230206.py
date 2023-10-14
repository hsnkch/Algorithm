import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = []
count = 0
c = 0
for i in a:
    if i > c:
        b.append(count)
        c = i
        count=0
    else:
        count += 1
b.append(count)        
print(max(b))
