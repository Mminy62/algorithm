from collections import deque
import sys
n, m, k, x = map(int, sys.stdin.readline().split())
adjList = [[] for _ in range(n+1)]
for _ in range(m):
    data = list(map(int,sys.stdin.readline().split()))
    adjList[data[0]].append(data[1])

queue = deque([x])
distance = [0] * (n + 1)
visited = [False] * (n+1)
visited[x] = True

while queue:
    x = queue.popleft()
    if adjList[x]:
        for v in adjList[x]:
            if not visited[v]:
                distance[v] = distance[x] + 1
                visited[v] = True
                queue.append(v)

answer = True
for i, v in enumerate(distance):
    if v == k:
        print(i)
        answer = False

if answer:
    print(-1)