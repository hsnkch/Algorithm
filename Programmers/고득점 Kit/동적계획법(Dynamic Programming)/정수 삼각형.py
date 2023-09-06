def solution(triangle):
    # answer = 0
    # dp=[0]*len(triangle)
    # dp[0] = triangle[0][0]

    # for i in range(1, len(triangle)):
    #     for j in range(len(triangle[i])):
    #         dp[i] = max(dp[i], dp[i-1] + triangle[i][j])

    # return max(dp)

    # 삼각형의 높이
    n = len(triangle)
    
    # 각 위치까지의 최대 합을 저장할 2차원 리스트
    dp = [[0] * n for _ in range(n)]
    
    # 초기값 설정 (맨 위의 숫자)
    dp[0][0] = triangle[0][0]
    
    # 다이나믹 프로그래밍을 사용하여 최대 합 계산
    for i in range(1, n):       # 층 수
        for j in range(i + 1):      # 각 층의 숫자
            if j == 0:      # 가장 왼쪽의 숫자
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:        # 가장 오른쪽의 숫자
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:       # 경로 2개 중 최대값
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    
    # 최대 합 중 최댓값 찾기
    answer = max(dp[n - 1])
    
    return answer




print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))