def solution(s):
    words = s.split(' ')    
    a = []
    for i in words:
        if i:
            b = i[0].upper() + i[1:].lower()
            a.append(b)
        else:
            a.append('')
    
    return ' '.join(a)