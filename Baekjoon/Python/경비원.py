import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input().rstrip())
course = []

def dist(dir,dist):
    if dir == 1:
        return dist
    elif dir == 2:
        return w + w + h - dist
    elif dir == 3:
        return w + h + w + h - dist
    else:
        return w + dist

for _ in range(n+1):
    a, b = map(int, input().split())
    course.append(dist(a,b))

ans = 0
for i in range(n):
    tmp = abs(course[-1] - course[i])
    ans += min(tmp,2*(w+h)-tmp)

print(course)