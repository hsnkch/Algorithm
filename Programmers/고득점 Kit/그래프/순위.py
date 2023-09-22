def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]

    for win, lose in results:
        graph[win].append(lose)




    return answer

print(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])