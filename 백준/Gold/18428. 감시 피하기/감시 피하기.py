from itertools import combinations

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(input().split())

x_loc = []
t_loc = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'X':
            x_loc.append((i, j))
        elif matrix[i][j] == 'T':
            t_loc.append((i, j))


xs = list(combinations(x_loc, 3))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        d_answer = True
        nx, ny = x, y

        while d_answer:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                d_answer = False
            elif matrix[nx][ny] == 'O':
                d_answer = False

            elif matrix[nx][ny] == 'S':
                return False

    return True

def check():
    for locations in xs:
        # 3개 벽 설치
        for loc in locations:
            x, y = loc
            matrix[x][y] = 'O'

        # 선생님 이동으로 확인
        count = 0
        for tx, ty in t_loc:
            if bfs(tx, ty): #하나라도 학생이 걸리면 검사 멈추기
                count += 1
        if count == len(t_loc):
            return "YES"

        # 벽 다시 제거
        for loc in locations:
            x, y = loc
            matrix[x][y] = 'X'

    return "NO"

print(check())