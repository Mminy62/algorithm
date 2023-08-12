A = [0] + list(input().rstrip())
B = [0] + list(input().rstrip())

a_length = len(A)
b_length = len(B)

dp = [[0] * b_length for _ in range(a_length)]
result = 0
for i in range(1, a_length):
    for j in range(1, b_length):
        # if A[i] != B[j]:
        #     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            result = max(result, dp[i][j])

print(result)
