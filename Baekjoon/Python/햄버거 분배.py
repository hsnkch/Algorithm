import sys
input = sys.stdin.readline

n,k = map(int,input().split())
words = list(input())
ans = 0

for i in range(n):
    if words[i] == 'P':
        for j in range(max(i-k,0), min(i+k+1,n)):
            if words[j] == 'H':
                words[j] = '0'
                ans += 1
                break

print(ans)