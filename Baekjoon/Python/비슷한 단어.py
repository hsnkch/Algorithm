import sys
input = sys.stdin.readline

n = int(input())
target = list(input().rstrip())
ans = 0

for _ in range(n-1):
    compare = target[:]
    word = input().rstrip()
    cnt = 0

    for i in word:
        if i in compare:
            compare.remove(i)
        else:
            cnt += 1
    
    if cnt < 2 and len(compare) < 2:
        ans += 1

print(ans)