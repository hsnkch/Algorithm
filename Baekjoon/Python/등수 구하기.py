import sys
input = sys.stdin.readline

n, score, p = map(int,input().split())

ans = 0

if n > 0:
    ranking = list(map(int,input().split()))
    if len(ranking) == p and ranking[-1] >= score:
        ans = -1
    else:
        while ranking:
            if ranking[-1] <= score:
                ranking.pop()
            else:
                break
        ans = len(ranking) + 1
        
else:
    ans = 1

print(ans)


