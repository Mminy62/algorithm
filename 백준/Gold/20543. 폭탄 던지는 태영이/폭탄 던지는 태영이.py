

N, M = map(int, input().split())
arr = [[0] * (N + 5) for _ in range(N + 5)]

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        arr[i][j] = row[j - 1] * -1

if M == 1:
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(arr[i][j], end=' ')
        print()
    exit()

def getSum(y, x):
    yy = max(0, y - M)
    xx = max(0, x - M)
    return sum[y][x] - sum[yy][x] - sum[y][xx] + sum[yy][xx]

sum = [[0] * (N + 5) for _ in range(N + 5)]
ans = [[0] * (N + 5) for _ in range(N + 5)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

        diff = arr[i][j] - getSum(i, j)
        if diff > 0:
            sum[i][j] += diff
            ans[i + M // 2][j + M // 2] += diff

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(ans[i][j], end=' ')
    print()