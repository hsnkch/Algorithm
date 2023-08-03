import sys
input = sys.stdin.readline

list = list(input().rstrip())
num = [0]*9

for i in list:
    if i == '0':
        num[0] += 1
    elif i == '1':
        num[1] += 1
    elif i == '2':
        num[2] += 1
    elif i == '3':
        num[3] += 1
    elif i == '4':
        num[4] += 1
    elif i == '5':
        num[5] += 1
    elif i == '7':
        num[7] += 1
    elif i == '8':
        num[8] += 1
    else:
        num[6] += 1
if num[6] % 2 == 0:
    num[6] = num[6] // 2
else:
    num[6] = num[6] // 2 +1

print(max(num))
