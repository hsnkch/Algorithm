import sys
input = sys.stdin.readline
from collections import deque


dir = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]

# bfs
def bfs(graph, x, y, l):
	q = deque()
	q.append((x, y))        # 시작 위치 큐에 삽입
	graph[x][y] = 0        # 괴물 위치로 바꿔 방문 처리
	while q:                # 큐가 빌 때까지
		x, y = q.popleft()    # 큐에서 현재 위치 빼기
		for dx, dy in dir:         # 상, 하, 좌, 우 확인
			rx, ry = x + dx, y + dy
			# 미로 안에 없다면 다음 조건 진행
			if (rx < 0 or rx >=l or ry < 0 or ry >= l):
				continue
			# 값이 1이라면 (처음 위치는 재방문 하지만 상관없으므로 진행)		
			if graph[rx][ry] == 999999999:
				q.append((rx, ry))                # 큐에 다음 위치로 넣기
				graph[rx][ry] = graph[x][y] + 1   # 다음 위치의 거리로 현재 위치 거리에 + 1
	return graph  # 마지막 위치에 거리를 반환

n = int(input())
for i in range(n):
	l = int(input())
	cur_x, cur_y = map(int, input().split())
	mov_x, mov_y = map(int, input().split())
	graph = [([999999999]*l) for _ in range(l)]
	result = bfs(graph,cur_x,cur_y,l)
	print(result[mov_x][mov_y])