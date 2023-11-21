import sys
input = sys.stdin.readline

a = int(input())
ans = []

for i in range(1, a+1):
    first = a
    second = i
    tmp = [a,i]

    while True:
        next = first - second
        if next >= 0:
            tmp.append(next)
            first = second
            second = next
        else:
            if len(tmp) > len(ans):
                ans = tmp
            break
print(len(ans))
print(*ans)