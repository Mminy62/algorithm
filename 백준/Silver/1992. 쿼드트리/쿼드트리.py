n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input())))
answer = ''

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

def check(x, y, n):
    flag = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != flag:
                return False
    return True

def dfs(x, y, size):
    global answer
    global board
    if not check(x, y, size):
        answer += '('
        for i in range(4):
            small_size = size // 2
            nx, ny = x + dx[i] * small_size, y + dy[i] * small_size
            dfs(nx, ny, small_size)
        answer += ')'
    else:# check 통과면
        answer += str(board[x][y])

    return
# 구역 탐색
dfs(0, 0, n)

print(answer)