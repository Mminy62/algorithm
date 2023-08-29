n = int(input())
array = list(map(int, input().split()))

dp = [1] * n

# top-down
for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))