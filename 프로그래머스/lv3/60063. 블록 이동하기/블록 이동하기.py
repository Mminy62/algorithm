from collections import deque

def get_next_pos(new_board, pos):
    next_pos_list = []
    pos = list(pos)

    pos_x1, pos_y1, pos_x2, pos_y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 상하좌우는 똑같이 적용
    for i in range(4):
        nx1 = pos_x1 + dx[i]
        ny1 = pos_y1 + dy[i]
        nx2 = pos_x2 + dx[i]
        ny2 = pos_y2 + dy[i]

        if new_board[nx1][ny1] == 1 or new_board[nx2][ny2] == 1:
            continue
        if new_board[nx1][ny1] == 0 and new_board[nx2][ny2] == 0:
            next_pos_list.append({(nx1, ny1), (nx2, ny2)})

    #가로인 경우
    if pos_x1 == pos_x2:
        for i in [-1, 1]:  # 위쪽으로 회전하거나, 아래쪽으로 회전
            if new_board[pos_x1 + i][pos_y1] == 0 and new_board[pos_x2 + i][pos_y2] == 0:  # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                next_pos_list.append({(pos_x2, pos_y1), (pos_x1 + i, pos_y1)})
                next_pos_list.append({(pos_x2, pos_y2), (pos_x2 + i, pos_y2)})
    #세로인 경우
    elif pos_y1 == pos_y2:
        for i in [-1, 1]:  # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if new_board[pos_x1][pos_y1 + i] == 0 and new_board[pos_x2][pos_y2 + i] == 0:  # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                next_pos_list.append({(pos_x1, pos_y1), (pos_x1, pos_y1 + i)})
                next_pos_list.append({(pos_x2, pos_y2), (pos_x2, pos_y2 + i)})

    return next_pos_list


def solution(board):
    answer = 0
    #2칸짜리 로봇이 벽 넘는 것 감지에 편하기 위해
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]


    start = {(1, 1), (1, 2)}
    cost = 0
    pos_queue = deque()
    pos_queue.append((start, cost))

    visited = [start]
    while pos_queue:
        pos, cost = pos_queue.popleft()

        if (n, n) in pos:
            return cost

        next_pos_list = get_next_pos(new_board, pos)

        for next_pos in next_pos_list:
            if next_pos not in visited:
                pos_queue.append((next_pos, cost + 1))
                visited.append(next_pos)

    return answer