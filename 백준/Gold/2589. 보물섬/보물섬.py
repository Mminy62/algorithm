from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(input().rstrip()))

#육지 리스트 담기
lands = deque([])
for i in range(n):
    for j in range(m):
        if array[i][j] == 'L':
            lands.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for x, y in lands:
    q = deque([(0, x, y)])
    visited = [[False] * m for _ in range(n)]
    distance = 0

    while q:
        cost, cx, cy = q.popleft()
        if not visited[cx][cy]:
            visited[cx][cy] = True
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if array[nx][ny] == 'W' or visited[nx][ny]:
                    continue

                # 방문하지 않은 land 인 경우
                q.append((cost + 1, nx, ny))
                distance = max(distance, cost + 1)

    result = max(result, distance)

print(result)