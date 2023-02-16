import sys
input = sys.stdin.readline

N = int(input())

def star(N):
    while N==0:
        
        N -= 1
        star(N)

star(N)        