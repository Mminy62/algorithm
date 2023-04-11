import sys
import copy
import heapq
input = sys.stdin.readline
n = int(input())

seats = [[0] * (n + 1) for _ in range(n + 1)]
#nx < 1 or nx > n
visited = [[0] * (n + 1) for _ in range(n + 1)]
graph = [0] * (n * n + 1)
order = []

#input 초기설정
for _ in range(n * n):
    temp = list(map(int, input().split()))
    graph[temp[0]] = temp[1:]
    order.append(temp[0])

def check(seats, fav): #좋아하는 학생이 자리에 있는지 확인
    for i in range(len(seats)):
        if fav in seats[i]:
            return (i, seats[i].index(fav))
    return (-1, -1)

def bfs(seats, fav_indexs, count_seats):
    n = len(seats) - 1
    fav_adj = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while fav_indexs:
        x, y = fav_indexs.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            if seats[nx][ny] == 0:
                count_seats[nx][ny] += 1
                fav_adj.append((nx, ny))

    return fav_adj, count_seats #좋아하는 학생의 인접한 자리와, count

def find_empty(seats, fav_indexs, count_seats):
    n = len(seats) - 1
    empty_pos = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while fav_indexs:
        x, y = fav_indexs.pop()
        empty = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            if seats[nx][ny] == 0:
                empty += 1

        heapq.heappush(empty_pos, (-empty, (x, y)))

    return heapq.heappop(empty_pos)[1]

def find_max(array):
    n = len(array)
    max_value = 0
    for i in range(n):
        max_value = max(max_value, max(array[i]))
    return max_value

def cal_fav(stu, seats, friends):
    n = len(seats) - 1
    flag = 0
    cnt = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if seats[i][j] == stu:
                x, y = i, j
                flag = 1
                break
        if flag:
            break
            
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
        if seats[nx][ny] in friends:
            cnt += 1

    if cnt == 0:
        return 0
    else:
        score = 10 ** (cnt - 1)
        return score

# 맨 처음 학생은 항상 (2, 2)에 존재한다.

seats[2][2] = order[0]

for stu in order[1:]:
    fav_adj = []
    fav_pos = []
    candi_seat = []
    for fav in graph[stu]:
        fav_index = check(seats, fav)
        if fav_index != (-1, -1):#만약에 아무도 없어
            fav_pos.append(fav_index)

    if fav_pos:
        count = copy.deepcopy(visited)
        fav_adj, count = bfs(seats, fav_pos, count)
        max_value = find_max(count)
        for i in range(len(fav_adj)):
            x, y = fav_adj[i]
            if count[x][y] == max_value:
                heapq.heappush(candi_seat, (x, y))

    # 2. 1을 만족하는 칸이 여러개면 주변의 비어있는 칸이 많은 칸으로 자리를 선정한다.
    if len(candi_seat) == 1:
        x, y = heapq.heappop(candi_seat)
        seats[x][y] = stu
        continue
    if len(candi_seat) < 1:#후보 자리가 없는 경우
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if seats[i][j] == 0:
                    candi_seat.append((i, j))
    # 2. 주변 빈칸이 더 많은 후보지 찾기
    candi_seat2 = []#2번째 후보 -> 주변 빈칸이 더 많은 후보지
    count2 = copy.deepcopy(visited)
    (x, y) = find_empty(seats, candi_seat, count2)

    seats[x][y] = stu

result = 0
for stu in order:
    result += cal_fav(stu, seats, graph[stu])

print(result)

