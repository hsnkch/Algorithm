import sys
input = sys.stdin.readline

s = input().rstrip()

for i in range(len(s)):
    a = s[i:]
    b= s[i:][::-1]
    if s[i:] == s[i:][::-1]:
        tmp = s+s[:i][::-1]
        print(len(tmp))
        break       