def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # 끝나는 지점을 기준으로 오름차순 정렬

    camera = -30001  # 카메라 위치 초기화 (범위를 벗어나는 값으로 설정)

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]  # 현재 카메라 위치 갱신

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))