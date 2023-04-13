graph = []
visited = [[0] * 5for _ in range(5)]

for _ in range(5):
    graph.append(list(map(int, input().split())))

mc_input = []
for _ in range(5):
    mc_input.append(list(map(int, input().split())))

def check_line():
    row, col, diag = 0, 0, 0
    c = [0, 0, 0, 0, 0]

    #row check
    for i in range(5):
        if sum(visited[i]) == 5:
            row += 1
    #col check
    for i in range(5):
        c[0] += visited[i][0]
        c[1] += visited[i][1]
        c[2] += visited[i][2]
        c[3] += visited[i][3]
        c[4] += visited[i][4]

    col = len(list(filter(lambda x: x == 5, c)))

    #diag check
    diag_cnt = 0
    for i in range(5):
        if visited[i][i] == 1:
            diag_cnt += 1
    if diag_cnt == 5:
        diag += 1

    diag_cnt = 0
    for i in range(5):
        if visited[i][4-i] == 1:
            diag_cnt += 1
    if diag_cnt == 5:
        diag += 1

    cnt = row + col + diag

    if cnt >= 3:
        return True
    else:
        return False
def pos(num):
    for i in range(5):
        if num in graph[i]:
            return (i, graph[i].index(num))

flag = 0
#input 호명
for i in range(5):
    for j in range(5):
        num = mc_input[i][j]
        x, y = pos(num)
        visited[x][y] = 1
        if check_line():
            print((i) * 5 + (j + 1))
            flag = 1
            break
    if flag:
        break
