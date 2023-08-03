coordinates = [(1,0),(0,3),(1,3),(2,3),(0,2),(1,2),(2,2),(0,1),(1,1),(2,1)]
left_now = [(0,0)]
right_now = [(2,0)]

def solution(numbers, hand):
    answer = ''
    for number in numbers:
        if number==1 or number==4 or number==7:
            answer += 'L'
            left_now.append(coordinates[number])
        elif number==3 or number==6 or number==9:
            answer += 'R'
            right_now.append(coordinates[number])
        else:
            answer += position(number, hand, left_now[-1], right_now[-1])
    return answer

def position(number, hand, l_now, r_now):
    x,y = coordinates[number]
    rx, ry = r_now
    lx, ly = l_now
    r_distance = abs(x-rx)+abs(y-ry)
    l_distance = abs(x-lx)+abs(y-ly)
    if r_distance > l_distance:
        left_now.append(coordinates[number])
        return 'L'
    elif r_distance < l_distance:
        right_now.append(coordinates[number])
        return 'R'
    else:
        if hand=='right':
            right_now.append(coordinates[number])
            return 'R'
        elif hand=='left':
            left_now.append(coordinates[number])
            return 'L'


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"right"))