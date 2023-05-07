from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque([(0, 0)])


while(q):
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1 and not visited[nx][ny]:
            graph[nx][ny] += graph[x][y]
            q.append((nx, ny))
            visited[nx][ny] = True

print(graph[n-1][m-1])