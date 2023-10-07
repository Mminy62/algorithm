'''
# 이동하는 칸인 250칸 하나 더 만들기
- 모든 파이어볼은 자신의 방향으로 속력만큼 이동한다
'''
import math
from copy import deepcopy

# move
# 일단 방향대로 속력만큼 움직이기, (현재칸 + dx[i] * 속력) % N 만큼 이동시키기
# 각 배열에 추가하기
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def move(board):
    nboard = [[[]for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]: #비어있지 않으면
                while board[i][j]:
                    m, s, d = board[i][j].pop()
                    nx = (i + dx[d] * s) % N
                    ny = (j + dy[d] * s) % N
                    nboard[nx][ny].append((m, s, d))
    return nboard

# 새거에서 2개이상의 볼 4개로 나누기
# 다 나누면 new -> b로 바꾸기는 return
def divide(nboard):
    for i in range(N):
        for j in range(N):
            if len(nboard[i][j]) > 1:
                num = len(nboard[i][j])
                weight, speed, direction = 0, 0, [0]
                dd = [0, 0]
                for k in range(num):
                    m, s, d = nboard[i][j].pop()
                    weight += m
                    speed += s
                    dd[d % 2] += 1
                weight = math.floor(weight/5)
                speed = math.floor(speed/num)
                if dd[0] == num or dd[1] == num:
                    direction = [0, 2, 4, 6]
                else:
                    direction = [1, 3, 5, 7]

                if weight != 0:
                    for dd in range(4):
                        nboard[i][j].append((weight, speed, direction[dd]))

    return nboard

N, M, K = map(int, input().split())
# m개의 볼 정보를 입력받으면, 초기 board에 (m, s, d) 순으로 넣어놓는다.
board = [[[]for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append((m, s, d))

while K:
    new = move(board)
    board = divide(new)
    K -= 1

# 질량 더하기
answer = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            answer += sum(board[i][j][k][0] for k in range(len(board[i][j])))

print(answer)