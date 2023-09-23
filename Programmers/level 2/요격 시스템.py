def solution(targets):
    answer = 0
    targets.sort(key = lambda x:x[1])
    missile = 0
    for i in range(len(targets)):
        if missile <= targets[i][0] :
            answer += 1
            missile = targets[i][1] 
            



    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))