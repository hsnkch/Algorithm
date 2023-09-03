def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x:x[2])
    parent = [0] * n
    for i in range(n):     # 자기 자신으로 부모 노드 설정
        parent[i] = i

    for i in costs:
        a, b, cost = i
        if find_parent(parent, a) != find_parent(parent, b):    # 부모 노드가 같으면 경로에 포함 X
            union_parent(parent, a, b)
            answer += cost

    return answer

def find_parent(parent,x):  # 재귀로 부모 노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):   
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b




print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))