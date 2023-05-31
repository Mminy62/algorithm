
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, direct = map(int, input().split())

room = []

for _ in range(n):
    room.append(list(map(int, input().split())))


def check(x, y, di): # 4개 방향 확인 -> 있으면 True, 없으면 False

    for i in range(di, di + 4):
        nx = x + dx[i % 4]
        ny = y + dy[i % 4]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return False
        if room[nx][ny] == 0:
            return True

    return False


ans = 0
#1 - 벽, 2 - 청소됨, 0 - 청소안됨
while True:
    # 1. 현재 칸 청소 x -> 청소하기
    if room[x][y] == 0:
        room[x][y] = 2
        ans += 1

    # 2. 현재 칸 주변 4칸의 청소가 다 되면
    # 바라보는 방향으로 뒤로 한칸 후진
    if not check(x, y, direct):
        nx = x - dx[direct]
        ny = y - dy[direct]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        if room[nx][ny] == 1:# 후진이 벽인 경우
            break
        else:
            x, y = nx, ny
            continue
    # 3. 주변에 청소 안된 구역이 있는 경우
    else:
        # 반시계 방향으로 90도 회전
        direct = (direct - 1) % 4
        nx = x + dx[direct]
        ny = y + dy[direct]
        if room[nx][ny] == 0:
            x, y = nx, ny

print(ans)