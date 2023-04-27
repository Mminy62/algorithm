import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
start = (0, 0)
for i in range(n):
    temp = list(map(int, input().split()))
    if 2 in temp:
        j = temp.index(2)
        start = (i, j)
        distance[i][j] = 0
    graph.append(temp)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            distance[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([start])
while q:
    x, y = q.popleft()
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1 and not visited[nx][ny]:
            q.append((nx, ny))
            visited[nx][ny] = True
            distance[nx][ny] = distance[x][y] + 1


for i in range(n):
    print(*distance[i])