import sys
input = sys.stdin.readline

n = int(input().rstrip())
total = int(input().rstrip())
students = list(map(int, input().split()))

pic = []
score = []
for i in range(total):
    if students[i] in pic:
        for j in range(len(pic)):
            if students[i] == pic[j]:
                score[j] += 1
    else:
        if len(pic) >= n:
            for j in range(n):
                if score[j] == min(score):
                    pic.pop(j)
                    score.pop(j)
                    break
        pic.append(students[i])
        score.append(1)
pic.sort()
print(' '.join(map(str, pic)))