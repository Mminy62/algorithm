import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1
result = 0
visited = set(maps[0][0])
def dfs(cur):
    x, y = cur
    global cnt, result
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maps[nx][ny] not in visited:
            visited.add(maps[nx][ny])
            cnt += 1
            dfs((nx, ny))
            cnt -= 1
            visited.remove(maps[nx][ny])
        else:
            result = max(result, cnt)

    return


dfs((0, 0))
print(result)