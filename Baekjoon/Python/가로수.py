import sys
import math
input = sys.stdin.readline

n = int(input())
og = list(int(input()) for _ in range(n))
gap = []
for i in range(n-1):
    gap.append(og[i+1]-og[i])

num = gap[0]
for i in range(1,len(gap)):
    num = math.gcd(num,gap[i])

result = 0
for i in gap:
    result += i//num-1

print(result)