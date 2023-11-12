R, C, W = map(int, input().split())
N = R + W
dp = [[] for _ in range(N + 1)]

for i in range(0, N + 1):
    for j in range(0, i + 1):
        if i == 0 or j == 0 or j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])

result = 0
width = 0
for i in range(R - 1, R - 1 + W):
    col = C - 1
    width += 1
    for j in range(col, col + width):
        result += dp[i][j]

print(result)