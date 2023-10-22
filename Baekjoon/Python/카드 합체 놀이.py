import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))

while m > 0:
    tmp = cards[0] + cards[1]
    cards[0] = tmp
    cards[1] = tmp
    cards.sort()
    m -= 1

print(sum(cards))

