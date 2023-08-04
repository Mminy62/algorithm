from sys import stdin
from collections import deque

M,N,H = map(int, stdin.readline().split())
li = [[[0]*M for i in range(N)]for j in range(H)]
count_one = 0
count_minus =0
max_num = 1
queue = deque()

for i in range(H):
    for j in range(N):
        tmp = list(map(int, stdin.readline().split()))
        for k in range(M):
            li[i][j][k] = tmp[k]
            if tmp[k] == 1:
                queue.append((i,j,k))
                count_one +=1
            elif tmp[k] == -1:
                count_minus +=1

ans =M*N*H - count_minus

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
        
if ans - count_one== 0 :
    print(0)
else:
    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<= nx < M and 0<=ny < N and 0 <= nz < H:
                if li[nz][ny][nx] == 0:
                    li[nz][ny][nx] = li[z][y][x] +1
                    max_num = max(li[nz][ny][nx],max_num)
                    count_one +=1
                    queue.append((nz,ny,nx))
        
    if count_one == ans:
        print(max_num -1)
    else:
        print(-1)