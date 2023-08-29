from itertools import product
def solution(word):
    answer = 0
    words = 'AEIOU'
    list = []

    for i in range(len(words)):
        for j in product(words, repeat=i+1):
            list.append(''.join(j))

    list.sort()
    
    return list.index(word)+1

print(solution("AAAA"))