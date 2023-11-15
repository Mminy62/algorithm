
N = int(input())
answer = []
dp = [0, 1, 2, 4]
dp += [0] * 13


for _ in range(N):
    num = int(input())

    if num < 4:
        answer.append(dp[num])

    else:
        for i in range(4, num + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        answer.append(dp[num])

for _ in range(N):
    print(answer[_])