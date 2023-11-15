N = int(input())
hard = [0] + list(map(int, input().split()))
answer = []
Q = int(input())
question = []
for _ in range(Q):
    question.append(tuple(map(int, input().split())))

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = dp[i - 1]
    if hard[i] < hard[i-1]:
        dp[i] += 1

for start, end in question:
    answer.append(dp[end] - dp[start])

for i in range(Q):
    print(answer[i])