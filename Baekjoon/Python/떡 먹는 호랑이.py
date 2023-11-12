import sys
input = sys.stdin.readline

d, k = map(int, input().split())
dp_1 = [0] * d
dp_1[0] = 1
dp_2 = [0] * d
dp_2[1] = 1
for i in range(2,d):
    dp_1[i] = dp_1[i-1] + dp_1[i-2]
    dp_2[i] = dp_2[i-1] + dp_2[i-2]
cnt_1 = dp_1[-1]
cnt_2 = dp_2[-1]

for i in range(1, k//cnt_1):
    total_2 = k - cnt_1 * i
    if total_2 % cnt_2 == 0:
        print(i)
        print((k - cnt_1 * i) // cnt_2)
        break
