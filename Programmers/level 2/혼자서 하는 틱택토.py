def solution(board):
    board = [list(row) for row in board]
    answer = 1
    O_cnt = 0
    X_cnt = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                O_cnt += 1
            if board[i][j] == 'X':
                X_cnt += 1
    
    if O_cnt - X_cnt not in (0,1):
        answer = 0

    if bingo(board, 'O') and bingo(board, 'X'):
        answer = 0
    
     # O가 승리했다면 O_cnt == X_cnt + 1이어야 함.
    if bingo(board, 'O') and O_cnt != X_cnt + 1:
        answer = 0
    
    # X가 승리했다면 O_cnt == X_cnt 여야 함.
    if bingo(board, 'X') and O_cnt != X_cnt:
        answer = 0

    return answer

def bingo(board, O_X):
    for row in board:
        if row == [O_X,O_X,O_X]:
            return True
        
    for col in range(3):
        if [board[row][col] for row in range(3)] == [O_X,O_X,O_X]:
            return True
        
    
    if [board[0][0], board[1][1], board[2][2]] == [O_X,O_X,O_X]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [O_X,O_X,O_X]:
        return True

    return False





print(solution(["O.X", ".O.", "..X"]))