import sys
input = sys.stdin.readline

def binary_search(note, num, start, end):
    while start <= end:
        mid = (start + end) // 2
        if note[mid] > num:
            end = mid - 1
        elif note[mid] < num:
            start = mid + 1
        else:
            return 1
    return 0

T = int(input().rstrip())
for i in range(T):
    N = int(input().rstrip())
    note_one = sorted(list(map(int,input().split())))
    M = int(input().rstrip())
    note_two = list(map(int,input().split()))
    for num in note_two:
        print(binary_search(note_one,num,0,N-1))

    