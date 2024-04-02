N, L = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
def check(x, y, dx, dy):

    # L번 반복
    nx, ny = x, y
    for _ in range(L-1):
        nx += dx
        ny += dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return False
        if visited[nx][ny]:
            return False
        if board[nx][ny] != board[x][y]:
            return False

    nx, ny = x, y
    for _ in range(L - 1):
        nx += dx
        ny += dy
        visited[nx][ny] = True

    return True

ans = 0

for i in range(N):
    cnt = 1
    flag = False
    for j in range(N-1):
        if j == 0:
            cnt = 1
        if j != 0 and board[i][j] == board[i][j-1] and L != 1:
            cnt += 1
        if board[i][j] != board[i][j + 1]:
            if board[i][j] + 1 == board[i][j + 1]:# 왼쪽이 더 작은 경우
                # 왼쪽 방향으로 체크
                if not visited[i][j] and check(i, j, 0, -1):
                    visited[i][j] = True
                else:
                   # j 이동
                    flag = True
                    break

            elif board[i][j] == board[i][j + 1] + 1:# 오른쪽이 더 작은 경우
                if not visited[i][j + 1] and check(i, j + 1, 0, 1):
                    visited[i][j + 1] = True
                    j += L
                else:
                    flag = True
                    break
            elif abs(board[i][j] - board[i][j + 1]) > 1:
                flag = True
                break

    if flag:
        continue
    else:
        ans += 1


# 위, 아래 비교
visited = [[False] * N for _ in range(N)]
for j in range(N):
    cnt = 1
    flag = False
    for i in range(N-1):
        if j == 0:
            cnt = 1
        if j != 0 and board[i][j] == board[i][j-1] and L != 1:
            cnt += 1
        if board[i][j] != board[i + 1][j]:
            if board[i][j] + 1 == board[i + 1][j]:# 아래가 더 큰 경우
                # 위쪽 방향으로 체크
                if not visited[i][j] and check(i, j, -1, 0):
                    visited[i][j] = True
                else:
                   # j 이동
                    flag = True
                    break

            elif board[i][j] == board[i + 1][j] + 1:# 아래가 더 작은 경우
                if not visited[i + 1][j] and check(i + 1, j, 1, 0):
                    visited[i + 1][j] = True
                    i += L
                else:
                    flag = True
                    break
            elif abs(board[i][j] - board[i + 1][j]) > 1:
                flag = True
                break

    if flag:
        continue
    else:
        ans += 1

print(ans)