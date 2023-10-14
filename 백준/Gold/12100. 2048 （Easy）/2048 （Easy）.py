from copy import deepcopy
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def up(board):
    for y in range(n):
        pointer = 0
        for x in range(1, n):
            temp = board[x][y]
            if board[x][y]:# 현재 위치에 값이 있는 경우만
                # 값이 없는 경우, 이동 후 포인터는 안옮기기
                if board[pointer][y] == 0:
                    board[pointer][y] = board[x][y]
                    board[x][y] = 0

                else:#포인터에 값이 있는 경우
                    if board[pointer][y] == board[x][y]:
                        board[pointer][y] *= 2
                        board[x][y] = 0
                        pointer += 1
                    else: #안 같으면
                        pointer += 1
                        board[x][y] = 0
                        board[pointer][y] = temp
    return board

def down(board):
    for y in range(n):
        pointer = n-1
        for x in range(n-2, -1, -1):
            temp = board[x][y]
            if board[x][y]:# 현재 위치에 값이 있는 경우만
                # 값이 없는 경우, 이동 후 포인터는 안옮기기
                if board[pointer][y] == 0:
                    board[pointer][y] = board[x][y]
                    board[x][y] = 0

                else:#포인터에 값이 있는 경우
                    if board[pointer][y] == board[x][y]:
                        board[pointer][y] *= 2
                        board[x][y] = 0
                        pointer -= 1
                    else: #안 같으면
                        pointer -= 1
                        board[x][y] = 0
                        board[pointer][y] = temp
    return board

def left(board):
    for x in range(n):
        pointer = 0
        for y in range(1, n):
            temp = board[x][y]
            if board[x][y]:# 현재 위치에 값이 있는 경우만
                # 값이 없는 경우, 이동 후 포인터는 안옮기기
                if board[x][pointer] == 0:
                    board[x][pointer] = board[x][y]
                    board[x][y] = 0

                else:#포인터에 값이 있는 경우
                    if board[x][pointer] == board[x][y]: #같은 경우
                        board[x][pointer] *= 2
                        board[x][y] = 0
                        pointer += 1
                    else: #안 같으면
                        pointer += 1
                        board[x][y] = 0
                        board[x][pointer] = temp

    return board

def right(board):
    for x in range(n):
        pointer = n-1
        for y in range(n-2, -1, -1):
            temp = board[x][y]
            if board[x][y]:# 현재 위치에 값이 있는 경우만
                # 값이 없는 경우, 이동 후 포인터는 안옮기기
                if board[x][pointer] == 0:
                    board[x][pointer] = board[x][y]
                    board[x][y] = 0

                else:#포인터에 값이 있는 경우
                    if board[x][pointer] == board[x][y]: #같은 경우
                        board[x][pointer] *= 2
                        board[x][y] = 0
                        pointer -= 1
                    else: #안 같으면
                        pointer -= 1
                        board[x][y] = 0
                        board[x][pointer] = temp

    return board

def dfs(board, cnt):
    if cnt == 5:
        return max(map(max, board))

    return max(dfs(up(deepcopy(board)), cnt + 1), dfs(down(deepcopy(board)), cnt + 1), dfs(left(deepcopy(board)), cnt + 1), dfs(right(deepcopy(board)), cnt + 1))


print(dfs(board, 0))