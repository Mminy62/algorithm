import math

n = int(input())
dp = [0]

for i in range(1, n + 1):
    minValue = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j ** 2])
    dp.append(minValue + 1)

print(dp[n])