import copy
import sys
input = sys.stdin.readline

N = int(input())
real = []
for i in range(N):
    real.append([0] * N)

students = []
favs_dict = {}
# 학생 입력 받을때 한명만 넣고, 나머지는 좋아하는 사람임
for i in range(N * N):
    temp = tuple(map(int, input().split()))
    students.append(temp)
    favs_dict[temp[0]] = temp[1:]
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(students):
    pos = (N + 1, N + 1)
    num = students[0]
    favorites = students[1:]
    temp_cnt = [0, 0] # num이 작성될 기준

    for i in range(N):
        for j in range(N):
            fav_cnt = 0
            empty_cnt = 0

            if real[i][j] == 0:# 빈 상태
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                        continue
                    if real[nx][ny] != 0 and real[nx][ny] in favorites:
                        fav_cnt += 1
                    if real[nx][ny] == 0:
                        empty_cnt += 1

                if temp_cnt[0] < fav_cnt:
                    temp_cnt = [fav_cnt, empty_cnt]
                    pos = (i, j)
                    continue

                if temp_cnt[0] == fav_cnt and temp_cnt[1] < empty_cnt:
                    temp_cnt = [fav_cnt, empty_cnt]
                    pos = (i, j)
                    continue

                if temp_cnt == [fav_cnt, empty_cnt] and pos[0] > i and pos[1] > j:
                    pos = (i, j)
                    continue

    return (pos, num)

idx = 0
result = 0
for i in range(N * N):
    pos, num = search(students[idx])
    real[pos[0]][pos[1]] = num
    idx += 1

for i in range(N):
    for j in range(N):
        num = real[i][j]
        fav_cnt = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]

            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if real[nx][ny] in favs_dict[num]:
                fav_cnt += 1

        if fav_cnt:
            result += 10 ** (fav_cnt - 1)

print(result)