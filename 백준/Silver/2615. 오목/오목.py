n = 19
blacks = []
whites = []
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            blacks.append((i, j))
        elif board[i][j] == 2:
            whites.append((i, j))


def search(omoks):
    dx = [1, 1, 0, -1]
    dy = [1, 0, 1, 1]

    for x, y in omoks:
        for i in range(4):
            cnt = 0
            for k in range(1, 6):
                nx = x + dx[i] * k
                ny = y + dy[i] * k
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if (nx, ny) not in omoks:
                    break  # another directions
                if (nx, ny) in omoks:
                    cnt += 1

            tx = x - dx[i]
            ty = y - dy[i]
            if (tx, ty) not in omoks and cnt == 4:
                return (x+1, y+1)

    return False

black_result = search(blacks)
white_result = search(whites)
if black_result:
    print(1)
    print(*black_result)
elif white_result:
    print(2)
    print(*white_result)
else:
    print(0)