
n, m = map(int, input().split())
walls = list(map(int, input().split()))

# input 값 정리
# h, w 만큼 2차원 배열 만들기
graph = [[0] * m for _ in range(n)]

for j in range(len(walls)):
    for i in range(n-1, n-1-walls[j], -1):
        graph[i][j] = 1

starts = []
for i in range(n):
    for j in range(1, m):
        if graph[i][j] == 0 and graph[i][j-1] == 1:
            starts.append((i, j))

result = 0
for x, y in starts:
    cnt = 1

    while y + 1 < m:
        y += 1
        if graph[x][y] == 0:
            cnt += 1
        if graph[x][y] == 1:
            result += cnt
            break


print(result)


