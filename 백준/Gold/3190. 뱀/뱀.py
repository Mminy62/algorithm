from collections import deque
n = int(input())
matrix = [[0] * (n+1) for _ in range(n+1)]

#apple 1
for i in range(int(input())):
    x, y = map(int, input().split())
    matrix[x][y] = 1

# directions # 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 회전 정보
check_time = deque()
for i in range(int(input())):
    t, d = input().split()
    check_time.append((int(t), d))

x, y = 1, 1
matrix[x][y] = 2 #뱀의 몸 전체 위치 2
type = 0
time = 0
q = [(x, y)]

while(True):
    nx = x + dx[type]
    ny = y + dy[type]

    ## 범위안에 있고 뱀의 몸통이 없는 위치(사과를 1로 표시)
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and matrix[nx][ny] != 2:
        #사과가 없다면
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            #움직이고 지난 자리는 다시 0으로
            matrix[px][py] = 0

        #사과가 있다면
        if matrix[nx][ny] == 1:
            matrix[nx][ny] += 1
            q.append((nx, ny))
            #꼬리 안빼고 그냥 두기

    else:#벽이나 몸에 부딪힌 경우
        print(time+1)
        break

    x, y = nx, ny
    time += 1

    #초가 다 끝난 후에 회전(type 만 변경)
    if check_time and check_time[0][0] == time:
        c = check_time.popleft()
        if c[1] == 'D':
            type = (type + 1) % 4
        else:
            type = (type - 1) % 4