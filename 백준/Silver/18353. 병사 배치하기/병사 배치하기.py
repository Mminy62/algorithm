import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[-1] = 1

for i in range(n - 2, -1, -1):
    for next_i in range(i + 1, n):
        if arr[i] > arr[next_i]:
            dp[i] = max(dp[i], dp[next_i] + 1)
    if dp[i] == 0:
        dp[i] = 1

print(n - max(dp))