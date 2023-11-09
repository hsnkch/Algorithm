import sys
input = sys.stdin.readline

N, P = map(int,input().split())
melody = [list(map(int,input().split())) for _ in range(N)]

strings = [[] for _ in range(7)]
ans = 0

for l, p in melody:
    if len(strings[l]) == 0:
        strings[l].append(p)
        ans += 1
    else:
        if p == strings[l][-1]:
            continue
        elif p > strings[l][-1]:
            strings[l].append(p)
            ans += 1
        else:
            while strings[l] and strings[l][-1] > p:
                strings[l].pop()
                ans += 1
            if strings[l] and strings[l][-1] == p:
                continue
            strings[l].append(p)
            ans += 1

print(ans)