from itertools import permutations
def numsNsyms(expression):
    num = []
    sym = []
    temp = ''

    for i in expression:
        if i.isdigit():
            temp += i
        else:
            if temp:
                num.append(int(temp))
                temp = ''
            sym.append(i)
    
    if temp:
        num.append(int(temp))

    return num, sym

def cal (a, b, symbol):
    if symbol == '+':
        return a + b
    if symbol == '-':
        return a - b
    if symbol == '*':
        return a * b

def solution(expression):
    num, sym = numsNsyms(expression)
    result = []
    
    perm = permutations(list(set(sym)))
    for i in perm:
        print(i)
        for j in range(len(num)):
            cal

    answer = 0
    return num,sym

print(solution("100-200*300-500+20"))