import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
array = []
q = deque([])

# visited 초기화
visited = [[False] * m for _ in range(n)]
# input -> array

for i in range(n):
    row = list(map(int, input().split()))
    for j, value in enumerate(row):
        if value == 1:
            q.append((i, j))
            visited[i][j] = True
        if value == -1:
            visited[i][j] = True
    array.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
days = 0

def BFS(q):
    next_q = deque([])
    for _ in range(len(q)):
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if array[nx][ny] == -1:
                visited[nx][ny] = True
                continue
            if array[nx][ny] == 0 and not visited[nx][ny]:
                array[nx][ny] = 1
                visited[nx][ny] = True
                next_q.append((nx, ny))

    return next_q

def check(days):
    for i in range(n):
        if False in visited[i]:
            return -1
    if days:
        days -= 1
    return days

while q:
    q = BFS(q)
    days += 1

print(check(days))