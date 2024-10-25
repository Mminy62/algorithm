import heapq
INF = int(1e9)
N, end = map(int, input().split())
graph = [[] for _ in range(end + 1)]
distance = [INF] * (end + 1)

for i in range(end):
    graph[i].append((i+1, 1)) # 바로 옆에거랑 연결지어서 쭉쭉 가도록

for _ in range(N):
    start, dest, length = map(int, input().split())
    if dest <= end:
        graph[start].append((dest, length))

queue = []
heapq.heappush(queue, (0,0))
distance[0] = 0

while queue:
    w1, u = heapq.heappop(queue)

    for v, w2 in graph[u]:
        cost = distance[u] + w2
        if distance[v] > cost:
            distance[v] = cost
            heapq.heappush(queue, (cost, v))
print(distance[end])