import heapq
import sys
input = sys.stdin.readline

INF = 1e9
n, k = map(int, input().split())
graph = [[] for _ in range(100001)]
distance = [INF] * (100001)
q = []
if n == k:
    print(0)
else:
    heapq.heappush(q, (0, n))

    while q:
        dist, cur = heapq.heappop(q)
        if cur == k:
            break

        if distance[cur] < dist:
            continue

        graph[cur].append((0, cur * 2))
        graph[cur].append((1, cur - 1))
        graph[cur].append((1, cur + 1))

        for i in graph[cur]:
            cost = dist + i[0]

            if 0 <= i[1] < 100001 and cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


    print(distance[k])