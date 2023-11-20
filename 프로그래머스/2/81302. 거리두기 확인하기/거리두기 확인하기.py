def checkVH(person, board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 상하좌우로 탐색
    for i in range(len(person)):
        x, y = person[i]

        for d in range(4):
            nx = x + 2 * dx[d]
            ny = y + 2 * dy[d]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if board[nx][ny] == "P" and board[nx - dx[d]][ny - dy[d]] == "X":
                continue
            # 바로 옆에 붙어있거나, 건너 있어도 가림막이 없는 경우
            if board[nx - dx[d]][ny - dy[d]] == "P" or board[nx][ny] == "P":
                return 0
    return 1

def checkH(person, board):
    # 대각선 탐색
    # 각각 -dx, -dy한 것
    rx = [-1, -1, 1, 1]
    ry = [-1, 1, 1, -1]

    for i in range(len(person)):
        x, y = person[i]

        for d in range(4):
            nx = x + rx[d]
            ny = y + ry[d]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if board[nx][ny] == "P" and board[nx - rx[d]][ny] == "X" and board[nx][ny - ry[d]] == "X":
                continue
            if board[nx][ny] == "P":
                return 0
    return 1

def solution(places):
    answer = []

    index = -1
    while index < 4:
        index += 1
        arr = places[index]
        board = [[0] * 5 for _ in range(5)]
        person = []

        for i in range(5):
            for j in range(5):
                if arr[i][j] == "P":
                    person.append((i, j))
                board[i][j] = arr[i][j]



        if not checkVH(person, board):
            answer.append(0)
            continue
        if not checkH(person, board):
            answer.append(0)
            continue
        answer.append(1)



    return answer

'''
~2:00

- 대기실은 5개, 각 대기실은 5 * 5크기
- 거리두기를 위해 각자 좌표거리간격으로 2이하로 앉지 말기
단 파티션으로 막혀있으면 거리가 짧아도 허용
-> 파티션은 가로 세로면 한칸씩 띄어서, 
대각선으로 앉아있으면 최소 파티션 2개 필요

한명이라도 안지키면 0, 모두 거리두기 잘 지키고 있으면 1을 반환 
각 대기실별로 결과 반환
'''