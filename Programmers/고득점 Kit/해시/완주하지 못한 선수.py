def solution(participant, completion):
    dic = {}

    for i in participant:
        dic[i] = dic.get(i, 0) + 1

    for j in completion:
        dic[j] -= 1

    for person, count in dic.items():
        if count > 0:
            return person

# 다른 풀이        
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))