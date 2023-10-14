import sys
input = sys.stdin.readline

n = int(input())
iList = list(map(int,input().split()))
sList = sorted(set(iList))  # 중복제거해서 먼저 정렬

dic={}  # 압축할 좌표와 기존 좌표를 담을 dic

for i in range(len(sList)): # dic 생성
    dic[sList[i]] = i

for i in range(n):  # 기존 좌표에 따라서 dic의 값 출력
    print("%d " %dic[int(iList[i])], end='')