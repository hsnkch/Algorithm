import sys

a, b = list(map(int, sys.stdin.readline().split()))

q = int('1'*a)
r = int('1'*b)

def rest(aa, bb):
    if aa > bb:
        if z != 0:
            z = aa % bb
            rest(z, bb)
        else:
            return 1
    else :
        if z != 0:
            z = bb % aa
            rest(aa, z)
        else:
            return 2    
        
print(rest(q,r))