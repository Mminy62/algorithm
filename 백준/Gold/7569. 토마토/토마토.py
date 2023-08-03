'''
- 익은 토마토의 자리 위치, 토마토 위치(-1 출력을 위해) 자리 받아놓기
- 익은 토마토부터 BFS 시작 전염된 것은 큐에 넣기
- day를 포함해서 큐에 넣기
- day가 빠른 것부터 꺼내쓰는 우선순위큐
- 마지막 day 출력
'''
import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[] for _ in range(H)]
pos = []
q = deque([])
result = -1

# input
for i in range(H):
    for j in range(N):
        line = list(map(int, input().split()))
        box[i].append(line)
        done = list(filter(lambda x: line[x] == 1, range(M)))
        temp = list(filter(lambda x: line[x] == 1 or line[x] == 0, range(M)))
        for k in temp:
            pos.append((i, j, k))
        for k in done:
            q.append((0, i, j, k))

def check():
    max_day = 0
    for (z, x, y) in pos:
        if box[z][x][y] == 0:
            return False
        max_day = max(max_day, box[z][x][y])
    return max_day

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

if check():
    result = 0
else:
    while q:
        day, z, x, y = q.popleft()

        c = check()
        if c:
            result = c
            break

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                continue
            if box[nz][nx][ny] == -1:
                continue
            # 해당 위치
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = day + 1
                q.append((day+1, nz, nx, ny))


print(result)
