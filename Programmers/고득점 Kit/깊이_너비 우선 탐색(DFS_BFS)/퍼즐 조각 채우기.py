from collections import deque
#좌, 상, 우, 하
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def get_rotated_blocks(blocks):
	#테이블에 놓인 블록들을 회전시킨다
    i = len(blocks)
    
    while i > 0:
        i -= 1
        #블록 크기, 블록 상태
        b_len, block = blocks[i]
        #블록 종류 i
        blocks[i].append(i)
        
        #회전하기 전 블록 상태 ori_block
        ori_block = block
        
        #시계방향으로 3번 회전시킨다
        for _ in range(3):
            new_block = []
            #블록 회전 시키기
            for y in range(len(ori_block[0])):
                row = []
                for x in range(len(ori_block)-1, -1, -1):
                    row.append(ori_block[x][y])
                new_block.append(row)
                
            #회전한 블록 추가하기
            blocks.append([b_len, new_block, i])
            ori_block = blocks[-1][1]
	
    #id별로 블록 정렬하기
    blocks.sort(key=lambda x:x[2])


def fill_puzzle(puzzles, blocks):
    answer = 0
    
    #visit[i] = i 종류의 블록이 사용되었으면 1, 아니면 0
    visit = [0]*(blocks[-1][-1]+1)
    blocks = deque(blocks)
    
    for p_len, puzzle in puzzles:
        i = len(blocks)
        while i > 0:
            i -= 1
            #블록의 크기, 블록 상태, 블록의 종류
            b_len, block, id = blocks.popleft()
            
            #이미 사용한 블록이라면, 사용할 수 없으므로 무시한다
            if visit[id]: continue
			
            #퍼즐 빈칸의 크기와 블록의 크기가 같지 않거나,
            #퍼즐 가로/세로 영역과 블록 가로/세로 영역이 크기가 같지 않은 경우,
            #해당 블록을 사용할 수 없음므로, blocks에 다시 추가해준다
            if p_len != b_len or len(puzzle) != len(block) or len(puzzle[0]) != len(block[0]):
                blocks.append([b_len, block, id])
                continue
                
            #해당 블록으로 퍼즐의 빈칸을 채울 수 있다면 True, 아니면 False
            check = True
            
            for y in range(len(puzzle)):
                for x in range(len(puzzle[0])):
                	#블록으로 퍼즐의 빈칸을 딱맞게 채울 수 없는 경우,
                    if puzzle[y][x] == block[y][x]:
                        check = False
                        break
                        
            #해당 블록을 사용할 수 있는 경우, 블록을 사용하고 answer값에 퍼즐의 크기만큼 더하고, 다음 퍼즐을 탐색한다
            if check:
                visit[id] = 1
                answer += p_len
                break
            
            #해당 블록을 사용할 수 없음므로, blocks에 다시 추가해준다
            blocks.append([b_len, block, id])
    return answer


def get_blocks(block_range, table):
    blocks = []
    
    #영역의 범위에 속하는 게임 보드/블록을 구한다
    for length, sx, ex, sy, ey in block_range:
        new_block = []
        for y in range(sy, ey+1):
            row = []
            for x in range(sx, ex+1):
                row.append(table[y][x])
            new_block.append(row)
        blocks.append([length, new_block])

    return blocks

def get_block_range(table, n):
    visit = [[0] * len(table[0]) for _ in range(len(table))]
    blocks = []
    
    for y in range(len(table)):
        for x in range(len(table[0])):
        	#해당 칸이 n과 같고 이전에 방문하지 않았다면, 영역을 구한다
            if table[y][x] == n and not visit[y][x]:
                q = deque([[x, y]])
                
                #영역의 시작 범위와 끝 범위를 구한다
                sx, ex = x, x
                sy, ey = y, y
                visit[y][x] = 1
                length = 1
                
                while q:
                    now_x, now_y = q.popleft()
                    
                    #해당 칸과 상, 하, 좌, 우로 인접한 칸 탐색
                    for ddx, ddy in zip(dx, dy):
                        nx = now_x + ddx
                        ny = now_y + ddy
                        
                        #영역 안에 속하는 경우,
                        if 0 <= nx < len(table[0]) and 0 <= ny < len(table):
                        	#해당 칸이 n과 같고 이전에 방문하지 않았다면, 영역에 속하므로 탐색을 이어나간다
                            if table[ny][nx] == n and not visit[ny][nx]:
                                visit[ny][nx] = 1
                                q.append([nx, ny])
                                #시작점과 끝점을 갱신
                                if ex < nx: ex = nx
                                if ey < ny: ey = ny
                                if sx > nx: sx = nx
                                if sy > ny: sy = ny
                                #영역 크기 카운팅
                                length += 1
                
                #영역의 크기와 영역의 범위를 blocks에 추가한다                
                blocks.append([length, sx, ex, sy, ey])
                
    return blocks


def solution(game_board, table):
	#각각의 블록이 차지하는 영역 구하기 -> 블록 = 1
    blocks_range = get_block_range(table, 1)
    #블록이 포함된 최소 사각형 배열 구하기
    blocks = get_blocks(blocks_range, table)
    #회전한 블록 추가하기
    get_rotated_blocks(blocks)
    
    #하나의 퍼즐이 들어가는 영역 구하기 -> 빈 칸 = 0
    puzzles_range = get_block_range(game_board, 0)
    #빈칸이 포함된 최소 사각형 배열 구하기
    puzzles = get_blocks(puzzles_range, game_board)

    return fill_puzzle(puzzles, blocks)