from collections import deque
from copy import deepcopy
n = int(input())

indegree = [0] * (n + 1)
time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for j in range(2, len(tmp)):
        pre = tmp[j]
        graph[pre].append(i)
        indegree[i] += 1
    time[i] = tmp[0]
# 각 작업마다 선행작업이 무엇인지 graph에 표기 & indegree


# 다 끝나면 indegree가 0인 작업 추가하는 것
q = deque([])
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

dp = [0] * (n + 1)
for node in q:
    dp[node] = time[node]

# q 작업 시작
while q:
    now = q.popleft()
    for nxt in graph[now]:
        dp[nxt] = max(dp[nxt], time[nxt] + dp[now])
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

print(max(dp))