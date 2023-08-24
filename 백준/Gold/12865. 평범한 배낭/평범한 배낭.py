n, k = map(int, input().split())

array = []
for _ in range(n):
    w, v = map(int, input().split())
    array.append((w, v))

array.sort(key=lambda x: (x[0],-x[1]))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(k+1):
        w, v = array[i-1][0], array[i-1][1]
        if j-w >= 0:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
# 
# for _ in range(1, n + 1):
#     print(dp[_])

print(dp[n][k])
