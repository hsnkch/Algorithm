import sys
input = sys.stdin.readline

n = int(input())

arr1 = [0] * 3
arr2 = [0] * 3

for _ in range(n):
    a,b,c = map(int,input().split())
    arr1[0] += a
    arr1[1] += b
    arr1[2] += c

    arr2[0] += a**2
    arr2[1] += b**2
    arr2[2] += c**2

max_val = max(arr1)

if arr1.count(max_val) == 1:
    for i in range(3):
        if arr1[i] == max_val:
            print(i+1,max_val)
else:
    square_max_value = max(arr2)
    if arr2.count(square_max_value) > 1:
        print(0,max_val)
    else:
        for i in range(3):
            if arr2[i] == square_max_value:
                print(i+1,max_val)
