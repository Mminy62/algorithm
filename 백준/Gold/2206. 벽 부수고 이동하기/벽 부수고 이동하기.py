import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
# input 지도
maps = []
for _ in range(N):
    maps.append(list(map(int, input().rstrip())))

if (N, M) == (1, 1):
    print(1)
else:

    # 방문 여부 & 벽 부순 여부로 3차원 배열 생성
    visited = [[[False] * M for _ in range(N)] for _ in range(2)]
    dist = [[0] * M for _ in range(N)]

    q = deque([(0, 0, 0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    # - 이동의 조건:
    # - 벽인 경우, 방문한적 없고 & 벽 부순적 없음(벽이면 원래 못 감)
    # - 벽이 아닌 경우, 방문한적 없음
    visited[0][0][0], visited[1][0][0] = True, True
    dist[0][0] = 1
    dist[N-1][M-1] = -1 # 방문하지 않았을 때의 default
    flag = 0
    temp = []
    while q:
        x, y, wall = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            flag = 0

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽인 경우 -> 현재 좌표까지 벽을 부순 적이 없고, 다음 상태에 방문한 적이 없는 경우,
            if maps[nx][ny] == 1 and wall == 0 and not visited[wall + 1][nx][ny]:
                visited[wall+1][nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny, wall+1))

            # 벽이 아닌 경우, 방문 여부만 중요
            if maps[nx][ny] == 0 and not visited[wall][nx][ny]:
                visited[wall][nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny, wall))

            if (nx, ny) == (N-1, M-1):
                temp.append(dist[nx][ny])

    result = 0
    if visited[0][N-1][M-1] or visited[1][N-1][M-1]: # n-1, m-1 에 방문 했다면
        dist[N-1][M-1] = min(temp)

    print(dist[N-1][M-1])
