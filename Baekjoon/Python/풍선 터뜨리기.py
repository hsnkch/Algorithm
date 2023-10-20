import sys
from collections import deque
input = sys.stdin.readline

# n = int(input())
# q = deque(enumerate(map(int, input().split())))
# ans = []

# while q:
#     idx, paper = q.popleft()
#     ans.append(idx + 1)

#     if paper > 0:
#         q.rotate(-(paper - 1))
#     elif paper < 0:
#         q.rotate(-paper)

# print(' '.join(map(str, ans)))

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []
cnt = 0

while q:
    if cnt >= 0:
        idx,paper=q.popleft()
    else:
        idx,paper=q.pop()

    ans.append(idx+1)

    if len(q) == 0:
        break

    cnt = 0

    if abs(paper)-1 ==0:
        if paper>0:
            cnt+=1
        else:
            cnt-=1
    else:
        for _ in range(abs(paper)-1):
            if paper > 0:
                q.append(q[0])
                q.popleft() 
                cnt += 1

            elif paper < 0:
                q.appendleft(q[-1])
                q.pop()
                cnt -= 1
                
print(' '.join(map(str, ans)))