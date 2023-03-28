n = int(input())
days = [0] * (n + 1)
prices = [0] * (n + 1)
for i in range(1, n + 1):
    d, p = map(int, input().split())
    days[i], prices[i] = d, p

dp = [0] * (n + 1)
if days[n] == 1:
    dp[n] = prices[n]

for i in range(n - 1, 0, -1):
    # i -> today
    next_day = i + days[i]
    if next_day > n + 1:
        # n이 10인경우, 8일차 + 3일 - 1은 10이므로 8일차의 값을 더해도 된다.
        dp[i] = dp[i+1]
        continue
    if next_day == n + 1:
        # 같은 날엔 다음 next day 값을 더하지 않고 해당 날의 값만 비교한다.
        next_day = prices[i]
    else:
        next_day = prices[i] + dp[next_day]
    dp[i] = max(dp[i+1], next_day)

print(dp[1])