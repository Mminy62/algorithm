from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
arr = []
q = deque([])
for i in range(N):
    temp = list(map(int, input().split()))
    pos = [i for i in range(M) if temp[i] == 1]
    for j in pos:
        q.append((i, j, 0))
    arr.append(temp)

flag = False
for i in range(N):
    if 0 in arr[i]:
        break
    if i == N - 1:
        flag = True

def BFS(q):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, cnt = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] != 0:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = cnt + 1
                q.append((nx, ny, cnt + 1))

answer = -1
if not flag:
    BFS(q)

    for i in range(N):
        if 0 in arr[i]:
            answer = -1
            break
        else:
            answer = max(answer, max(arr[i]))
else:
    answer = 0

print(answer)
