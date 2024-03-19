from itertools import combinations
import sys
input = sys.stdin.readline
INF = 10e9

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드워셜
for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cities = [i for i in range(1, N + 1)]# 조합으로 2개씩 뽑아놓은것 만들기
chickens = list(combinations(cities, 2))

# 각 도시별로 2개 치킨집에 대한 최소 거리를 저장한다

result = (10e9, 1, 2)
for chicken in chickens:
    a, b = chicken
    temp = 0
    for city in cities:
        temp += min(graph[city][a], graph[city][b])
    if result > (temp, a, b):
        result = (temp, a, b)

print(result[1], result[2], result[0] * 2)