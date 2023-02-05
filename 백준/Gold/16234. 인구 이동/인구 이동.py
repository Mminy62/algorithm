from collections import deque
import math

N, L, R = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(N)]


def bfs(start):  # return units index list
    queue = deque([start])

    index_list = [start]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while (queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == 1:
                continue

            diff = abs(matrix[x][y]-matrix[nx][ny])
            if diff >= L and diff <= R:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                index_list.append((nx, ny))

    if len(index_list) == 1: #차이나는 주변국이 없는 경우
        return 0

    return index_list

def search():
    count = 0
    flag = 0
    global visited

    while (flag == 0):
        # bfs가 끝났음에도 uindx(차이 있는 주변국이 없으면)가 비어있으면 count 종료
        # bfs 로 주변국 탐색 시작
        uindex = []

        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1:
                    continue
                else:
                    visited[i][j] = 1
                    temp = bfs((i, j))
                    if temp != 0:
                        uindex.append(temp)
        if not uindex:
            flag = 1
            return count

        # 인구 이동 시작
        for countries in uindex:
            peos = 0
            for index in countries:
                x, y = index
                peos += matrix[x][y]

            peos = math.floor(peos // len(countries))
            for x, y in countries:
                matrix[x][y] = peos

        # 인구 이동 끝
        count += 1

        # 방문 초기화
        visited = [[0] * N for _ in range(N)]

print(search())