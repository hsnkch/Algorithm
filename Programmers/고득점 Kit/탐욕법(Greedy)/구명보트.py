from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while people:
        heaviest = people.pop()
        
        if people and heaviest + people[0] <= limit:
            people.popleft()
            
        answer += 1

    return answer


print(solution( [40, 55, 55, 60, 60, 60, 70, 80], 100 ))