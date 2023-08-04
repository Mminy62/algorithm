from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().rstrip())))

visited = [[[False] * M for _ in range(N)] for _ in range(K+1)]
visited[0][0][0] = True
dist = [[0] * M for _ in range(N)]
dist[0][0] = 1

# N, M == 1, 1 -> 뭘 해도 1 (벽이 최소 1개이기에)
if (N, M) == (1, 1):
    print(1)
else:
    # 벽의 개수에 따라서 방문 배열을 늘린다.
    q = deque([(0, 0, 0)]) # x, y, wall
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = deque([])

    while q:
        x, y, wall = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            '''
            벽인 경우, 벽을 부술 수 있는지 확인 -> wall + 1 < H, visited False, maps 1
            벽 아닌 경우, maps == 0, visited False
            '''
            if 0 <= nx < N and 0 <= ny < M:
                # 벽인 경우, 벽을 부술 수 있는지 확인 -> wall + 1 < K, visited False, maps 1
                if maps[nx][ny] == 1 and wall + 1 <= K and not visited[wall + 1][nx][ny]:
                    visited[wall + 1][nx][ny] = True
                    q.append((nx, ny, wall + 1))
                    dist[nx][ny] = dist[x][y] + 1

                if maps[nx][ny] == 0 and not visited[wall][nx][ny]:
                    visited[wall][nx][ny] = True
                    q.append((nx, ny, wall))
                    dist[nx][ny] = dist[x][y] + 1

                if (nx, ny) == (N-1, M-1):
                    temp.append(dist[nx][ny])


    if temp:
        print(min(temp))
    else:
        print(-1)


