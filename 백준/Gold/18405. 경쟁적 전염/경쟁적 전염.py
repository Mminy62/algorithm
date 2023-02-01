from collections import deque

n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

time, rx, ry = map(int, input().split())
virus = [deque([]) for i in range(k+1)] #virus 좌표

for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
            virus[matrix[i][j]].append((i, j))

#bfs
for t in range(time):
    for index, v_coor in enumerate(virus):
        temp = []
        while v_coor: #1번 바이러스의 좌표들이 다 증식 될 때까지
            x, y = v_coor.popleft()

            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if matrix[nx][ny] > 0:
                    continue
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = index
                    temp.append((nx, ny))

        for data in temp:
            virus[index].append(data)


print(matrix[rx-1][ry-1])