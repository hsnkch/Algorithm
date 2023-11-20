import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    
    max_profit = 0 
    max_price = 0
    
    for i in range(len(price)-1,-1,-1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            max_profit += max_price - price[i]
    
    print(max_profit)

