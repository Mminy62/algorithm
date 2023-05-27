import sys
import heapq
input = sys.stdin.readline
INF = 1e9
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    cost, cur = heapq.heappop(q)

    if distance[cur] < cost:
        continue
    for node in graph[cur]:
        b, c = node
        dist = cost + c
        if dist < distance[b]:
            distance[b] = dist
            heapq.heappush(q, (dist, b))

for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])