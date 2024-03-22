from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    cnt = 1
    while q:
        qlen = len(q)
        for _ in range(qlen):
            rx, ry, bx, by = q.popleft()
            for i in range(4):
                nrx, nry, nbx, nby = rx, ry, bx, by
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if a[nrx][nry] == 'O':
                        break
                    if a[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break

                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if a[nbx][nby] == 'O':
                        break
                    if a[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break

                if a[nbx][nby] == 'O':
                    continue
                if a[nrx][nry] == 'O':
                    print(cnt)
                    return

                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not c[nrx][nry][nbx][nby]:
                    c[nrx][nry][nbx][nby] = 1
                    q.append([nrx, nry, nbx, nby])

        cnt += 1
    print(-1)
    return

n, m = map(int, input().split())

a = []
for i in range(n):
    row = list(input().strip())
    a.append(row)
    for j in range(m):
        if a[i][j] == 'B':
            bx, by = i, j
            a[i][j] = '.'
        elif a[i][j] == 'R':
            rx, ry = i, j
            a[i][j] = '.'

q = deque()
c = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
q.append([rx, ry, bx, by])
c[rx][ry][bx][by] = 1
bfs()