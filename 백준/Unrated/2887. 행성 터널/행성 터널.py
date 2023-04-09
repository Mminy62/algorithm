import sys
input = sys.stdin.readline

n = int(input())
graph = []
parent = [i for i in range(n)]
edges = []
coorx = []
coory = []
coorz = []

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

for i in range(n):
    x, y, z = map(int, input().split())
    coorx.append((x, i))
    coory.append((y, i))
    coorz.append((z, i))

coorx.sort()
coory.sort()
coorz.sort()

result = 0
for i in range(1, n):
    edges.append((abs(coorx[i-1][0] - coorx[i][0]), coorx[i-1][1], coorx[i][1]))
    edges.append((abs(coory[i - 1][0] - coory[i][0]), coory[i - 1][1], coory[i][1]))
    edges.append((abs(coorz[i - 1][0] - coorz[i][0]), coorz[i - 1][1], coorz[i][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)