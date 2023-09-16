from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 제한사항에서 모든 좌표값은 1 이상 50 이하라고 했고 2배의 좌표를 그려야 하므로 102*102 크기의 2차원 배열 선언
    field = [[-1] * 102 for i in range(102)]
    visited = [[1] * 102 for i in range(102)]
    
    # 직사각형 그리기
    for r in rectangle:
    	# 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
            	# x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 1    
   
    q = deque()
    q.append((characterX * 2,characterY * 2))

    dir = [(1,0),(-1,0),(0,1),(0,-1)]

    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break

        for dx, dy in dir:
            rx, ry = x + dx, y + dy
            for i in range(len(rectangle)):
               if field[rx][ry] == 1 and visited[rx][ry] == 1:
                q.append([rx, ry])
                visited[rx][ry] = visited[x][y] + 1        
            
    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))

