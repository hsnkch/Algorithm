import sys
input = sys.stdin.readline

n = int(input())
iList = list(map(int, input().split()))

#오름차순으로 버블정렬, 선택정렬, 삽입정렬, 퀵정렬, 병합정렬

# 버블정렬
def bubble(List):
    for i in range(len(List)):
        for j in range(len(List)-i-1):
            if List[j] > List[j+1]:
                List[j],List[j+1] = List[j+1],List[j]
    print(List)
bubble(iList)

# 선택정렬
def select(List):
    for i in range(len(List)):
        min = i
        for j in range(i+1,len(List)):
            if List[j] < List[min]:
                min = j
                List[j],List[min] = List[min],List[j]
    print(List)
select(iList)

# 삽입정렬
def insert(List):
    for i in range(1,len(List)):
        for j in range(i,0,-1):
            if List[j] < List[j-1]:
                List[j],List[j-1] = List[j-1],List[j]
            else:
                break
    print(List)
insert(iList)

# 퀵정렬
def quick(List):
    if len(List) <= 1:
        return List
    
    pivot = List[0]
    tail = List[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick(left) + [pivot] + quick(right)
print(quick(iList))

# 병합정렬
def merge(List):
     if len(List) <= 1:
        return List
    