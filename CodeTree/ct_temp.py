
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input()))))

visited = [[False] * m for _ in range(n)]
# 3개의 육지를 가진 땅의 수
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, cnt):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[nx][ny] == 0:
            continue

        if not visited[nx][ny] and arr[nx][ny] == 1:
            visited[nx][ny] = True
            cnt = dfs(nx, ny, cnt + 1)

        # 넘어가는지 확인
        # 안넘어가면 cnt +1 한걸로 돌리기

    return cnt

def check():
    global ans
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                temp = dfs(i, j, 1)
                if temp == 3:
                    ans += 1

    return ans


# 1이고 not visited일때 dfs, 상하좌우 체크

print(check())

