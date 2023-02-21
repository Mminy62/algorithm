import sys

input = sys.stdin.readline
INF = int(10e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)


# graph 초기화
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cost = graph[i][k] + graph[k][j]
            graph[i][j] = min(graph[i][j], cost)

for i in range(1, n + 1):
    print(*[0 if num == INF else num for num in graph[i][1:]])