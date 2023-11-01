import sys
input = sys.stdin.readline
from collections import deque

king, stone, n = input().split()
moves = deque()
for i in range(int(n)):
    moves.append(input().rstrip())

char = ['A', 'B', 'C', 'D', 'E', 'F','G','H']
ways = ['R','L','B','T','RT','LT','RB','LB']
king_list = []
stone_list = []
dir = [(1,0),(-1,0),(0,-1),(0,1),(1,1),(-1,1),(1,-1),(-1,-1)]
king_list.append((char.index(king[0]), int(king[1])-1))
stone_list.append((char.index(stone[0]), int(stone[1])-1))

while moves:
    move = moves.popleft()
    x, y = king_list[-1]
    a, b = stone_list[-1]
    dx, dy = dir[ways.index(move)]
    rx = x + dx
    ry = y + dy
    ra = a + dx
    rb = b + dy
    if 0 <= rx < 8 and 0 <= ry < 8:
        if rx == a and ry == b:
            if 0 <= ra < 8 and 0 <= rb < 8:
                stone_list.append((ra, rb))
                king_list.append((rx,ry))
        else:
            king_list.append((rx,ry))

ans_k = king_list.pop()
ans_s = stone_list.pop()

print(char[ans_k[0]] + str(ans_k[1]+1))
print(char[ans_s[0]] + str(ans_s[1]+1))