import sys
input = sys.stdin.readline

n, m = map(int, input().split())
clouds = [(n-2, 0), (n-2, 1), (n-1, 0), (n-1, 1)] #구름 좌표를 담은 리스트

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

commands = []
for _ in range(m):
    d, s = map(int, input().split())
    commands.append((d-1, s))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

rx = [-1, -1, 1, 1]
ry = [-1, 1, -1, 1]

for d, s in commands:
    # 1. 구름 이동
    for i in range(len(clouds)):
        x, y = clouds[i]
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        clouds[i] = (nx, ny)


        # 2. 구름 비 내리기
        graph[nx][ny] += 1

    for i in range(len(clouds)):
        x, y = clouds[i]
    # 3. 대각선 1 거리 체크
        cnt = 0
        for j in range(4):
            tx = x + rx[j]
            ty = y + ry[j]

            if tx < 0 or tx >= n or ty < 0 or ty >= n:
                continue
            if graph[tx][ty] > 0:
                cnt += 1

        graph[x][y] += cnt

    temp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and (i, j) not in clouds:
                temp.append((i, j))
                graph[i][j] -= 2


    clouds = temp


result = 0
for i in range(n):
    result += sum(graph[i])

print(result)