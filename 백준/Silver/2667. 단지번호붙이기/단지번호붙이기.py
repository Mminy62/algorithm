N = int(input())
board = []
for _ in range(N):
    temp = list(input())
    board.append(list(map(int, temp)))

visited = [[False] * N for _ in range(N)]

# 방문했는지는 visited를 global로

# dfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, node):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            node = dfs(nx, ny, node + 1) # 깊게 들어간 후 막힌 곳에 대한 Node를 가져오는 것. 가져온 노드는 또 그 값에 더해서 계속 더함

    return node

cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if board[i][j] and not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            result.append(dfs(i, j, 1))

print(cnt)
result.sort()
for item in result:
    print(item)