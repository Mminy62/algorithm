def solution(land): #dp문제

    n = len(land)
    dp = [[0] * 4 for _ in range(n)] # 40만
    
    dp[0] = land[0]
    
    for i in range(1, n):
        for j in range(4):
            value = dp[i-1][j]
            for k in range(4):
                if j != k:
                    temp = dp[i-1][k] + land[i][j]
                    if temp > value:
                        value = temp
            dp[i][j] = value
    
    return max(dp[n-1])