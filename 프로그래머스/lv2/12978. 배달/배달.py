import heapq

INF = int(10e9)


def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    distance[1] = 0

    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    #dijkstra
    q = []
    heapq.heappush(q, (0, 1))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


    for node in distance:
        if node <= K:
            answer += 1

    return answer