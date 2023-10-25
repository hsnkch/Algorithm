import sys
inpyut = sys.stdin.readline

n = int(input().rstrip())
stick = [0]*1001
max_h = 0
max_idx = 0
for i in range(n):
    l, h = map(int, input().split())
    stick[l] = h
    if max_h < h:
        max_idx = l
        max_h = h

cur_L = 0
ans = 0
for i in range(max_idx+1):
    cur_L = max(cur_L,stick[i])
    ans += cur_L

cur_R = 0
for i in range(1000,max_idx,-1):
    cur_R = max(cur_R,stick[i])
    ans += cur_R

print(ans)






