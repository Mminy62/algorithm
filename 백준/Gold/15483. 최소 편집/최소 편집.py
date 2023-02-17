A = input()
B = input()
a_length = len(A)
b_length = len(B)

dp = [[0] * (a_length + 1) for _ in range(b_length + 1)]

# 1행 초기화
dp[0] = [i for i in range(a_length + 1)]

# 1열 초기화
for i in range(b_length + 1):
    dp[i][0] = i

for i in range(1, b_length + 1):
    for j in range(1, a_length + 1):
        if A[j-1] == B[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

print(dp[b_length][a_length])