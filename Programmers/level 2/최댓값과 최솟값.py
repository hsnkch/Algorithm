def solution(s):
    a = list(map(int, s.split()))
    mina = min(a)
    maxa = max(a)
    return f"{mina} {maxa}" 

print(solution("-1 -2 -3 -4"))