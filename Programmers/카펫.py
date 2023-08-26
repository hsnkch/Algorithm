def solution(brown, yellow):
    answer = []

    for h in range(3, int((brown+yellow)**0.5)+1):
        if (brown + yellow) % h == 0:
            answer.append(((brown + yellow) // h, h))

    for width, height in answer:
        if (width - 2) * (height - 2) == yellow:
            answer = [width, height]
 
    return answer

print(solution(24,24))