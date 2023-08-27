# def solution(prices):
#     answer = []
#     for idx, price in enumerate(prices):
#         cnt = 0
#         for j in range(idx+1, len(prices)):
#             if price <= prices[j]:
#                 cnt += 1      
#         answer.append(cnt+1)
                     
#     return answer


def solution(prices):
    # 가격이 떨어지지 않은 시간을 저장하는 리스트
    answer = [0] * len(prices)
    
    # 가격의 인덱스를 저장하는 스택
    stack = []  

    # 하락할때
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    # 하락 x
    while stack:
        k = stack.pop()
        answer[k] = len(prices) - 1 - k
        
    return answer

print(solution([1, 2, 3, 2, 3]))