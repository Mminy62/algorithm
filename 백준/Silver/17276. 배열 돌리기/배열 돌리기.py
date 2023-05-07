import sys
input = sys.stdin.readline

result = []
test_case = int(input())
for _ in range(test_case):
    array = []
    n, d = map(int, input().split())
    for _ in range(n):
        array.append(list(map(int, input().split())))

    if d < 0:
        d = 360 + d
    start = d // 45 - 1

    before = []
    before.append([array[i][i] for i in range(n)])
    before.append([array[i][(n+1)//2-1] for i in range(n)])
    before.append([array[n-i-1][i] for i in range(n-1, -1, -1)])
    before.append([array[(n+1)//2-1][i] for i in range(n-1, -1, -1)])

    after = [[0] * n for _ in range(n)]

    # rotate
    for b_i in range(4):
        index = (b_i + start) % 8

        if index == 0 or index == 4:
            if index == 0:
                for i in range(n):
                    after[i][(n + 1)//2-1] = before[b_i][i]
            if index == 4:
                for i in range(n):
                    after[n-i-1][(n + 1)//2-1] = before[b_i][i]

        if index == 1 or index == 5:
            if index == 1:
                for i in range(n):
                    after[i][n-i-1] = before[b_i][i]
            else:
                for i in range(n):
                    after[n-i-1][i] = before[b_i][i]
        if index == 2 or index == 6:
            if index == 2:
                for i in range(n):
                    after[(n+1)//2 -1][n-i-1] = before[b_i][i]
            else:
                for i in range(n):
                    after[(n+1)//2 -1][i] = before[b_i][i]
        if index == 3 or index == 7:
            if index == 3:
                for i in range(n):
                    after[n-i-1][n-i-1] = before[b_i][i]
            else:
                for i in range(n):
                    after[i][i] = before[b_i][i]

    # 남은 칸 채우기
    for i in range(n):
        for j in range(n):
            if after[i][j] == 0:
                after[i][j] = array[i][j]

    for a in range(n):
        result.append(after[a])

for _ in range(len(result)):
    print(*result[_])