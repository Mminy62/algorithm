n = int(input())
landmine = []
matrix = []
users = []
for i in range(n):
    row = list(input())
    for j in range(n):
        if row[j] == '*':
            landmine.append((i, j))
    matrix.append(row)

for _ in range(n):
    users.append(list(input()))
# 인풋 정보하나식 matrix랑 -> x이고 그 좌표가 '*'이면 -> '*' 로 입력, 아니면 주변 탐색

# (-1, 0) ( 1, 0), ( 0, 1) (0, -1) (1, 1)(1, -1) (-1,-1)(-1, 1)
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

flag = 0
for i in range(n):
    for j in range(n):
        if users[i][j] == 'x':
            if matrix[i][j] == '*':
                users[i][j] = '*'
                flag = 1
            else:#주변 탐색
                cnt = 0
                for t in range(8):
                    nx = i + dx[t]
                    ny = j + dy[t]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if matrix[nx][ny] == '*':
                        cnt += 1

                users[i][j] = str(cnt)

        else:
            users[i][j] = '.'

if flag:
    for i, j in landmine:
        users[i][j] = '*'

for k in range(n):
    print(''.join(users[k]))