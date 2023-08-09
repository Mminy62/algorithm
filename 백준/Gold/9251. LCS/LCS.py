A = list(input().rstrip())
B = list(input().rstrip())
a_len = len(A)
b_len = len(B)
A = [0] + A
B = [0] + B
dp = [[0] * (b_len + 1) for _ in range(a_len + 1)]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] != B[j]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1

print(dp[a_len][b_len])