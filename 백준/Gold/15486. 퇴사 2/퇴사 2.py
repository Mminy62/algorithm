import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    t, c = map(int, input().split())
    arr.append([t, c])

dp = [0] * (N + 1)

for i in range(N-1, -1, -1):
    ntime = i + arr[i][0]
    if i + arr[i][0] > N:
        cost = 0
        dp[i] = max(cost, dp[i + 1])
        continue
    cost = arr[i][1] + dp[ntime]
    dp[i] = max(dp[i + 1], cost)

print(dp[0])