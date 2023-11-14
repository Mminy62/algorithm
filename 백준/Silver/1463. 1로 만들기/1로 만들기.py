n = int(input())

dp = [0] * (n + 1)

if not n == 1:
    for i in range(2, n + 1):
        minValue = 1e9
        if not i % 3:
            minValue = min(minValue, dp[i//3] + 1)
        if not i % 2:
            minValue = min(minValue, dp[i//2] + 1)

        dp[i] = min(minValue, dp[i-1] + 1)

print(dp[n])