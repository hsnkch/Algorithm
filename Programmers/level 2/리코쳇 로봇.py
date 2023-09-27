from collections import deque
def solution(board):
    answer = -1
    q = deque()
    dir = ((1,0),(-1,0),(0,1),(0,-1))
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                q.append((i,j))
                visited[i][j] = 1

    while q:
        x, y = q.popleft()
        if board[x][y] == 'G':
            answer = visited[x][y]-1

        for dx, dy in dir:
            now_x, now_y = x, y
            while True:
                now_x += dx
                now_y += dy
                if 0<=now_x<len(board) and 0<=now_y<len(board[0]) and board[now_x][now_y] == 'D':
                    now_x -= dx
                    now_y -= dy
                    break
                if now_x<0 or now_x>=len(board) or now_y<0 or now_y>=len(board[0]):
                        now_x -= dx
                        now_y -= dy
                        break
            
            if not visited[now_x][now_y]:
                visited[now_x][now_y] = visited[x][y] + 1
                q.append((now_x, now_y))

    return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))