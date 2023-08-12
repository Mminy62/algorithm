n, m, x, y, cnum = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))

#명령어 방향성에 맞게 설정
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

#주사위 dice는 일단 다 0임 (1~6만 쓸 예정)
dice = [0] * 7

for c in cmd:
    nx = x + dx[c]
    ny = y + dy[c]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
        
    if c == 1: # 동쪽이니까 옆면만 굴리기
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    if c == 2: # 왼쪽
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
    if c == 3: #위쪽
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
    if c == 4: # 아래쪽
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]

    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[6]

    else:
        dice[6] = maps[nx][ny]
        maps[nx][ny] = 0

    x, y = nx, ny

    print(dice[1])

