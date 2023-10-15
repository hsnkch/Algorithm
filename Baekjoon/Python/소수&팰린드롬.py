import sys, math
input = sys.stdin.readline

n = int(input().rstrip())

def find(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

ans = 0

for i in range(n, 1000001): 
    if i == 1:
        continue
    if str(i) == str(i)[::-1]: 
        if find(i): 
            ans = i
            break

if ans == 0: 
    ans = 1003001

print(ans)
