from collections import deque
import sys
input = sys.stdin.readline

r,c,n = map(int, input().split())
board = []
for i in range(r):
    board.append(list(input().rstrip()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()

def bfs(q,board):
    while q:
        x,y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            rx = x + dx[i]
            ry = y + dy[i]
            if 0<=rx<r and 0<=ry<c and board[rx][ry] == 'O':
                board[rx][ry] = '.'

def simulate(t):
    global q, board
    if t == 1:
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    q.append((i,j))
    elif t % 2 == 1:
        bfs(q, board)
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    q.append((i,j))
    else:
        board = [['O']*c for _ in range(r)]

for i in range(1,n+1):
    simulate(i)

for i in board:
    print(''.join(i))
