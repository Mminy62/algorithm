N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, list(input()))))

visited = [[False] * N for _ in range(N)]
cnt = 0
def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if board[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        cnt += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

    return

group = 0
arr = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            group += 1
            dfs(i, j)
            arr.append(cnt)
            cnt = 0

print(group)
arr.sort()
for num in arr:
    print(num)