def solution(s):
    cnt = 0
    zero_count = 0

    while s != "1":
        zero_count += s.count('0')
        s = s.replace('0', '')
        
        s = bin(len(s))[2:]
        
        cnt += 1
        

    return [cnt, zero_count]





