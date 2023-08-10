import math
def solution(progresses, speeds):
    days = []
    answer = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    print(days)
    while days:
        now = days.pop(0)
        cnt = 1

        for _ in range(len(days)):
            if now >= days[0]:
                cnt += 1
                days.pop(0)
        
        answer.append(cnt)

    return answer


# 다른 풀이
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]



print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))