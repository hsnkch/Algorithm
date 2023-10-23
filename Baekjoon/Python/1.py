import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break
    str = '1'
    cnt = 1
    while True:
        if int(str) % n == 0:
            break
        str += '1'
        cnt += 1

    print(cnt)
