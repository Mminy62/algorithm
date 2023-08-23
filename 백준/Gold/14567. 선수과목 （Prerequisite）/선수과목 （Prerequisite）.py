from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
result = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)#a -> b a를 먼저 들어야함
    indegree[b] += 1

q = deque([])
time = 1
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append((i, time))


while q:
    now, time = q.popleft()
    result[now-1] = time
    for node in graph[now]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append((node, time + 1))

print(' '.join(list(map(str, result))))