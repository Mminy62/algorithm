import sys
input = sys.stdin.readline

n = int(input())
array = [(0, 0)]
dp = [0] * (n+1)

for _ in range(n):
    array.append(tuple(map(int, input().split())))

if array[-1][0] == 1:
    dp[-1] = array[-1][1]

for i in range(n-1, 0, -1):
    time, pay = array[i]

    next_day = i + time
    if next_day > n + 1:
        dp[i] = dp[i + 1]
        continue
    if next_day == n + 1:
        next_day = max(dp[n], pay)
    else:
        next_day = pay + dp[next_day]

    dp[i] = max(dp[i + 1], next_day)

print(dp[1])