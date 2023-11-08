import sys
input = sys.stdin.readline

n = int(input().rstrip())
house = sorted(list(map(int, input().split())))

print(house[(n-1)//2])