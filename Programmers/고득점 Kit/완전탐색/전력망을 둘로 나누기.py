def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(node, parent):
        size = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                size += dfs(neighbor, node)
        return size
    
    min_difference = float('inf')
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        size_a = dfs(a, b)
        size_b = n - size_a
        
        min_difference = min(min_difference, abs(size_a - size_b))
        
        graph[a].append(b)
        graph[b].append(a)
    
    return min_difference


print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))