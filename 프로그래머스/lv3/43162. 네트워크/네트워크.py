def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    answer = 0
    parent = [0] * n
    edges = []

    for i in range(n):
        parent[i] = i

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union_parent(parent, i, j)


    for i in range(n):
        if i == parent[i]:
            answer += 1
            
    return answer