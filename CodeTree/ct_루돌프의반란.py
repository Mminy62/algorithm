'''
P명의 산타들
- 루돌프 이동
: 거리가 가장 가까운 산타 찾기(대각선은 1칸으로 치기)
    - 그 산타 방향으로 1칸 이동 (방향 대각선 포함 8개), 대각선 1칸도 1칸 전진
    - 산타가 여러명이면, r이 큰 산타에게 돌진, r도 같으면 c (정렬의 반대,,, -0, -1)
    => 거리를 기준으로 산타를 찾고, 그 산타에게 가장 빠른 방향으로(대각선 포함) 움직인다.

- 산타 이동(함수)
    - 루돌프에게 거리가 가장 가까워지는 방향 찾기, 1칸 이동
    - 다른 산타가 있는 곳엔 못들어감
    - 움직일 수 있는 칸이 없으면 안움직임
    - 루돌프랑 안가까워지면 산타 움직이지 X
    - 상하좌우, 방향이 여러개면, 상우 하좌 우선순위

충돌(함수)
- 루돌프가 움직여서 충돌 -> 산타 C만큼 점수, 동시에 산타는 루돌프가 이동해온 방향으로 C만큼 밀려남(방향 그대로?)
- 산타가 움직여서 충돌(루돌프랑) -> 산타 D만큼 점수, 동시에 산타는 자신의 방향의 반대 방향으로 D만큼 밀려남
- 밀려날땐 충돌 신경 X -> 그냥 이동, 밀려난 칸에 산타가 있으면 상호작용!, N칸 밖이면 없어짐

상호작용(함수)
- 원래 있던 산타는 해당 방향으로 1칸씩 밀린다. 그 옆에 산타들도 다 1칸씩 밀려난다. (N의 끝에서부터 1칸씩 이동하는 코드)
- 날라온 산타 착지는 원래 칸에 제대로 발생

기절(조건문)
- 산타는 루돌프 충돌&이동 후 기절함
- k번째 턴이면, K + 1번째 턴까지 기절하게 됨(1판 쉬는거)
- 산타만 못 움직임.

게임 종료
- M번의 턴
- P명의 산타가 다 탈락이면 게임 종료
- 매 턴마다 탈락하지 않은 산타들한텐 1점씩 부여(함수)
=> 게임 끝난 후엔 산타가 얻은 최종 점수를 구한다(각각, 1 ~ P까지)


산타, 루돌프 각각 방향 갖고 있어야하고
N, M(겜수), P, C, D


'''

N, M, P, C, D = map(int, input().split())
r1, r2 = map(int, input().split())
rudol = (r1 - 1, r2 - 1, 0)
santas = {}
score = {}
for _ in range(P):
    num, a, b = map(int, input().split())
    santas[num] = [a - 1, b - 1, 0, 0]
    score[num] = 0

# rudol -> -1
# 빈 칸은 0
board = [[0] * N for _ in range(N)]
# 초기값 세팅
board[rudol[0]][rudol[1]] = -1
for i in range(1, P + 1):
    x, y, direct, rest = santas[i]
    board[x][y] = i

rdx = [-1, -1, 0, 1, 1, 1, 0, -1]
rdy = [0, 1, 1, 1, 0, -1, -1, -1]

sdx = [-1, 0, 1, 0]
sdy = [0, 1, 0, -1]


# 게임 시작마다 산타가 있는지 체크


def search_rudol(rudol):
    x, y, d = rudol
    ans = 0  # 우선순위가 높은 산타의 번호
    ax, ay = 0, 0  # 우선순위가 높은 산타의 좌표
    distance = 50 ** 4
    for idx, (sx, sy, sd, rest) in santas.items():
        temp = abs(x - sx) ** 2 + abs(y - sy) ** 2
        if distance > temp:
            distance = temp
            ans = idx
            ax, ay = sx, sy
        elif distance == temp and (sx, sy) > (ax, ay):
            ax, ay = sx, sy
            ans = idx
    return ans


# 산타 번호로 보내주기
def move_rudol(rudol, santa):  # 루돌프 좌표 및 방향 보내주기
    rx, ry, rd = rudol
    sx, sy, sd, rest = santa

    ax, ay, ad = 0, 0, 0
    distance = N * 4
    for i in range(8):
        nx = rx + rdx[i]
        ny = ry + rdy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        temp = abs(nx - sx) ** 2 + abs(ny - sy) ** 2
        if distance > temp:
            distance = temp
            ax, ay, ad = nx, ny, i

    if board[ax][ay] > 0:  # 루돌프 이동에 산타가 있었다면
        crash(ax, ay, "C", ad, board[ax][ay])

    board[rx][ry] = 0
    board[ax][ay] = -1


    return (ax, ay, ad)

# 충돌 후 산타 이동
def crash(sx, sy, size, di, santa_num):  # 산타 현재위치, 밀려난 크기, 방향, 산타 번호
    nx, ny = 0, 0
    dx, dy = 0, 0
    value = 0
    if size == "D":
        di = (di + 2) % 4
        nx = sx + sdx[di] * D
        ny = sy + sdy[di] * D
        value = D
        dx, dy = sdx[di], sdy[di]

    if size == "C":
        nx = sx + rdx[di] * C
        ny = sy + rdy[di] * C
        value = C
        dx, dy = rdx[di], rdy[di]

    score[santa_num] += value

    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        del santas[santa_num]
        return
    if board[nx][ny] == 0:
        board[nx][ny] = santa_num
        santas[santa_num][0], santas[santa_num][1] = nx, ny

    elif board[nx][ny] > 0:#상호작용
        interaction(nx, ny, santa_num, dx, dy)

    santas[santa_num][3] = k + 2
    return

# 산타 이동
def interaction(nx, ny, santa_num, dx, dy):

    while True:
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            del santas[santa_num]
            break
        if board[nx][ny] == 0:
            santas[santa_num][0], santas[santa_num][1] = nx, ny
            board[nx][ny] = santa_num
            break

        if board[nx][ny] > 0:
            temp = board[nx][ny]
            santas[santa_num][0], santas[santa_num][1] = nx, ny
            board[nx][ny] = santa_num
            santa_num = temp
            nx += dx
            ny += dy

    return


def santa_move(rudol, santa_num, k):
    rx, ry, rd = rudol
    sx, sy, sd, rest = santas[santa_num]
    if rest > 0 and k != rest:
        return
    if rest > 0 and k == rest:
        santas[santa_num][3] = 0

    distance = abs(rx - sx) ** 2 + abs(ry - sy) ** 2 + 1

    result = []
    min_dist = abs(rx - sx) ** 2 + abs(ry - sy) ** 2 + 1
    # 방향 찾아서 움직이기
    for i in range(4):
        nx = sx + sdx[i]
        ny = sy + sdy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        temp = abs(rx - nx) ** 2 + abs(ry - ny) ** 2
        if distance > temp and board[nx][ny] <= 0:
            distance = temp
            result.append((temp, nx, ny, i))
            min_dist = min(min_dist, temp)

    for dist, ax, ay, ad in result:
        if min_dist == dist:
            if board[ax][ay] == -1:# 루돌프랑 충돌
                # 충돌
                board[sx][sy] = 0
                crash(ax, ay, "D", ad, santa_num)

            else: # 빈 칸일때
                board[sx][sy] = 0
                board[ax][ay] = santa_num
                santas[santa_num][0], santas[santa_num][1] = ax, ay

    return


for k in range(1, M + 1):
    if not santas.keys():
        break
    santa_num = search_rudol(rudol)
    rudol = move_rudol(rudol, santas[santa_num])

    keys = sorted(santas.copy().keys())
    for i in keys:
        if i in santas.keys():
            santa_move(rudol, i, k)

    for key in santas.keys():
        score[key] += 1


sorted_score = dict(sorted(score.items(), key=lambda x: x[0]))
print(' '.join(list(map(str, sorted_score.values()))))