def solution(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    sqrt = int(n ** 0.5)

    for i in range(3, sqrt + 1, 2):
        if n % i == 0:
            return False

        return True
    
print(solution(123))