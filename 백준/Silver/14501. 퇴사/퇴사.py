n = int(input())

dp = [0] * (n+1)
array = [[0]]
max_value = 0

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(n, 0, -1):
    time = i + array[i][0]
    if time <= n + 1:#현재 날짜가 포함되는 경우
        dp[i] += array[i][1]
        if time <= n:# 현재 날짜의 상담 간격만큼 더해주는 경우
            dp[i] += dp[time]
        dp[i] = max(dp[i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)