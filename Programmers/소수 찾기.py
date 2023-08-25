import math
from itertools import permutations
def solution(numbers):
    answer = 0    
    nums = set()

    for i in range(1, len(numbers)+1):
        perms = permutations(numbers, i)

        for perm in perms:
            num = int(''.join(perm))
            nums.add(num)
        
    for num in nums:
        if is_prime(num) == True:
            answer += 1    
    return answer

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    sqrt_num = int(math.sqrt(number))
    for i in range(3, sqrt_num + 1):
        if number % i == 0:
            return False
    
    return True

print(solution("17"))