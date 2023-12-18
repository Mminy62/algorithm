def solution(triangle):
    N = len(triangle)
    dp = []
    
    for i in range(N):
        M = len(triangle[i])
        dp.append([0] * M)
    dp[0][0] = triangle[0][0]
    
    for i in range(N-1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], triangle[i+1][j] + dp[i][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], triangle[i+1][j+1] + dp[i][j])
    
    return max(dp[-1])