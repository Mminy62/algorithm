import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]]
for i in range(1, n + 1):
    graph.append([0] + list(map(int, input().split())))

info = []
for _ in range(m):
    info.append(list(map(int, input().split())))

#플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(m):
    a, b, c = info[i]
    cost = graph[a][b]
    if cost <= c:
        print('Enjoy other party')
    else:
        print('Stay here')