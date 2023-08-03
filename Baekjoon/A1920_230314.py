import sys
input = sys.stdin.readline

n = int(input())
n_arr = sorted(list(map(int, input().split())))

m = int(input())
m_arr = list(map(int, input().split()))

start = 0
end = n-1

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target: 
            start = mid + 1
    return 0

for i in m_arr:
    print(binary_search(n_arr, i, 0, n-1))