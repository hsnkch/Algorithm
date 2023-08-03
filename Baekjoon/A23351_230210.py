import sys
input = sys.stdin.readline

N,K,A,B = map(int,input().split())

def water(N, K, A, B):  # 물주기 함수
    list = [K]*N    # 캣닢 배열
    day = 0     # day 초기화
    while 0 not in list:    # 수분이 0이된 캣닢이 없을때까지
        for i in range(A):  # A개의 캣닢에 물주기
            list[i] += B    # B만큼 수분 충전

        for i in range(len(list)):  # 캣닢 전체 list에서
            list[i] -= 1    # 수분 1씩 감소
        
        list.sort()     # 정렬시켜서 안준애들 물주기
        day += 1    # day 증가
    return day  # 수분이 0인 캣닢이 나오면 그 때의 day return

print(water(N,K,A,B))