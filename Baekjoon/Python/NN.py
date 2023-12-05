import sys
input = sys.stdin.readline

n,m = map(int,input().split())
str_n = str(n) * n
print(str_n[:m])