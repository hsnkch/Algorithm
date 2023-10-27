import sys
input = sys.stdin.readline

c, r = map(int,input().split())
k = int(input().rstrip())

if k > c*r:
    print(0)
    sys.exit()

dir = [(1,0),(0,1),(-1,0),(0,-1)]
seats = [[0] * c for _ in range(r)]
seats[0][0] = 1
cur_dir = 0
x,y = 0,0

for i in range(2,k+1):
    while True:
        dx,dy = dir[cur_dir]
        rx = x + dx
        ry = y + dy
        if 0 <= rx < r and 0 <= ry < c and seats[rx][ry] == 0:
            seats[rx][ry] = i
            x, y = rx, ry
            break
        else:
            cur_dir = (cur_dir + 1) % 4

print(y+1, x+1)
